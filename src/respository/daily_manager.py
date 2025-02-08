"""对config表进行操作"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QCheckBox, QComboBox, QLineEdit

from ..views.prompt_view import PromptView
import os
import json
import json5
import copy

class DailyManager():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '') 
        self.configManager = kwargs.get('configManager', '')
        self.prompt_view = PromptView(self.parent)
        # cookies.json
        self.daily_cookie_path = kwargs.get('daily_cookie_path', '') 
        self.daily_appsettings_path = kwargs.get('daily_appsettings_path', '')
        self.key_bili = 'BiliBiliCookies'

        self.default_config_DailyTaskConfig = {
            "DailyTaskConfig": {
                "Cron": "0 15 * * *",
                "IsWatchVideo": True,
                "IsShareVideo": True,
                "IsDonateCoinForArticle": False,
                "NumberOfCoins": 5, 
                "NumberOfProtectedCoins": 0,
                "SaveCoinsWhenLv6": False,
                "SelectLike": True,
                "SupportUpIds": "",
                "DayOfAutoCharge": -1,
                "AutoChargeUpId": "-1",
                "ChargeComment": "",
                "DayOfReceiveVipPrivilege": 1,
                "DayOfExchangeSilver2Coin": -1,
                "DevicePlatform": "android",
                "CustomComicId": 27355,
                "CustomEpId": 381662
            }
        }
        self.key_DailyTaskConfig = 'DailyTaskConfig'
        # self.modify_config = self.default_config_DailyTaskConfig # 存储修改后的配置，存在浅拷贝问题
        self.modify_config = copy.deepcopy(self.default_config_DailyTaskConfig)   # 深拷贝，递归地复制字典及其所有嵌套的对象，确保两个字典完全独立。

    # 加载配置， 设置默认值
    def load_settings(self):
        # 读取配置文件
        with open(self.daily_appsettings_path, 'r', encoding='utf-8') as file:
            config_data = json5.load(file)

        self.ui_show(config_data)
    
    # 设置复选框默认选项
    def set_default_checkbox_values(self, checkbox, default_value):
        checkbox.setChecked(default_value)
    # 设置下拉框默认选项
    def set_default_combox_values(self, combox, options, default_value):
        # 确保传入的option内元素是字符串
        options = [str(i) for i in options]
        # 清空下拉框并添加所有选项
        combox.clear()
        combox.addItems(options)
        # 设置下拉框的默认值
        index = combox.findText(str(default_value), Qt.MatchFixedString)
        # print(index)
        if index >= 0:
            combox.setCurrentIndex(index)
    
    # 设置输入框默认值
    def set_default_lineEdit_values(self, lineEdit, lineEdit_default_value):
        lineEdit.setText(str(lineEdit_default_value))
    
    # 设置显示的默认值
    def ui_show(self, config_data):
        # DailyTaskConfig
        DailyTaskConfig = config_data[self.key_DailyTaskConfig]
        # 设置复选框的默认值
        ui = self.parent.ui
        checkBox = [   
            ui.checkBox_setting_DailyTaskConfig_IsWatchVideo, 
            ui.checkBox_setting_DailyTaskConfig_IsShareVideo, 
            ui.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle,
            ui.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6,
            ui.checkBox_setting_DailyTaskConfig_SelectLike
        ]
        checkBox_default_value = [
            DailyTaskConfig['IsWatchVideo'],
            DailyTaskConfig['IsShareVideo'],
            DailyTaskConfig['IsDonateCoinForArticle'],
            DailyTaskConfig['SaveCoinsWhenLv6'],
            DailyTaskConfig['SelectLike']
        ]
        for checkbox, default_value in zip(checkBox, checkBox_default_value):
            self.set_default_checkbox_values(checkbox, default_value)

        # 设置下拉框的默认值
        combox = [
            ui.comboBox_setting_DailyTaskConfig_NumberOfCoins,
            ui.comboBox_setting_DailyTaskConfig_DayOfAutoCharge,
            ui.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege,
            ui.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin,
            ui.comboBox_setting_DailyTaskConfig_DevicePlatform
        ]
        combox_default_value = [
            DailyTaskConfig['NumberOfCoins'],
            DailyTaskConfig['DayOfAutoCharge'],
            DailyTaskConfig['DayOfReceiveVipPrivilege'],
            DailyTaskConfig['DayOfExchangeSilver2Coin'],
            DailyTaskConfig['DevicePlatform']
        ]
        options = [
            list(range(1, 6)),  # 1-5 的列表 [0, 5]
            list(range(-1, 32)),
            list(range(-1, 32)),
            list(range(-1, 32)),
            ["ios","android"]
        ]
        
        for combox, options, combox_default_value in zip(combox, options, combox_default_value):
            self.set_default_combox_values(combox, options, combox_default_value)
        

        # 设置输入框的默认值
        lineEdit = [
            ui.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins,
            ui.lineEdit_setting_DailyTaskConfig_SupportUpIds,
            ui.lineEdit_setting_DailyTaskConfig_AutoChargeUpId,
            ui.lineEdit_setting_DailyTaskConfig_ChargeComment,
            ui.lineEdit_setting_DailyTaskConfig_CustomComicId,
            ui.lineEdit_setting_DailyTaskConfig_CustomEpId,
        ]
        lineEdit_default_value = [
            DailyTaskConfig['NumberOfProtectedCoins'],
            DailyTaskConfig['SupportUpIds'],
            DailyTaskConfig['AutoChargeUpId'],
            DailyTaskConfig['ChargeComment'],
            DailyTaskConfig['CustomComicId'],
            DailyTaskConfig['CustomEpId'],
        ]

        for lineEdit, lineEdit_default_value in zip(lineEdit, lineEdit_default_value):
            self.set_default_lineEdit_values(lineEdit, lineEdit_default_value)
        
    # 改变每日任务配置
    def modify_settings(self):
        # 保留注释方法
        # 读取 appsettings.json 文件
        with open(self.daily_appsettings_path, 'r', encoding='utf-8') as file:
            config_data = json5.load(file)
        
        # 修改 DailyTaskConfig 中的值
        if self.key_DailyTaskConfig in config_data:
            config_data[self.key_DailyTaskConfig].update(self.modify_config[self.key_DailyTaskConfig])
        else:
            config_data[self.key_DailyTaskConfig] = self.modify_config[self.key_DailyTaskConfig]

        # print(config_data)
        # 写回 appsettings.json 文件
        # ensure_ascii=False 以确保中文字符不被转义
        with open(self.daily_appsettings_path, 'w', encoding='utf-8') as file:
            # json5.dump(config_data, file, indent=4, ensure_ascii=False)
            json.dump(config_data, file, indent=4, ensure_ascii=False)

        self.prompt_view.prompt(text="配置修改成功", type="success")

        # keys = kwargs.get('keys', '')
        # # 不断读取字典值
        # if keys is not None:
        #     for key in keys:
        #         if key in self.DailyTaskConfig:
        #             self.DailyTaskConfig = self.DailyTaskConfig[key]
        #         else:
        #             self.DailyTaskConfig = None
        #             break
    
    # 重置默认配置
    def reset_default_config(self):
        # 保留注释方法
        # 读取 appsettings.json 文件
        with open(self.daily_appsettings_path, 'r', encoding='utf-8') as file:
            config_data = json5.load(file)
        
        # 修改 DailyTaskConfig 中的值
        if self.key_DailyTaskConfig in config_data:
            config_data[self.key_DailyTaskConfig].update(self.default_config_DailyTaskConfig[self.key_DailyTaskConfig])
        else:
            config_data[self.key_DailyTaskConfig] = self.default_config_DailyTaskConfig[self.key_DailyTaskConfig]

        # print(self.default_config_DailyTaskConfig[self.key_DailyTaskConfig])
        # 写回 appsettings.json 文件
        # ensure_ascii=False 以确保中文字符不被转义
        with open(self.daily_appsettings_path, 'w', encoding='utf-8') as file:
            # json5.dump(config_data, file, indent=4, ensure_ascii=False)
            json.dump(config_data, file, indent=4, ensure_ascii=False)

        # 显示配置
        self.ui_show(config_data)
        self.prompt_view.prompt(text="已恢复为默认配置", type="success")
        

    # 获取嵌套键路径的值，转为list
    def get_nested_value(self, key_path):
        keys = key_path.split('.')
        return keys
    
    # 格式转换
    def format_config(self, key, value):
        if key in ["NumberOfCoins", "NumberOfProtectedCoins","DayOfAutoCharge",
                     "DayOfReceiveVipPrivilege","DayOfExchangeSilver2Coin",
                    "CustomComicId", "CustomEpId"]:
            # 若传入value为空，直接返回
            if not value:
                return value
            value = int(value)
        return value
    # 根据传入的键名称设置
    def setting(self, keys, item):
        # 加载配置时默认也会执行。

        # 按照点分隔
        # DailyTaskConfig.IsWatchVideo
        keys = self.get_nested_value(keys)
        if len(keys) <= 1:
            pass
        else:
            # 判断类型
            if isinstance(item, QCheckBox):
                # 传入的是复选框
                value = item.isChecked()
            elif isinstance(item, QComboBox):
                # 传入的是combox
                value = item.currentText().strip()
            elif isinstance(item, QLineEdit):
                value = item.text().strip()

            # 主键.次键。如：DailyTaskConfig.IsWatchVideo
            key_1, key_2 = keys
            # self.modify_config[key_1] = {key_2: value}
            # 不断追加字典内容
            value = self.format_config(key_2, value)
            try:
                self.modify_config[key_1][key_2] = value
            except KeyError:
                self.modify_config[key_1] = {key_2: value}
            
            # self.print_modify_config()

    # 打印修改后的配置键值对
    def print_modify_config(self):
        print(self.modify_config)

    # 格式化cookie
    def format_cookie(self, cookie):
        # 格式化cookie，清除value前后空格和换行
        cookie = re.sub(r'[\s\n]', '', cookie)
        return cookie

    # 根据cron中的nickname，动态修改cookies.json文件中BiliBiliCookies配置
    def modify_cookies(self, nickname):
        # 读取 cookies.json 文件，如果文件不存在则创建一个空的 JSON 对象
        cookies_data = self.read_config(self.daily_cookie_path, self.key_bili)
        
        # 根据nickname判断读取哪些内容
        # 如果nickename是默认或空，则读取 config.json 中的所有 cookie 值
        value = []
        if nickname == "默认" or nickname == "":
            value = [cookie["cookie"] for cookie in self.configManager.read_config("cookie")]
        else:
            # 根据 nickname 读取对应的 cookie 值
            items = self.configManager.read_config("cookie")
            if items:
                for item in items:
                    if item["nickname"] == nickname:
                        value = [item["cookie"]]
                        break

        self.update_config(self.daily_cookie_path, self.key_bili, value)
   
    # 读取指定配置
    def read_config(self, path, key):
        config_data = {}
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)
        # 如果没有指定key，则返回None
        if key not in config_data:
            # return None
            # 若键不存在，则创建键
            config_data[key] = []
        return config_data[key]
    
    # 更新配置
    def update_config(self, path, key, value):
        # 读取现有配置文件，如果文件不存在则创建一个默认配置
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)
        else:
            config_data = {}

        # 更新配置中的指定字段
        config_data[key] = value

        # 保存更新后的配置文件
        with open(path, "w", encoding="utf-8") as config_file:
            json.dump(config_data, config_file, ensure_ascii=False, indent=4)

        # print(f"{key} : {value}")

    # 检测文件夹是否存在，文件夹不存在则创建文件夹，递归创建
    def init_folder(self):
        """
        创建文件夹
        """
        if not os.path.exists(self.video_path):
            os.makedirs(self.video_path)
        # 检查并创建 config_path 的路径，创建目录
        config_dir = os.path.dirname(self.config_path)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

    

