#!/usr/bin/env python
#!encoding:utf-8
#!filename:login.py

"""
由于获取"我关注的问题"需要先登录知网站之后才能取到
"我关注的问题"的列表。
本模块用于模拟浏览器登录知乎网站.
"""

import requests
import re

def Login_Zhihu(email,password):
    """先登录知乎网站之后才能访问"我关注的问题"列表
    """

    zhihu_login = r"http://www.zhihu.com/login"
    login_status = "我关注的问题"
    global zhihu_status
    global zhihu_session
    zhihu_session = requests.Session() #用requests设置cookie
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0)\
        Gecko/20100101 Firefox/24.0",
        "Referer":"http://www.zhihu.com/login"
            }

    #提交账号密码
    logininfo = {"email":email,
                "password":password,
                "sign-button":"登录"}

    #post登录知乎网站
    login = zhihu_session.post(zhihu_login,data=logininfo, headers=headers, timeout=10)
    #print (post.text)
    if login.status_code == 200: #判断是否post成功
        html_text = login.text

        if re.search(login_status, html_text) != None:#判断登录状态
            print ("Login Success")
            zhihu_status = "Login Success"

        else:
            print ("Login Failure")
            zhihu_status = "Login Failure"


#==============================================================================
if __name__ == "__main__":
    email = "sam.hxq@gmail.com"
    password = "password"
    Login_Zhihu(email,password)
    print (zhihu_status)

