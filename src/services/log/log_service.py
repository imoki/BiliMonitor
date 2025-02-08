from .. import json, os, datetime
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialogButtonBox, QTableWidgetItem
from ...views.prompt_view import PromptView

class LogService():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '') 
        self.key = kwargs.get('key', '') 
        self.unique = kwargs.get('unique', '')
        self.table = kwargs.get('table', '') 
        self.log_path = kwargs.get('log_path', '') 
        self.configManager = kwargs.get('configManager', '')
        self.rowCount = 10
        self.prompt_view = PromptView(self.parent)
        # print(kwargs)
    # 
    def load_table(self):
        data = self.read_history(self.key)
        # print(data)
        if not data:
            return
        # 表格处理
        if len(data) + 1 < self.rowCount:
            self.table.setRowCount(self.rowCount)
        else:
            self.table.setRowCount(len(data) + 1)
        

        # 定义列的顺序和对应的键名
        column_order = ["start_time", "end_time", "name", "state", "notes"]
        column_names = {
            "start_time": "开始时间",
            "end_time": "结束时间",
            "name": "任务名称",
            "state": "状态",
            "notes": "备注",
        }

        # 设置表头
        header_labels = [column_names[col] for col in column_order if col in column_names]
        self.table.setHorizontalHeaderLabels(header_labels)

        for rowIndex, row in enumerate(data):
            for colIndex, column in enumerate(column_order):
                try:
                    # print(column, row[column])
                    if column in row:
                        value = row[column]
                        self.table.setItem(rowIndex + 1, colIndex, QTableWidgetItem(str(value)))
                except:
                    pass
    # 读取指定配置
    def read_history(self, key):
        if os.path.exists(self.log_path):
            with open(self.log_path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)
        # 如果没有指定key，则返回None
            if key not in config_data:
                return None
            return config_data[key]
        else:
            # 创建默认配置文件
            config_data = {
                key: [],
            }
            with open(self.log_path, "w", encoding="utf-8") as config_file:
                json.dump(config_data, config_file, ensure_ascii=False, indent=4)
            return config_data[key]

    # 更新配置
    def update_history(self, key, value):
        # 读取现有配置文件，如果文件不存在则创建一个默认配置
        if os.path.exists(self.log_path):
            with open(self.log_path, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)
        else:
            config_data = {}

        # 更新配置中的指定字段
        config_data[key] = value

        # 保存更新后的配置文件
        with open(self.log_path, "w", encoding="utf-8") as config_file:
            json.dump(config_data, config_file, ensure_ascii=False, indent=4)

    # 追加历史记录，只保留最近15条记录
    def append_history(self, cron_name, start_time, state, notes):
        items = self.read_history(self.key)
        
        dict = {
            "start_time": start_time,
            "end_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": cron_name,
            "state": state,
            "notes": notes,
        }
        # print(dict)
        items.append(dict)
        # 只保留最近15条记录
        if len(items) > 15:
            items.pop(0)
        self.update_history(self.key, items)

    # 清空历史记录
    def clear_history(self):
        # 创建一个新的字典，只包含空的 history 列表
        new_history = {
            "history": []
        }

        # 将新的字典写回到 history.json 文件
        with open(self.log_path, "w", encoding="utf-8") as config_file:
            json.dump(new_history, config_file, ensure_ascii=False, indent=4)


        # # 清空表格中所有行
        # if isinstance(self.ui.tableWidget_history, QTableWidget):
        #     self.ui.tableWidget_history.clearContents()
        #     self.ui.tableWidget_history.setRowCount(0)

        # 清空除第一行（作为表头行）外的所有行
        if isinstance(self.parent.ui.tableWidget_history, QTableWidget):
            self.rowCount = self.parent.ui.tableWidget_history.self.rowCount()
            # print(self.rowCount)
            for row in range(1, self.rowCount):
                self.parent.ui.tableWidget_history.removeRow(row)
        
        self.prompt_view.prompt(text="清空历史记录成功", type="success")


    # 删除表格中的某行。
    def table_delete_selected_rows_history(self):
        """
        删除表格中的某行。
        :param table: 表格对象
        :param key: 配置文件中的key
        :param unique: 比较的key
        
        """
        # for i in self.ui.tableWidget_list.selectedItems():
        #     print(f"获取到了第{i.row()}行，第{i.column()}列，元素为{i.text()}")
        
        row = self.table.currentRow()
        if row == 0:
            return
        if row == 0:
            return
        # 获取当前行的数据
        item = self.table.item(row, 0)
        # if not item:
        #     self.show_success_message(text="无法删除此行", type="warning")
        #     return

        if not item:
            self.prompt_view.prompt(text="无法删除此行", type="warning")
            return
        else:
            itemtext = item.text()
            # print(itemtext)

            # 删除表格中的行
            self.table.removeRow(row)

            # 更新配置文件中的数据
            content = self.read_history(self.key)
            # print(content)
            if content:
                # try:
                content = [item for item in content if item[self.unique] != itemtext]
                # print(content)
                self.update_history(self.key, content)
                # except:
                #     return

            self.prompt_view.prompt(text="删除成功", type="success")