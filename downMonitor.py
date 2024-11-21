"""
@author: imoki
@github: https://github.bom/imoki
@file: downMonitor.py
@time: 2024/11/21
@desc: bilibili视频下载脚本，支持bvid下载，支持bark推送消息。
        b站up最新合集视频监控。仅下载今天和昨天内容，且不会重复下载，保存在自定义文件夹下。
        根据bvid列表（合集）进行下载，填写bvidlist、savepath、key变量即可
"""

import json
import requests
import time
from datetime import datetime, timedelta, timezone
import os
from urllib.parse import quote


# 配置，自定义
bvidlist = ["BV第一个合集", "BV第二个合集"] # 需要下载的bvid列表
savepath = ".\\视频\\"    # 保存路径
key = "xxxxxxxx"  # bark推送的key


#  接口地址
apiinfourl = "https://bili.zhouql.vip/meta/"    # 获取媒体信息，aid,cid
apidownurl = "https://bili.zhouql.vip/download/"    # 获取下载地址

message = "【bili合集监控下载】\n"    # 待发送该消息

def send_bark_message(message, key):
    """
    发送Bark消息。

    参数:
    message (str): 要发送的消息内容。
    key (str): Bark应用程序的密钥。
    """
    # print("开始推送")

    url = f"https://api.day.app/{key}/{message}"
    response = requests.get(url)
    if response.status_code == 200:
        print("🚀 消息发送成功！")
    else:
        print(f"❌ 消息发送失败，状态码：{response.status_code}")


# 根据下载地址下载mp4文件
def download_file(download_url, save_path):
    """
    根据下载地址下载文件。

    参数:
    download_url (str): 下载地址。
    save_path (str): 保存路径。
    """
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(download_url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            content = "✅ 文件下载成功\n"
            writemessage(content)
        else:
            content = f"❌ 文件下载失败，状态码: {response.status_code}\n"
            writemessage(content)
    except Exception as e:
        content = f"❌ 文件下载失败，错误: {e}\n"
        writemessage(content)

# 获取当前日期并格式化为 YYYYMMDD
def get_current_date_formatted():
    """
    获取当前日期并格式化为 YYYYMMDD。

    返回:
    str: 格式化为 YYYYMMDD 的当前日期。
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y%m%d')
    return formatted_date
    
# 获取最新剧集信息
def get_latest_episode_id(bvid):

    """
    根据 BVID 获取最新集的 AID 和 CID。

    参数:
    bvid (str): BVID。

    返回:
    tuple: (AID, CID)。
    """

    url = apiinfourl + bvid
    # headers = {
    #     'Content-Type': 'application/json; charset=utf-8'
    # }
    resp = requests.get(url)
    # 设置响应的编码
    # resp.encoding = 'iso-8859-1'
    
    resp = resp.json()
    #print(resp)
    
    code = resp['code']
    result = []
    if(code== 0):
        # print("获取最新集成功")
        episodes = resp['data']['ugc_season']['sections'][0]['episodes']

        # 获取今天的日期
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        # day_before_yesterday = today - timedelta(days=2)
        
        
        # 从后往前遍历剧集列表
        count = 0
        for episode in reversed(episodes):
            if count >= 8:  # 最多往前看8个
                break
            
            # latest_episode = episodes[-1]
            title = episode['title']
            aid = episode['aid']
            cid = episode['cid']
            ctime = episode['arc']['ctime']
    
            # 将 ctime 转换为本地时间
            ctime_datetime = datetime.fromtimestamp(ctime, timezone.utc).astimezone()
            # print(ctime_datetime.date())
            # print(today)
            # print(yesterday)
            # 检查 ctime 的日期部分是否为今天或昨天，只要这两天视频
            if ctime_datetime.date() == today or ctime_datetime.date() == yesterday:
                episodesdict = {
                    "title": title,
                    "aid": aid,
                    "cid": cid,
                    "ctime": ctime
                }
                result.append(episodesdict)
            else:
                # print(f"找到第一个不是今天和昨天的剧集: {title}, AID: {aid}, CID: {cid}, ctime: {ctime}")
                break
            count += 1
        # print(result)
    return code, result

# 获取下载地址
def getdownurl(aid, cid):
    """
    根据 AID 和 CID 获取下载地址。

    参数:
    aid (int): 视频的 AID。
    cid (int): 视频的 CID。

    返回:
    str: 下载地址。
    """

    url = apidownurl + str(aid) + "/" + str(cid)
    resp = requests.get(url)
    resp = resp.json()
    code = resp['code']
    downurl = ""
    if(code== 0):
        downurl = resp['data']['durl'][0]['url']
        #print("[ + ] 获取下载地址成功")
    return code, downurl

def checkcid(cid):
    """
    检查 savepath 文件夹中是否存在名为 时间_cid.mp4 的文件。
    
    参数:
    cid (str): 视频的 CID。
    savepath (str): 存储视频的文件夹路径。
    
    返回:
    bool: 如果文件存在，则返回 True，否则返回 False。
    """
    # 遍历 savepath 文件夹中的所有文件
    for filename in os.listdir(savepath):
        # 检查文件名是否符合 时间_cid.mp4 的格式
        if filename.endswith(f"_{cid}.mp4"):
            print(f"🎊 文件已存在: {filename}")
            return True
    
    print(f"🪄 文件不存在: *_{cid}.mp4，执行下载操作")
    return False


def writemessage(content):
    """
    写入推送消息
    
    参数:
    content (string): 每一行的内容
    """
    global message
    print(content)
    message += content

if __name__ == "__main__":
    # 遍历bvidlist
    for bvid in bvidlist:
        content = "🎮️ 开始处理" + bvid + "\n"
        writemessage(content)

        code, result = get_latest_episode_id(bvid)
        # 等待几秒
        time.sleep(3)
        # 判断result数组长度是否为0
        if code == 0:
            if len(result) != 0:
                content = "✨ 总共检索到" + str(len(result)) + "个视频，开始处理\n"
                writemessage(content)
                # 便利result数组
                for item in result:
                    title = item['title']
                    aid = item['aid']
                    cid = item['cid']
                    ctime = item['ctime']
                    # print(f"最新集标题: {title}")
                    # print(f"最新集AID: {aid}")
                    content = f"🧸 最新集CID: {cid}\n"
                    writemessage(content)
                    # print(f"最新集时间: {ctime}")

                    # 检查是否已经下载过了
                    if checkcid(cid):
                        content = "🔮 已经下载过了\n"
                        writemessage(content)
                    else:
                        # 如果没下载则进行下载
                        code, downurl = getdownurl(aid, cid)
                        if code == 0:
                            print(f"🎯 下载地址: {downurl}\n")
                            time.sleep(3)
                            # 根据下载地址下载文件
                            # savepath = f"{title}.mp4"
                            name = str(get_current_date_formatted()) + "_" + str(cid) # "今天时间 + cid"

                            path = savepath + name +  ".mp4"
                            print(f"🕹️ 开始进行下载，保存路径: {path}\n")
                            download_file(downurl, path)

                            time.sleep(10)
                        else:
                            content = "❌ 获取下载地址失败\n"
                            writemessage(content)
            else:
                content = "🎈 没有最新集\n"
                writemessage(content)
        else:
            content = "❌ 获取最新集失败\n"
            writemessage(content)
            
    # print(message)
    message = quote(message)
    # print(message)
    send_bark_message(message, key)

        
