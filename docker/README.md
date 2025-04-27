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