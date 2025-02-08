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

# 线程运行定时任务
class DynamicThread(QThread):
    signal = Signal(str)

    def __init__(self, **kwargs):
        super().__init__()
        self.parent = kwargs.get('parent', '')
        self.cron_name = kwargs.get('cron_name', '')
        self.dynamicService = kwargs.get('dynamicService', '')
        self.logService = kwargs.get('logService', '')
        self.realTimeLogService = RealTimeLogService(parent = self.parent,)

    def run(self):
        try:
            # with QMutexLocker(self.parent.mutex):
                # self.parent.mutex.lock()
            self.realTimeLogService.clear_log()
            self.realTimeLogService.show_default_log()
            # 执行主要任务
            self.dynamicService.run_task_down(realTimeLogService = self.realTimeLogService, logService =  self.logService, cron_name = self.cron_name)
            # print(self.cron_name)
            # # 模拟线程执行
            # time.sleep(3)
            content = "🎉 任务完成"
            self.signal.emit(content)
        except Exception as e:
            # print(f"TaskThread error: {e}")
            # self.signal.emit(f"任务失败: {e}")
            import traceback
            print(f"TaskThread error: {e}")
            print(traceback.format_exc())
            self.signal.emit(f"任务失败: {e}")
        finally:
            # self.parent.mutex.unlock()
            self.quit()