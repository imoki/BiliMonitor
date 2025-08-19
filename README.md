<div align="center">
    <img src="https://socialify.git.ci/imoki/BiliMonitor/image?description=1&font=Rokkitt&forks=1&issues=1&language=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark">

<div id="shield">

[![][github-stars-shield]][github-stars-link]
[![][github-forks-shield]][github-forks-link]
[![][github-issues-shield]][github-issues-link]
[![][github-contributors-shield]][github-contributors-link]

<!-- SHIELD GROUP -->
</div>
</div>

## windows使用方法
项目右侧的**Releases**中下载最新版本，解压即可使用

## docker使用方法（linux使用方法，下载docker后拉取bilimonitor镜像即可使用）
1. 拉取Docker镜像  
```
docker pull imoki/bilimonitor:latest
```
  
2. 在宿主机（真机）中创建一个保存视频的目录，如  
```
mkdir /home/video
```
  
3. 运行Docker容器： 使用以下命令来运行Docker容器。 
命令中的**/home/video**是宿主机上用于存储视频文件的目录路径，你需要将其替换为实际的路径。  
```
docker run -d -v /home/video:/app/src/video imoki/bilimonitor:latest
```
  
4. 修改定时时间（默认为17:30，如果不需要修改则跳过此步骤）  
- 4.1 查看容器ID： 第一列默认就是容器ID。
```
docker ps -a
```
- 4.2 进入容器： 使用以下命令进入容器。
``` 
docker exec -it 容器ID /bin/bash  
```
- 4.3 修改定时时间： 使用以下命令修改定时时间。  
方法一：使用sed命令修改定时时间。（快捷方法）  
其中的12:00为修改后的时间，根据需要修改。  
```
sed -i 's/"cron": "[^"]*"/"cron": "12:00"/' /app/src/config/config.json
```
  
方法二：使用vim编辑config.json文件（常规方法）  
根据config.json文件说明，修改时间。  
```
vim /app/src/config/config.json  
```


5. 添加up主
- 方法一：使用sed命令添加指定up主uid（快捷方法）  
命令中的222103174，替换为要添加的up主uid。（uid在哔哩哔哩网页版up主空间右侧侧边栏可以看到）  
```
sed -i '/"uids": \[/a\ \ \ \ \ \ \ \ {"uid": "222103174","notes":""},' /app/src/config/config.json
```
   
- 方法二：或使用vim编辑config.json文件（常规方法）   
根据config_example.json.bak例子文件说明，添加up主的uid。  
```
vim /app/src/config/config.json  
```
 
  
## 程序文件说明
仅需配置config.json文件即可，每天会自动定时执行。  
config.json文件路径：/app/src/config/config.json  
1. uid填写up主的uid。  
2. cron填写定时时间，每天指定时间会执行任务。

## 🖥️ 二次开发步骤
windows平台，vscode编辑器，python3.9环境开发  
1. vscode 安装插件：PyQt  
并进行配置（以下D:\Python3913替换为你本地python路径）  
```
选项：
Pyqt-integration › Pyrcc: Cmd
'pyrcc' command file, you can also specify a path
填入：
D:\Python3913\Scripts\pyside6-rcc.exe

选项：
Pyqt-integration › Pyuic: Cmd
'pyuic' command file, you can also specify a path
填入：
D:\Python3913\Scripts\pyside6-uic.exe

选项：
Pyqt-integration › Qtdesigner: Path
Path of QT designer
填入：
D:\Python3913\Lib\site-packages\PySide6\designer.exe
```  
2. 下载此项目源码到本地，并进入主目录中
```
git clone https://github.com/imoki/BiliMonitor.git
cd BiliMonitor
```  
4. 安装第三方python库（若运行命令后依旧缺少某个库，则使用pip install xxx，单独安装，xxx为缺少的模块）  
```
pip install -r requirements.txt
```
4. UI界面编辑（采用图形化编辑UI界面需安装“Qt Designer”，以下用此工具编辑UI界面）  
4.1 在vscode中选择main.ui文件并右键点击，选择：PyQt: Edit in Designer。使用“Qt Designer”工具编辑完成并保存。  
4.2 在vscode中选择main.ui文件并右键点击，选择：PyQt: Compile form。会在主目录下自动生成Ui_main.py文件。  
编辑Ui_main.py文件的第607行
将
``` 
font2.setWeight(QFont.)
```  
改为：
```
font2.setWeight(QFont.Normal)
```
将
``` 
import resources_rc
```  
改为：
```
from . resources_rc import *
```
将主目录下的Ui_main.py内容覆盖掉modules下的ui_main.py内容   
4. 根据自己的需求修改程序逻辑代码  
基本只需要改“main.py”文件和“src”目录下的文件即可，其他代码无需改动。    
5. 运行
```
python main.py
```

6. 打包成EXE可执行文件  
版本格式：主版本号.次版本号.修订号（如 v5.7.0）  
版本递增规则：  
修复bug时增加修订号（第三位）：v5.7.0 → v5.7.1  
小功能更新时增加次版本号（第二位）：v5.7.0 → v5.8.0  
大功能更新或架构更新时增加主版本号（第一位）：v5.7.0 → v6.0.0  
```
pyinstaller -w -i ./icon/icon.ico --name=BiliMonitor_v5.7.0.exe -F main.py 
```

7. 上传项目到github，可执行文件的压缩包上传到releases，即可成为项目贡献者     
  
### 👑 参考项目
PyDracula  
https://github.com/Wanderson-Magalhaes    
API  
https://github.com/SocialSisterYi  
RayWangQvQ  
https://github.com/RayWangQvQ/BiliBiliToolPro  
周棋洛  
https://github.com/Zhouqluo  


<!-- LINK GROUP -->

[github-codespace-link]: https://codespaces.new/imoki/BiliMonitor
[github-codespace-shield]: https://github.com/imoki/BiliMonitor/blob/main/images/codespaces.png?raw=true
[github-contributors-link]: https://github.com/imoki/BiliMonitor/graphs/contributors
[github-contributors-shield]: https://img.shields.io/github/contributors/imoki/BiliMonitor?color=c4f042&labelColor=black&style=flat-square
[github-forks-link]: https://github.com/imoki/BiliMonitor/network/members
[github-forks-shield]: https://img.shields.io/github/forks/imoki/BiliMonitor?color=8ae8ff&labelColor=black&style=flat-square
[github-issues-link]: https://github.com/imoki/BiliMonitor/issues
[github-issues-shield]: https://img.shields.io/github/issues/imoki/BiliMonitor?color=ff80eb&labelColor=black&style=flat-square
[github-stars-link]: https://github.com/imoki/BiliMonitor/stargazers
[github-stars-shield]: https://img.shields.io/github/stars/imoki/BiliMonitor?color=ffcb47&labelColor=black&style=flat-square
[github-releases-link]: https://github.com/imoki/BiliMonitor/releases
[github-releases-shield]: https://img.shields.io/github/v/release/imoki/BiliMonitor?labelColor=black&style=flat-square
[github-release-date-link]: https://github.com/imoki/BiliMonitor/releases
[github-release-date-shield]: https://img.shields.io/github/release-date/imoki/BiliMonitor?labelColor=black&style=flat-square
[pr-welcome-link]: https://github.com/imoki/BiliMonitor/pulls
[pr-welcome-shield]: https://img.shields.io/badge/🤯_pr_welcome-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge
[github-contrib-link]: https://github.com/imoki/BiliMonitor/graphs/contributors
[github-contrib-shield]: https://contrib.rocks/image?repo=imoki%2FBiliMonitor
[docker-pull-shield]: https://img.shields.io/docker/pulls/imoki/BiliMonitor?labelColor=black&style=flat-square
[docker-pull-link]: https://hub.docker.com/repository/docker/imoki/BiliMonitor
[docker-size-shield]: https://img.shields.io/docker/image-size/imoki/BiliMonitor?labelColor=black&style=flat-square
[docker-size-link]: https://hub.docker.com/repository/docker/imoki/BiliMonitor
[docker-stars-shield]: https://img.shields.io/docker/stars/imoki/BiliMonitor?labelColor=black&style=flat-square
[docker-stars-link]: https://hub.docker.com/repository/docker/imoki/BiliMonitor
[starchart-shield]: https://api.star-history.com/svg?repos=imoki/BiliMonitor&type=Date
[starchart-link]: https://api.star-history.com/svg?repos=imoki/BiliMonitor&type=Date
