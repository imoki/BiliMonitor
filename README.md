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
  
## docker使用方法
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
 
  
## docker程序文件说明
仅需配置config.json文件即可，每天会自动定时执行。  
config.json文件路径：/app/src/config/config.json  
1. uid填写up主的uid。  
2. cron填写定时时间，每天指定时间会执行任务。  
  
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
