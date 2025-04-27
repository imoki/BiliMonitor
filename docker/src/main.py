from respository.config_manager import ConfigManager
from services.dynamic.dynamic_service import DynamicService
from services.log.log_service import LogService
from services.log.real_time_log_service import RealTimeLogService

class bili():
    def __init__(self):
        # 配置参数
        # config_path = ".\\src\\config\\config.json"
        # video_path = ".\\src\\video\\"    # 视频保存路径
        config_path = "/app/src/config/config.json"
        video_path = "/app/src/video/"
        
        # 动态页配置，获取最新动态视频相关
        dynamicKey = "uids" # 数据存放key，用于获取全部数据
        dynamicUnique = "uid" # 主键，唯一值，用于保证表内数据唯一性

        # 服务初始化
        self.cron_name = "dynamic"
        self.configManager = ConfigManager(parent = self, config_path = config_path, video_path = video_path)
        self.dynamicService = DynamicService(parent = self, key = dynamicKey, unique = dynamicUnique, configManager = self.configManager)
        self.realTimeLogService = RealTimeLogService(parent = self)
        self.logService = LogService(parent = self)
        # 加载配置文件
        self.configManager.load_config()

    def run(self):
        # print("开始运行")
        self.dynamicService.run_task_down(realTimeLogService = self.realTimeLogService, logService =  self.logService, cron_name = self.cron_name)
        # print(self.cron_name)


if __name__ == "__main__":

    app = bili()
    app.run()
