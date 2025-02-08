
from ..log.real_time_log_service import RealTimeLogService
from PySide6.QtCore import QThread, Signal
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

# 接收命令行窗口的输出
class DailyThread(QThread):
    signal = Signal(str)

    def __init__(self, **kwargs):
        super().__init__()
        self.parent = kwargs.get('parent', '')
        self.command = kwargs.get('command', '')
        # self.cron_name = kwargs.get('cron_name', '')
        self.cron = kwargs.get('cron', '')
        self.cron_name = self.cron["name"]
        self.logService = kwargs.get('logService', '')
        self.realTimeLogService = RealTimeLogService(parent = self.parent,)

        # 配置文件路径
        self.dailyManager = kwargs.get('dailyManager', '')

    # def run(self):
    #     # 测试
    #     start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     self.realTimeLogService.clear_log()
    #     self.realTimeLogService.show_default_log()

    #     # 根据传入的账户动态修改配置文件，以便支持多账号
    #     try:
    #         nickname = self.cron["nickname"]
    #     except:
    #         # 如果nickname为空则执行默认选项
    #         nickname = "默认"
    #     self.dailyManager.modify_cookies(nickname)

    #     content = "🍻 执行每日任务"
    #     print(content)
    #     self.realTimeLogService.append_log(content)

    #     content = f"😶‍🌫️ 开始运行 {self.cron_name}"
    #     self.realTimeLogService.append_log(content)

    def run(self):
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.realTimeLogService.clear_log()
        self.realTimeLogService.show_default_log()

        # 根据传入的账户动态修改配置文件
        self.dailyManager.modify_cookies(self.cron["nickname"])

        content = "🍻 执行每日任务"
        print(content)
        self.realTimeLogService.append_log(content)

        content = f"😶‍🌫️ 开始运行 {self.cron_name}"
        self.realTimeLogService.append_log(content)

        try:
            process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            
            # # 禁用缓存
            # process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True, bufsize=1)
            
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())
                    content = output.strip()
                    self.realTimeLogService.append_log(content)
                    # self.signal.emit(output.strip())

            #  # 处理标准错误输出
            # while True:
            #     error_output = process.stderr.readline()
            #     if error_output == '' and process.poll() is not None:
            #         break
            #     if error_output:
            #         self.signal.emit(error_output.strip())
            #         content = error_output.strip()
            #         AppFunctions.append_log(self.parent, content)
            

            rc = process.poll()
            # return rc
            
            if rc == 0:
                # self.signal.emit("任务完成")
                # self.signal.emit("任务结束")
                self.logService.append_history(self.cron_name, start_time, "任务完成", "")
                content = "🎉 运行结束"
                self.realTimeLogService.append_log(content)
            else:
                self.signal.emit(f"任务失败，退出码: {rc}")
                # self.signal.emit("任务结束")
                self.logService.append_history(self.cron_name, start_time, "任务失败", "")
                content = "❌ 任务失败"
                self.realTimeLogService.append_log(content)
        except Exception as e:
            self.signal.emit(f"Error running command: {e}")
        