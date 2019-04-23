#### zhihu_to_evernote

**将知乎收藏和"我关注的问题"自动发送到Evernote/印象笔记/OneNote/有道云笔记中**

###用到的库和程序
- Python_ver          = "Python3.6"
- selenium_ver        = "selenium3.141.0"
- Chrome_ver          = "Chrome73"
- chromedriver_Ver    = "2019/03/07版本"

### 使用说明、
由于知乎的反爬虫机制、原来的requests模式已经不能抓取数据了、所以本次全部重新用selenium来抓取数据
- url=‘知乎收藏地址’
- username=‘之后帐号’
- password=‘密码’
- smtp = "smtp.126.com"   # 发送邮件的SMTP地址
- send_mail = "huaisha1224@126.com"   # 发送邮件的帐号
- send_mail_pwd = "1qaz2wsx"  #   发送邮件密码
- to_mail = 'me@OneNote.com'  # 接受邮件的帐号、按实际情况填写、OneNote不需要才


### 说明
- 目前完成了知乎数据的采集功能、并经过测试可以发送到OneNote里面
- 由于印象笔记免费版本的帐号不能接收邮件、所以暂时还没测试

### 接下来的安排
- 会支持印象笔记、Evernote、以及有道云笔记
- 通过配置文件的方式、填入个性化数据
- 打包成exe、方便使用
