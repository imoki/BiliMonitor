import time

class RealTimeLogService():
    def __init__(self, **kwargs):
        pass

    # 清空日志
    def clear_log(self):
        # print("running clear_log...")
        pass

            # 显示日志
    def show_log(self, text):
        pass
    
    # 追加日志
    def append_log(self, text):
        # print("running append_log...")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(current_time)
        text = f"[{current_time}] {text}"
        print(text)


    # 打印默认消息
    def show_default_log(self):
        # print("running show_default_message...")
        # 当前时间
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        text = f"[{current_time}] 👻 开始运行"
        print(text)



