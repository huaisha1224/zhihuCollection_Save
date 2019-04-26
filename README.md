**将知乎收藏和"我关注的问题"自动发送到Evernote/印象笔记/OneNote/有道云笔记中**

### 用到的库和程序
- Python_ver          = "Python3.6"
- selenium_ver        = "selenium3.141.0"


### 使用说明
由于知乎的反爬虫机制、原来的requests模式已经不能抓取数据了、所以本次全部重新用selenium来抓取数据;
- 你需要安装Chrome浏览器
- 安装对应Chrome版本对应的Chromedriver.exe
- 当然你也可以用Firefox浏览器

[Chromedriver.exe驱动程序](https://npm.taobao.org/mirrors/chromedriver/)




### 说明
- 目前完成了知乎数据的采集功能、并经过测试可以发送到OneNote里面
- 由于印象笔记免费版本的帐号不能接收邮件、所以暂时还没测试

### 接下来的安排
- 会支持印象笔记、Evernote、以及有道云笔记
- 通过配置文件的方式、填入个性化数据
- 打包成exe、方便使用
