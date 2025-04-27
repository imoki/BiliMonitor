
class LogService():
    def __init__(self, **kwargs):
        pass
        # print(kwargs)
    # 读取指定配置
    def read_history(self, key):
        pass

    # 更新配置
    def update_history(self, key, value):
        pass

    # 追加历史记录，只保留最近15条记录
    def append_history(self, cron_name, start_time, state, notes):
        pass

    # 清空历史记录
    def clear_history(self):
       pass


    # 删除表格中的某行。
    def table_delete_selected_rows_history(self):
        pass