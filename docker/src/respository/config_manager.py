"""对config表进行操作"""

import os
import json

class ConfigManager():
    def __init__(self, **kwargs):
        self.config_path = kwargs.get('config_path', '') 
        self.video_path = kwargs.get('video_path', '')    # 视频保存路径
        self.version = "2.0"   # 专属于config配置的version，根据版本号进行针对性更新
        self.config_data = ""

    # 校验config配置的格式，更新为最新格式
    def check(self):
        # 检查是否有version字段
        with open(self.config_path, "r", encoding="utf-8") as config_file:
            self.config_data = json.load(config_file)

        # 1.0版本的配置文件处理
        if "version" not in self.config_data:
            self.config_data["version"] = "1.0"
        if self.config_data["version"] != self.version:
            # 更新config配置的格式
            print("⚡️ 更新config配置的格式")
            self.config_data["version"] = self.version

            # cookie字符传变成cookie数组
            if "cookie" in self.config_data:
                # 校验cookie的；类型
                # 如果是字符串则说明是1.0版本的配置文件，需要转换成数组
                # print(type(self.config_data["cookie"]))
                if isinstance(self.config_data["cookie"], str):
                    cookie_str = self.config_data["cookie"]
                    dict = {
                        "nickname" : "昵称1",
                        "cookie": cookie_str,
                        "notes": ""
                    }
                    self.config_data["cookie"] = [dict]
            
            # 保存更新后的配置文件
            with open(self.config_path, "w", encoding="utf-8") as config_file:
                json.dump(self.config_data, config_file, ensure_ascii=False, indent=4)
                
    # 加载配置
    def load_config(self):
        self.init_folder()
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)

                # 确保 uids 字段存在
                if "uids" not in config_data:
                    config_data["uids"] = []

                # 更新配置文件以确保 uids 字段存在
                with open(self.config_path, "w", encoding="utf-8") as config_file:
                    json.dump(config_data, config_file, ensure_ascii=False, indent=4)
        else:
            # 创建默认配置文件
            default_config = {
                "cookie": [],
                "uids": [],
                "version": self.version
            }
            with open(self.config_path, "w", encoding="utf-8") as config_file:
                json.dump(default_config, config_file, ensure_ascii=False, indent=4)
        
        # 配置检查并更新
        self.check()
    # 读取指定配置
    def read_config(self, key):
        config_data = ""
        if os.path.exists(self.config_path):
            # print(self.config_path)
            with open(self.config_path, "r", encoding="utf-8") as config_file:
                
                config_data = json.load(config_file)
                # print(config_data)
        # 如果没有指定key，则返回None
        if key not in config_data:
            return None
        return config_data[key]
    
    # 更新配置
    def update_config(self, key, value):
        # 读取现有配置文件，如果文件不存在则创建一个默认配置
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)
        else:
            config_data = {}

        # 更新配置中的指定字段
        config_data[key] = value

        # 保存更新后的配置文件
        with open(self.config_path, "w", encoding="utf-8") as config_file:
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

    

