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

## ✨ 简介
b站up最新合集视频监控。仅下载今天和昨天内容，且不会重复下载，保存在自定义文件夹下。

## 🍨 教程 
方法1：直接用python运行
```python
python downMonitor.py
``` 
  
方法2：将bat脚本加入开机自启动，开机时自动打开最新一期视频。  
加入开机自启动，快捷键win+R，输入以下命令打开的startup文件夹：  
```
shell:startup
```  
再将bat脚本加入打开的startup文件夹中。  
bat内的路径需修改为实际路径。默认执行当前文件加内的downMonitor.py脚本  
此时就完成了，开机时会自动启动。 

方法3：加入windows定时任务
将脚本放入定时任务中，可设置每隔一天执行一次，有新合集视频则会下载。


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
