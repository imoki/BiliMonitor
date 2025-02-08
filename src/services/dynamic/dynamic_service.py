
# from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialogButtonBox, QTableWidgetItem

from ...views.prompt_view import PromptView
from ...views.table_view import TableView

from datetime import datetime, timedelta, timezone
import subprocess

import json
import requests
import time
import os
from urllib.parse import quote
import random
import math
import qrcode
import threading
import gzip
from io import BytesIO
import re

class DynamicService():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '') 
        self.table = kwargs.get('table', '') 
        self.key = kwargs.get('key', '')  # "uids"
        self.unique = kwargs.get('unique', '')
        self.configManager = kwargs.get('configManager', '')
        self.rowCount = 10
        self.realTimeLogService = ""
        self.logService = ""
        self.prompt_view = PromptView(self.parent)

        #  bilibili官方接口地址
        self.apiinfourl = "https://api.bilibili.com/x/web-interface/view"    # 获取媒体信息，aid,cid
        self.apidownurl = "https://api.bilibili.com/x/player/playurl"    # 获取下载地址
        self.apidynamicurl = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?host_mid="  # 获取动态
        self.message = "【bilibili视频下载】\n"    # 待发送该消息
        self.downMaxCount = 3    # 下载失败最大重试次数
        self.urlMaxCount = 3    # 获取下载地址最大重试次数
        self.recentCount = 5    # 动态获取最近几条数据
    # 加载配置表格
    def load_table(self):
        tableView = TableView(parent = self.parent, table = self.table)

        data = self.configManager.read_config(self.key)
        if not data:
            data = []
            
        # 表格处理
        if len(data) + 1 < self.rowCount:
            self.table.setRowCount(self.rowCount)
        else:
            self.table.setRowCount(len(data) + 1)
        
        # 定义列的顺序和对应的键名
        column_order = ["uid", "name", "notes"]
        column_names = {
            "uid": "ID",
            "name": "名称",
            "notes": "备注",
        }

        # 设置表头
        header_labels = [column_names[col] for col in column_order if col in column_names]
        self.table.setHorizontalHeaderLabels(header_labels)

        for rowIndex, row in enumerate(data):
            for colIndex, column in enumerate(column_order):
                if column in row:
                    value = row[column]
                    tableView.setItem(rowIndex + 1, colIndex, value)

    # 表格创建
    def table_create(self):
        # 弹出框标题
        title = "添加UP主"
        # 弹出框内容
        labels = [
            {
                'label': "ID",
                'value': "",
                'type': "QLineEdit",
            },
            {
                'label': "名称",
                'value': "",
                'type': "QLineEdit",
            },
            {
                'label': "备注",
                'value': "",
                'type': "QLineEdit",
            }
        ]

        table_dict = {
            "key" : self.key,
            "title" : title,
            "labels": labels,
        }
        
        tableView = TableView(parent = self.parent, table_dict = table_dict)
        tableView.table_dialog_accepted.connect(self.handle_dialog_accept_create)
        tableView.create_dialog()
        tableView.handle_dialog_accept()

    # 表格创建，处理信号
    def handle_dialog_accept_create(self, edits):
        # print(self.key , " accept")
        # print(edits)
        signal_name = edits.get("name")
        if signal_name != self.key:
            return
        # print(self.key, " 接收成功")
        status = edits.get("status")
        if status == "cancel":
            self.prompt_view.prompt(text="编辑取消", type="warning")
        else:
            signal_value = edits.get("value")
            item_text_1 = signal_value.get("ID")
            item_text_2 = signal_value.get("名称")
            item_text_3 = signal_value.get("备注", "")

            # 数据输入校验
            # 去除空格和换行
            item_text_1 = item_text_1.strip()
            if not item_text_1:
                self.prompt_view.prompt(text="ID不能为空", type="warning")
                return

            dict_data = {
                "uid": item_text_1,
                "name": item_text_2,
                "notes": item_text_3,
            }

            # 读取配置文件中的数据
            content = self.configManager.read_config(self.key)
            if content:
                for item in content:
                    if item[self.unique] == item_text_1:
                        self.prompt_view.prompt(text=f"{item_text_1} 已存在", type="warning")
                        return

                # 没有相同的则添加，则向key中添加dict
                content.append(dict_data)
                self.configManager.update_config(self.key, content)
                self.prompt_view.prompt(text="编辑成功", type="success")
                self.load_table()
            else:
                # 说明没有指定key
                content = [dict_data]
                self.configManager.update_config(self.key, content)
                self.prompt_view.prompt(text="编辑成功", type="success")
                self.load_table()

    def table_edit(self):
        row = self.table.currentRow()

        item_1 = self.table.item(row, 0)
        item_2 = self.table.item(row, 1)
        item_3 = self.table.item(row, 2)

        if not item_1 or not item_2:
            self.prompt_view.prompt(text="无法编辑此行", type="warning")
            return

        item_1 = item_1.text()
        item_2 = item_2.text()
        item_3 = item_3.text() if item_3 else ""

        # 弹出编辑框基础配置
        # 弹出框标题
        title = "编辑UP主"
        # 弹出框内容
        labels = [
            {
                'label': "ID",
                'value': item_1,
                'type': "QLineEdit",
            },
            {
                'label': "名称",
                'value': item_2,
                'type': "QLineEdit",
            },
            {
                'label': "备注",
                'value': item_3,
                'type': "QLineEdit",
            }
        ]

        table_dict = {
            "key" : self.key,
            "title" : title,
            "labels": labels,
        }
        
        tableView = TableView(parent = self.parent, table_dict = table_dict, edit_row = row)
        tableView.table_dialog_accepted.connect(self.handle_dialog_accept_edit)
        tableView.create_dialog()
        tableView.handle_dialog_accept()
    
    # 表格编辑，处理信号
    def handle_dialog_accept_edit(self, edits):
        # print(self.key, " edit accept")
        signal_name = edits.get("name")
        if signal_name != self.key:
            return
        # print(self.key, " edit 接收成功")

        status = edits.get("status")
        if status == "cancel":
            self.prompt_view.prompt(text="编辑取消", type="warning")
        else:
            row = edits.get("edit_row") # 记录的是真实行，从0开始。实际不可能为0，因为0为表头
            # print("row", row)
            signal_value = edits.get("value")
            item_text_1 = signal_value.get("ID")
            item_text_2 = signal_value.get("名称")
            item_text_3 = signal_value.get("备注", "")

            # 读取配置文件数据
            items = self.configManager.read_config(self.key)
            # 除当前行外，校验是否存在其它同名数据 
            index = row - 1 # 表格行索引转配置索引，配置索引比表格行所以小1
            for i in range(0, len(items)):
                if i != index and items[i][self.unique] == item_text_1:
                    self.prompt_view.prompt(text=f"{item_text_1} 已存在", type="warning")
                    return

            # 对cookie进行格式化校验

            # 更新某一行表格中显示的数据
            tableView = TableView(parent = self.parent, table = self.table)
            tableView.setItem(row, 0, item_text_1)
            tableView.setItem(row, 1, item_text_2)
            tableView.setItem(row, 2, item_text_3)

            # 更新配置文件中的数据
            if items:
                # 从0开始，所以要减1
                if 0 <= index < len(items):
                    items[index]["uid"] = item_text_1
                    items[index]["name"] = item_text_2
                    items[index]["notes"] = item_text_3

                self.configManager.update_config(self.key, items)
            self.prompt_view.prompt(text="编辑成功", type="success")

    # 删除表格中的某行。
    def table_delete_selected_rows(self):
        """
        删除表格中的某行。
        :param table: 表格对象
        :param key: 配置文件中的key
        :param unique: 比较的key
        
        """
        # for i in self.table.selectedItems():
        #     print(f"获取到了第{i.row()}行，第{i.column()}列，元素为{i.text()}")
        
        row = self.table.currentRow()
        # 获取当前行的数据
        item = self.table.item(row, 0)
        if not item:
            self.prompt_view.prompt(text="无法删除此行", type="warning")
            return

        itemtext = item.text()
        # print(itemtext)

        # 删除表格中的行
        self.table.removeRow(row)

        # 更新配置文件中的数据
        content = self.configManager.read_config(self.key)
        if content:
            content = [item for item in content if item[self.unique] != itemtext]
            self.configManager.update_config(self.key, content)

        self.prompt_view.prompt(text="删除成功", type="success")

    
    # 添加id（已废弃）
    def add_id(self):
        value = self.parent.ui.textEdit_home_2.toPlainText()
        # 对输入的值进行格式化处理，去除空格
        value = value.strip()

        if not value:
            self.prompt_view.prompt(text="请填写uid", type="warning")
            return
        self.prompt_view.prompt(text="添加成功", type="success")

        content = self.format_id(value)
        if content is None:
            self.prompt_view.prompt(text=f"{value} 已存在", type="warning")
            return

        self.configManager.update_config("uids", content)
        self.parent.ui.textEdit_home_2.clear()

    # （已废弃）
    def format_id(self, value):
        # 对获取的id进行格式化
        dict = {
            "uid": value,
            "name": "",
        }

        content = self.configManager.read_config(self.key)
        # 便利配置查看是否有相同的，如果相同则不添加
        if content:
            for item in content:
                if item["uid"] == value:
                    return None # 已存在uid
            # 没有相同的则添加，则向key中添加dict
            content.append(dict)
        else:
            # 说明没有指定key
            content = [dict]
        
        return content

     ###############################运行功能相关###############################

    # 通过bvid获取cid
    # 根据单个bvid获取AID和CID。配合动态id获取
    def getaidcid(self, bvid):

        """
        根据 单个BVID 获取 AID 和 CID。

        参数:
        bvid (str): BVID。

        返回:
        tuple: (AID, CID)。
        """

        url = self.apiinfourl

        params = {
            'bvid': bvid
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        # headers = {
        #     'Content-Type': 'application/json; charset=utf-8'
        # }

        try:
            # resp = requests.get(url)
            resp = requests.get(url,headers=headers, params=params)
            # 设置响应的编码
            # resp.encoding = 'iso-8859-1'
            
            resp = resp.json()
            # print(resp)
            
            code = resp['code']
            result = []
            if(code== 0):
                # print("获取最新集成功")
                aid = resp['data']['aid']
                cid = resp['data']['cid']
                title = resp['data']['title']
                ctime = resp['data']['ctime']

                episodesdict = {
                    "title": title,
                    "aid": aid,
                    "cid": cid,
                    "ctime": ctime
                }
                result.append(episodesdict)
        except Exception as e:
            content = f'🚨 获取最新集的 AID 和 CID 失败，错误: {e}'
            # print(content)
            code = 1
            result = []

        return code, result

    # 获取下载地址
    def getdownurl(self, aid, cid):
        """
        根据 AID 和 CID 获取下载地址。

        参数:
        aid (int): 视频的 AID。
        cid (int): 视频的 CID。

        返回:
        str: 下载地址。
        """

        # url = self.apidownurl + str(aid) + "/" + str(cid)
        url = self.apidownurl

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        params = {
            'avid': aid,
            'cid': cid
        }

        # print(url)
        try:
            # resp = requests.get(url)
            resp = requests.get(url,headers=headers, params=params)
            resp = resp.json()
            # print(resp)
            code = resp['code']
            downurl = ""
            if(code== 0):
                downurl = resp['data']['durl'][0]['url']
                #print("[ + ] 获取下载地址成功")
        except Exception as e:
            content = f"🚨 获取下载地址失败，错误: {e}"
            # print(content)
            code = 1
            downurl = ""
        return code, downurl


    # 根据下载地址下载mp4文件
    def download_file(self, download_url, save_path):
        """
        根据下载地址下载文件。

        参数:
        download_url (str): 下载地址。
        save_path (str): 保存路径。
        """
        # 设置请求头
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        # }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Referer": "https://www.bilibili.com"
        }

        try:
            response = requests.get(download_url, headers=headers, stream=True)
            if response.status_code == 200:
                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                content = "✅ 下载成功"
                self.realTimeLogService.append_log(content)
                self.writemessage(content)
                return 1
            else:
                content = f"❌ 下载失败，状态: {response.status_code}"
                self.realTimeLogService.append_log(content)
                self.writemessage(content)
                return 0
        except Exception as e:
            content = f"❌ 下载失败，错误: {e}"
            self.realTimeLogService.append_log(content)
            self.writemessage(content)
            return 0

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
    def get_latest_episode_id(self, bvid):

        """
        根据 合集BVID 获取最新集的 AID 和 CID。

        参数:
        bvid (str): BVID。

        返回:
        tuple: (AID, CID)。
        """

        url = self.apiinfourl + bvid
        # headers = {
        #     'Content-Type': 'application/json; charset=utf-8'
        # }
        try:
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
        except Exception as e:
            # content = f"❌ 获取最新集的 AID 和 CID，错误: {e}"
            code = 1
            result = []
            # print(result)
        return code, result


    def checkbvid(self, bvidlist):
        """
        检查 bvid.txt 文件中是否存在名为 某某bvid 的文件。返回未下载的bvid
        
        参数:
        bvidlist (list): 包含视频 BVID 的列表。
        
        返回:
        返回过滤后的 bvidlist，其中不包含已下载的 BVID。
        """
        # 取父亲目录，如/config/
        config_dir = os.path.dirname(self.configManager.config_path)
        # 路径拼接
        bvid_path = os.path.join(config_dir, "bvid.txt")

        # 检查文件是否存在，如果不存在则创建一个空文件
        if not os.path.exists(bvid_path):
            with open(bvid_path, 'w') as file:
                pass  # 创建空文件

        with open(bvid_path, 'r') as file:
            downloaded_bvids = set(file.read().strip().split(','))
            # downloaded_bvids = set(file.read().splitlines())
        
        return [bvid for bvid in bvidlist if bvid not in downloaded_bvids]

    # 纯追加
    def writebvid_one(self, bvidlist):
        # 取父亲目录，如/config/
        config_dir = os.path.dirname(self.configManager.config_path)
        # 路径拼接
        bvidpath = os.path.join(config_dir, "bvid.txt")
        with open(bvidpath, 'a') as file:
            if file.tell() != 0:  # Check if the file is not empty
                file.write(',')
            file.write(','.join(bvidlist))
    # 只追加那些未出现的 BVID
    def writebvid(self, bvidlist):
        # 取父亲目录，如/config/
        config_dir = os.path.dirname(self.configManager.config_path)
        # 路径拼接
        filename = os.path.join(config_dir, "bvid.txt")
        # 读取已存在的 BVID
        try:
            with open(filename, 'r') as file:
                existing_bvids = set(file.read().strip().split(','))
        except FileNotFoundError:
            existing_bvids = set()

        # 找出未出现的 BVID
        new_bvids = [bvid for bvid in bvidlist if bvid not in existing_bvids]

        # 如果有新的 BVID，追加到文件中
        if new_bvids:
            with open(filename, 'a') as file:
                if existing_bvids:
                    file.write(',')
                file.write(','.join(new_bvids))

    # 根据动态获取bvid，无需真实cookie
    def getdynamicbvid(self):

        dynamiclist = []
        bvidlist = []
        key = "uids"
        items = self.configManager.read_config(self.key)

        for item in items:
            # print(item['uid'])
            dynamiclist.append(item['uid'])
        # print(dynamiclist)

        # print("⚡️ 根据动态获取bvid")
        # print(cookie)
        content = "⚡️ 根据动态获取bvid"
        # print(content)
        self.realTimeLogService.append_log(content)
        for host_mid in dynamiclist:
            content = " 🆙 UP主：" + host_mid + " "
            # print(content)
            self.realTimeLogService.append_log(content)
            url = self.apidynamicurl + host_mid
            
            # print(url)
            # headers = {
            # 'Cookie' : cookie,
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            # }

            headers = {
                'Cookie' : "buvid3=x",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            # print(headers)

            try:
                # 发送请求
                response = requests.get(url, headers=headers)

                # 解析JSON响应
                data = response.json()
                # print(data)
                # data = json.loads(data)

                # 检查请求是否成功
                result = []
                if data['code'] == 0:
                    # 获取动态详情
                    # 提取bvid
                    # print(data)
                    # print("⚡️ 获取动态详情")
                    items = data['data']['items']
                    # 遍历items列表
                    # 只获取最近5条数据
                    items = items[:self.recentCount]
                    for item in items:
                        # print(item)
                        try:
                            # 检查每个层级是否为None
                            if (item.get('modules') and 
                                item['modules'].get('module_dynamic') and 
                                item['modules']['module_dynamic'].get('major') and 
                                item['modules']['module_dynamic']['major'].get('archive')):
                                bvid = item['modules']['module_dynamic']['major']['archive']['bvid']
                                content = f'✨ 添加新BVID：{bvid}'
                                # print(content)
                                self.realTimeLogService.append_log(content)
                                # 将bvid加入bvidlist中
                                bvidlist.append(bvid) 
                            else:
                                # print("🚧 未找到bvid")
                                pass

                            # bvid = item['modules']['module_dynamic']['major']['archive']['bvid']
                            # print(bvid)
                            # # print(f'✨ 添加新bvid: {bvid}')
                            # # 将bvid加入bvidlist中
                            # bvidlist.append(bvid) 
                        except KeyError:
                            # print("未找到bvid")
                            pass
                else:
                    content = f'🚨 根据动态获取bvid失败，错误代码: {data["code"]}'
                    # print(content)
                    self.realTimeLogService.append_log(content)
            except Exception as e:
                content = f'🚨 根据动态获取bvid失败，错误: {e}'
                # print(content)
                self.realTimeLogService.append_log(content)
            # time.sleep(10)
            wait_time = random.randint(10, 20)
            content = f"⏳️ 等待 {wait_time} 秒"
            # print(content)
            self.realTimeLogService.append_log(content)
            time.sleep(wait_time)
        
        return bvidlist



    def checkcid(self, cid):
        """
        检查 视频存放文件夹 中是否存在名为 时间_cid.mp4 的文件。
        
        参数:
        cid (str): 视频的 CID。
        
        返回:
        bool: 如果文件存在，则返回 True，否则返回 False。
        """
        # 遍历 视频存放文件夹 中的所有文件
        for filename in os.listdir(self.configManager.video_path):
            # 检查文件名是否符合 时间_cid.mp4 的格式
            if filename.endswith(f"_{cid}.mp4"):
                # print(f"🎊 文件已存在: {filename}")
                return True
        
        # print(f"🪄 文件不存在: *_{cid}.mp4，执行下载操作")
        return False


    def read_and_parse_json(self, file_path):
        try:
            # 打开文件并读取内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 解析JSON内容
            json_data = json.loads(content)
            
            return json_data
        except FileNotFoundError:
            # print(f"文件未找到: {file_path}")
            return None
        except json.JSONDecodeError:
            # print(f"文件内容不是有效的JSON: {file_path}")
            return None

    def logo(self):
        """
        打印logo
        """
        # # 打印MOKU的logo
        # logo_text = """
        # ██╗ ██╗      ██╗ ██████╗  
        # ██║ ██║      ██║ ██╔══██╗ 
        # ██║ ██║      ██║ ██████╔╝ 
        # ██║ ██║      ██║ ██╔══██╗ 
        # ██║ ███████╗ ██║ ██████╔╝ 
        # ╚═╝ ╚══════╝ ╚═╝ ╚═════╝  
        # """

        # logo_text = """
        # ██╗ ██╗                ██╗ ██████╗  
        # ██║ ██║                ██║ ██╔══██╗ 
        # ██║ ██║                ██║ ██████╔╝ 
        # ██║ ██║                ██║ ██╔══██╗ 
        # ██║ ███████╗    ██║ ██████╔╝ 
        # ╚═╝ ╚══════╝    ╚═╝ ╚═════╝  
        # """
        
        logo_text = "🚀 启动哔哩哨兵"
        # print(logo_text)
        content = logo_text
        self.writemessage(content)

    def writemessage(self, content):
        """
        写入推送消息
        
        参数:
        content (string): 每一行的内容
        """
        # global message
        # print(content)
        self.message += content


    # 下载视频定时任务
    def run_task_down(self, realTimeLogService, logService, cron_name):
        self.realTimeLogService = realTimeLogService
        self.logService = logService
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        content = f"😶‍🌫️ 开始运行 {cron_name}"
        self.realTimeLogService.append_log(content)
        """
        主函数
        """
        # self.logo()
        # test()
        
        bvidlist = self.getdynamicbvid()
        # 写入bvid到配置文件中
        bvidlist = self.checkbvid(bvidlist)    
        self.writebvid(bvidlist)
        # print(bvidlist)
        
        # 遍历bvidlist
        for bvid in bvidlist:
            content = "🎮️ 开始获取：" + bvid + ""
            self.realTimeLogService.append_log(content)
            self.writemessage(content)

            # code, result = get_latest_episode_id(bvid)
            code, result = self.getaidcid(bvid)
            # print(code)
            # print(result)
            # 等待几秒
            time.sleep(3)
            # 判断result数组长度是否为0
            if code == 0:
                if len(result) != 0:
                    # content = "✨ 总共检索到" + str(len(result)) + "个视频，开始处理"
                    # self.realTimeLogService.append_log(content)
                    # writemessage(content)
                    # 便利result数组
                    for item in result:
                        title = item['title']
                        aid = item['aid']
                        cid = item['cid']
                        ctime = item['ctime']
                        
                        # print(f"最新集AID: {aid}")
                        # content = f"🧸 集CID: {cid}"
                        content = f"🧸 标题：{title}"
                        # print(content)
                        self.realTimeLogService.append_log(content)
                        # writemessage(content)
                        # print(content)
                        # print(f"最新集时间: {ctime}")

                        # 检查是否已经下载过了
                        if self.checkcid(cid):
                            content = "🔮 已经下载过了"
                            # writemessage(content)
                            self.realTimeLogService.append_log(content)
                            # print(content)
                        else:
                            # 如果没下载则进行下载
                            code, downurl = self.getdownurl(aid, cid)
                            # 如果code==0则获取成功，否则尝试获取三次
                            if code == 0:
                                # content = f"🎯 下载地址: {downurl}"
                                # self.realTimeLogService.append_log(content)
                                time.sleep(3)
                                # 根据下载地址下载文件
                                name = title
                                # name = str(self.get_current_date_formatted()) + "_" + str(cid) # "今天时间 + cid"
                                path = self.configManager.video_path + name +  ".mp4"
                                content = f"💾 开始下载，保存路径：{path}"
                                self.realTimeLogService.append_log(content)
                                downflag = 0
                                downflag = self.download_file(downurl, path)
                                # 如果downflag 为1则下载成功，否则尝试下载三次
                                if downflag == 0:
                                    content = "❗ 下载失败，尝试下载三次"
                                    self.realTimeLogService.append_log(content)
                                    for i in range(int(self.downMaxCount)):
                                        content = f"❗ 尝试下载第{i+1}次"
                                        self.realTimeLogService.append_log(content)
                                        downflag = self.download_file(downurl, path)
                                        if downflag == 1:
                                            content = "✅ 下载成功"
                                            self.realTimeLogService.append_log(content)
                                            break
                                        # else:
                                        #     print("❌ 下载失败，尝试重新下载")
                                        #     time.sleep(3)

                                time.sleep(10)
                            else:
                                # content = "❌ 获取下载地址失败\n"
                                # writemessage(content)
                                content = f"❗ 获取下载地址失败，尝试获取{self.urlMaxCount}次"
                                self.realTimeLogService.append_log(content)
                                for i in range(int(self.urlMaxCount)):
                                    content = f"❗ 尝试获取下载地址第{i+1}次"
                                    self.realTimeLogService.append_log(content)
                                    code, downurl = self.getdownurl(aid, cid)
                                    if code == 0:
                                        # content = f"🎯 下载地址: {downurl}"
                                        # 根据下载地址下载文件
                                        name = title
                                        # name = str(AppFunctions.get_current_date_formatted()) + "_" + str(cid) # "今天时间 + cid"
                                        path = self.configManager.video_path + name +  ".mp4"
                                        content = f"💾 开始进行下载，保存路径: {path}"
                                        self.realTimeLogService.append_log(content)
                                        downflag = 0
                                        downflag = self.download_file(downurl, path)
                                        # 如果downflag 为1则下载成功，否则尝试下载三次
                                        if downflag == 0:
                                            content = f"❗ 尝试下载{self.downMaxCount}次"
                                            self.realTimeLogService.append_log(content)
                                            for i in range(int(self.downMaxCount)):
                                                content = f"❗ 尝试下载第{i+1}次"
                                                self.realTimeLogService.append_log(content)
                                                downflag = self.download_file(downurl, path)
                                                if downflag == 1:
                                                    content = "✅ 下载成功"
                                                    self.realTimeLogService.append_log(content)
                                                    break
                                                # else:
                                                #     print("❌ 下载失败，尝试重新下载")
                                                #     time.sleep(3)

                                        time.sleep(10)
                                        break
                                    else:
                                        # print("❌ 获取下载地址失败，尝试重新获取")
                                        time.sleep(3)

                else:
                    content = "🎈 无视频"
                    self.realTimeLogService.append_log(content)
                    self.writemessage(content)
            else:
                content = "❌ 获取失败"
                self.realTimeLogService.append_log(content)
                self.writemessage(content)
            time.sleep(10)
                
        # print(message)
        
        # print(message)
        # send_bark_message(message, key)

        self.logService.append_history(cron_name, start_time, "运行结束", "")
        content = "🎉 运行结束"
        self.realTimeLogService.append_log(content)