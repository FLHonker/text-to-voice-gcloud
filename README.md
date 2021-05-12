# Google Text-to-Speech 演讲稿批量处理

鉴于目前新冠疫情，大多数学术会议都采用了线上会议的方式，要求投稿人录制一个10分钟左右的短视频来介绍自己的视频。大多数人会做一个PPT，然后写一个稿子，一边放PPT一边念稿子，录下屏幕生成录像。如果不小心念错了，要么整个重来，要么就得后期处理了。有没有方式能够快速制作学术会议的演讲录像呢？

关于以上问题请先参考[知乎:5分钟，快速制作学术会议的演讲录像](https://zhuanlan.zhihu.com/p/195730992)。
这里主要提供[Google TTS](https://cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize) API 的批量处理解决方案。

对于`Google TTS`网页端的试用非常有限，像其他大多数免费的text-to-voice网站一样，有一定的次数限制，并不能帮助你完成整篇稿子的转译。所以，只能利用API服务，通过命令行方式批量处理。

## 准备工作

1. 首先，确保你的本地计算机能全局访问google， 如果你自己拥有一台海外的Linux系统的vps最好了；
2. 注册、登录Google Cloud；
3. 完成Google官方指导的准备工作 -- [快速入门：使用命令行](https://cloud.google.com/text-to-speech/docs/quickstart-protocol)；
4. 安装依赖项: python3, curl
5. 下载本仓库。

## 使用方法

1. 使用word等编辑好你的演讲稿，根据你的PPT，每页写一段，不要换行。将文本复制到`text.txt`文档中，还是强调：每页PPT的内容放一行，使用回车分隔每段。仓库的[text.txt](./text.txt)提供了样例。
2. 将[gcloud_token.json](./gcloud_token.json) 替换为你下载的Google Cloud 访问密钥。
3. 运行脚本，为每一张PPT的文本生成语音文件:
   ```python
   python3 text2voice_goo.py 
   ```
   整个text to speech处理过程在1分钟以内。
4. 根据语音文件编号放进你的每页PPT中，导出视频文件即可。


## 注意事项

1. `request.json`文件不要修改，它提供了`curl`命令所需要的模板。
2. 当然，python脚本中本应利用更高效和可移植的`requests`或`urllib3`库，当时经过测试，通过google密钥访问总是拒绝，故还是使用官方建议的`curl`命令行。
3. 建议使用Linux系统，windows在安装Google Cloud SDK时需要配置全局VPN。
4. 如果您的Google Cloud服务开通存在困难，可以联系我提供`gcloud_token.json`文件访问和使用我的API。

## About

后面搭个公开网站方便大家伙儿使用🤣🤣🤣~

Contact: Frank (frankliu624@outlook.com)

