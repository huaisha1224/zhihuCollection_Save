####zhihu_to_evernote

**将知乎收藏和"我关注的问题"自动发送到Evernote/印象笔记中**

**Go语言版本请移步到[ZhihuToEvernote](https://github.com/huaisha1224/ZhihuToNote)**

**EXE执行文件请移步到[ZhihuToEvernote](https://github.com/huaisha1224/ZhihuToNote)下载**

###安装第三方库

- 1、安装requests 2.1.0版本的第三方库
- 2、安装BeautifulSoup 4.2版本的第三方库

###使用说明

- 1、请使用国内邮箱、以保证能正常发送邮件到印象笔记中
- 2、将login.py和zhihu_to_evernote.py文件下载到同一个目录下
- 3、修改config.ini里面的内容为自己真实信息
- 4、然后命令行下python zhihu_to_evernote.py即可

		python zhihu_to_evernote.py

###配置文件config.ini说明

	[info]
	url = http://www.zhihu.com/collection/20261977
	mail_host = smtp.126.com
	mail_user = huaisha******@126.com
	mail_password = password
	evernote_mail=huaisha*****@m.yinxiang.com
	notebook = 知乎收藏文章
	zhihu_email = no
	zhihu_password = no

**字段解释**

	[info]
	;知乎收藏页面的URL地址
	url = http://www.zhihu.com/collection/20261977
	;发送邮件的服务器
	mail_host = smtp.126.com
	;发送邮件的Email地址
	mail_user = huaisha****@126.com
	;登陆密码
	mail_password = password
	;接收邮件的Evernote地址
	evernote_mail=huaisha***@m.yinxiang.com
	;evernote上的一个笔记本、所有的收藏文章都会添加到这个笔记本下面，需要先有此笔记本
	notebook = 知乎收藏文章
	;下面2项为知乎账号密码/如果你需要吧"我关注的问题"也发送到Evernote那么填上账号密码,
	如果是把知乎收藏发送到Evernote的话下面2项请填写no
	zhihu_email = no
	zhihu_password = no


