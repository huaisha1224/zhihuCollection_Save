**将知乎收藏和"我关注的问题"自动发送到Evernote/印象笔记/OneNote/有道云笔记中**

### 用到的库和程序
- Python_ver          = "Python3.6"
- selenium_ver        = "selenium3.141.0"


### 使用说明
由于知乎的反爬虫机制、原来的requests模式已经不能抓取数据了、所以本次全部重新用selenium来抓取数据;
- 安装selenium `pip install selenium
- 需要安装Chrome浏览器
- 安装Chrome版本对应的Chromedriver.exe
- 当然你也可以用Firefox浏览器
- 修改config.ini配置文件
- python zhihuCollection_Save.py

[Chromedriver.exe驱动程序](https://npm.taobao.org/mirrors/chromedriver/)




### 配置文件说明
    [zhihu] # 知乎收藏地址和帐号信息
    url = https://www.zhihu.com/collection/20261977
    zhihu_user = sam.hxq@gmail.com
    zhihu_password = xxxxxx

    [email] #用于登录并发送邮件
    mail_host = smtp.126.com
    mail_user = huaisha1224@126.com
    mail_password = xxxxx

    [evernote]  # 印象笔记/Evernote/OneNote/有道云笔记的邮件接收地址
    to_mail= huaisha1224@m.yinxiang.com 



### 接下来的安排

- [x] 支持印象笔记、Evernote
- [x] 通过配置文件的方式、填入个性化数据    
- [x] 支持有道云笔记
- [x] 打包成exe、方便使用


### 给个笔记的接收邮箱
- OneNote的接受邮件：me@onenote.com(需要在onenote后台添加发送邮件)
- 有道云笔记：save@note.youdao.com(需要在有道云笔记后台添加发送邮件)
- 印象笔记：huaisha1224@m.yinxiang.com(在印象笔记后台获取邮件地址)
