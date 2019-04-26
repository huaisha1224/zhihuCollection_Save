# !/usr/bin/env python3
# encoding = utf-8
__author__ = "Sam.huang"

from selenium import webdriver
from configparser import ConfigParser
import email.mime.multipart
import email.mime.text
import smtplib
import time
import os

"""
将知乎收藏问答页面的所有问答保存到Evernote/印象笔记/OneNote/有道云笔记中

整体思路大概是下面这个样子的
1.  先通过知乎收藏地址的获取到所有的问题URL
2.  访问单个问题URL
3.  提取出问题名称、和内容
4.  通过邮件的形式发送到印象笔记、OneNote和有道云笔记


Python_ver          = "Python3.6"
selenium_ver        = "selenium3.141.0"
Chrome_ver          = "Chrome73"
chromedriver_Ver    = "2019/03/07版本"

"""



# ======================================================================================================================

def get_question_url():
    """
    获取知乎收藏里面的所有回答URL地址
    """
    # 从配置文件读取知乎收藏地址
    config = ConfigParser()
    config.read('config.ini', encoding='UTF-8')
    url = config['zhihu']['url']

    global question_list
    question_list = []
    br = webdriver.Chrome()
    br.get(url)
    while True:
        for i in range(1, 11):  # 一页最多有10个回答、获取所有回答的url
            try:
                code = ('/html/body/div[3]/div[1]/div/div[2]/div[%s]/h2/a' % i)
                question = br.find_element_by_xpath(code)
                if question:
                    question_url = question.get_attribute('href')  # 收藏的问题url
                    print(question_url)
                    question_list.append(question_url)  # 把url添加到列表里面
                else:
                    print(code)
            except Exception:  # 没有10个回答、中断循环
                pass

        try:
            next_page = br.find_element_by_link_text('下一页')  # 继续下一页的收藏
            if next_page:
                next_page.click()   # 进入下一页
                print('~~~~下一页~~~~')
        except Exception:
            for x in question_list:  # 把列表里面的url写入到文件、下次不需要重新获取
                with open('zhihuQuestionUrl.txt', 'a') as f:
                    f.write(x)
                    f.write('\n')
            print("~~~~所有收藏问题URL采集完成！~~~~~")
            break


# ======================================================================================================================

def start_zhihu_question():
    """
    获取回答页面的问题标题和问题内容
    """
    # 从配置文件读取知乎帐号密码
    config = ConfigParser()
    config.read('config.ini', encoding='UTF-8')
    username = config['zhihu']['zhihu_user']
    password = config['zhihu']['zhihu_password']

    # 如果找不到知乎问题URL列表 就调用函数去获取列表
    if not os.path.exists('zhihuQuestionUrl.txt'):
        print('~~~~本地找不到知乎URL列表~~~~')
        get_question_url()  # 调用函数获取知乎URL列表

    with open('zhihuQuestionUrl.txt', 'r') as f:
        url_list = f.readlines()

    for url in url_list:
        print(url)
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-automation'])   # 设置浏览器为开发者模式
            br = webdriver.Chrome(options=options)
            br.get(url)
            question_title = br.find_element_by_xpath(
                '/html/body/div[1]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1')

            if not question_title:  # 如果获取标题失败、说明需要登录、登录一波
                username = br.find_element_by_name('username')
                username.click()
                username.send_keys(username)  # 知乎帐号

                password = br.find_element_by_name('password')
                password.click()
                password.send_keys(password)   # 知乎密码

                loginButton = br.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button')
                loginButton.click()
            # 获取问题的名称、用于作为邮件的标题
            question_name = question_title.text
            print(question_name)

            content = br.find_element_by_xpath("//*").get_attribute("outerHTML")    # 获取html格式的内容
            sendMail(question_name, content)    # 发送邮件
            time.sleep(5)
            br.close()
        except Exception:
            pass


# ======================================================================================================================
def sendMail(question_name, question_content):
    """
    用问题的title作为邮件主题。
    用webdriver下载页面内容、然后用smtplib发送html内容到
    Evernote的邮件地址中，Evernote会自动添加到笔记本中.
    """
    config = ConfigParser()
    config.read('config.ini', encoding='UTF-8')
    smtp = config['email']['mail_host']  # 发送邮件的SMTP地址
    mail_user = config['email']['mail_user']  # 发送邮件的帐号
    mail_password = config['email']['mail_password']  # 发送邮件密码
    to_mail = config['evernote']['to_mail']    # 接受邮件的帐号

    msg = email.mime.multipart.MIMEMultipart()  # 创建消息对象
    msg['from'] = mail_user  # 指定发件人
    msg['to'] = to_mail  # 指定收件人
    msg['subject'] = question_name  # 邮件主题

    text = email.mime.text.MIMEText(_text=question_content, _subtype="html")  # _text代表邮件内容，_subtype代表邮件内容的发送形式
    msg.attach(text)
    try:
        em = smtplib.SMTP_SSL()
        em.connect(smtp)
        em.login(mail_user, mail_password)
        em.sendmail(from_addr=mail_user, to_addrs=to_mail, msg=msg.as_string())
        em.quit()
        print('~~~~~邮件发送完成~~~~')
    except Exception:
        print('~~~~~邮件跑丢了、跳过跳过~~~~~~')


if __name__ == "__main__":
    start_zhihu_question()
