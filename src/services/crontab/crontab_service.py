from ...views.prompt_view import PromptView
from ...views.table_view import TableView

class CrontabService():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '') 
        self.key = kwargs.get('key', '') # "crons"，同时作为信号量标识
        self.unique = kwargs.get('unique', '')
        self.table = kwargs.get('table', '') 
        self.configManager = kwargs.get('configManager', '')
        self.rowCount = 10
        self.prompt_view = PromptView(self.parent)
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
        column_order = ["name", "cron", "type", "nickname", "notes"]
        column_names = {
            "name": "任务名称",
            "cron": "定时时间",
            "type": "任务类型",
            "nickname":"账号",
            "notes": "备注",
        }

        # 设置表头
        header_labels = [column_names[col] for col in column_order if col in column_names]
        self.table.setHorizontalHeaderLabels(header_labels)

        for rowIndex, row in enumerate(data):
            for colIndex, column in enumerate(column_order):
                # print(column, row[column])
                if column in row:
                    value = row[column]
                    if column == "type":
                        # 根据 type 值设置显示文本
                        type_value = row[column]
                        if type_value == 0:
                            display_text = "下载视频"
                        elif type_value == 1:
                            display_text = "签到做任务"
                        else:
                            display_text = f"未知类型 ({type_value})"
                        
                        tableView.setItem(rowIndex + 1, colIndex, display_text)
                        # self.table.setItem(rowIndex + 1, colIndex, QTableWidgetItem(display_text))
                    else:
                        tableView.setItem(rowIndex + 1, colIndex, value)
                        # self.table.setItem(rowIndex + 1, colIndex, QTableWidgetItem(str(value)))
    # 下拉框不同值动态修改
    def handle_combox_signal(self, edits):
        # print("accept")
        # print(edits)
        signal_name = edits.get("name")
        if signal_name != self.key:
            return
        # print(self.key, " combox 接收成功")
        status = edits.get("status")
        if status == "cancel":
            self.prompt_view.prompt(text="编辑取消", type="warning")
        else:
            signal_value = edits.get("value")
            labels = signal_value.get("labels")


    # def set_table_customize_value(self, tableView, value):
    #     tableView.set_table_customize_value(value)

    # 表格创建
    def table_create(self):
        # 弹出框标题
        title = "添加定时任务"

        # 弹出框内容
        labels = [
            {
                'label': "任务名称",
                'value': "默认",
                'type': "QLineEdit",
            },
            {
                'label': "定时时间",
                'value': "09:00",
                'type': "QLineEdit",
            },
            {
                'label': "任务类型",
                'value': ["下载视频", "签到做任务"],
                'default': 0,
                'type': "QComboBox",
                'association': {
                    'id': 2,
                    'foregin_id':3
                },
            },
            {
                'label': "账号",
                'value': [""],
                'default': 0,
                'type': "QComboBox",
            },
            {
                'label': "备注",
                'value': "",
                'type': "QLineEdit",
            }
        ]

        # 添加动态读取的账号
        # 读取cookie配置
        key = "cookie"
        items = self.configManager.read_config("cookie")
        if items:
            nicknames = [item["nickname"] for item in items]
            nicknames.insert(0, "默认")
            labels[3]["value"] = nicknames 
        # else:
        #     labels[3]["value"] = ["全部"]

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
        # print("cron accept")
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
            name = signal_value.get("任务名称")
            cron = signal_value.get("定时时间")
            # cron_type = signal_value.get("任务类型")    # 是index
            cron_type_text = signal_value.get("任务类型")    # 是文本
            nickname = signal_value.get("账号")
            notes = signal_value.get("备注", "")

            # 数据输入校验
            # 去除空格和换行
            name = name.strip()
            if not name:
                self.prompt_view.prompt(text="任务名称不能为空", type="warning")
                return

            # 对定时时间进行格式化校验
            cron = self.format_cron(cron)
            if not cron:
                return

            cron_list = ["下载视频", "签到做任务"]
            cron_type = 0
            # 根据cron_text文本获取cron_type索引
            for i, cron_text_item in enumerate(cron_list):
                if cron_text_item == cron_type_text:
                    cron_type = i
                    break

            # 添加动态读取的账号
            # 读取cookie配置
            key = "cookie"
            items = self.configManager.read_config("cookie")

            dict_data = {
                "name": name,
                "cron": cron,
                "type": cron_type,
                "nickname": nickname,
                "notes": notes,
            }

            # 读取配置文件中的数据
            content = self.configManager.read_config(self.key)
            if content:
                for item in content:
                    if item[self.unique] == name:
                        self.prompt_view.prompt(text=f"{name} 已存在", type="warning")
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

    # 表编辑
    def table_edit(self):
        # row = self.parent.ui.tableWidget_cron.currentRow()

        # item_1 = self.parent.ui.tableWidget_cron.item(row, 0)
        # item_2 = self.parent.ui.tableWidget_cron.item(row, 1)
        # item_3 = self.parent.ui.tableWidget_cron.item(row, 2)
        # item_5 = self.parent.ui.tableWidget_cron.item(row, 4)

        # 当前选中的行
        row = self.table.currentRow()
        # 行内数据
        item_1 = self.table.item(row, 0)
        item_2 = self.table.item(row, 1)
        item_3 = self.table.item(row, 2)
        item_4 = self.table.item(row, 3)
        item_5 = self.table.item(row, 4)

        # 如果前两个数据没有则判定为空行，不执行编辑操作
        if not item_1 or not item_2:
            self.prompt_view.prompt(text="无法编辑此行", type="warning")
            return

        # 空行校验通过后，读取行内数据
        item_text_1 = item_1.text()
        item_text_2 = item_2.text()
        item_text_3 = item_3.text()
        item_text_4 = item_4.text() if item_4 else ""   # 可能为空，因此需要判断
        item_text_5 = item_5.text() if item_5 else ""

        # 特殊值特殊获取
        # combox默认值
        combox_list = ["下载视频", "签到做任务"]
        item_combox_index_3 = 0
        # 根据cron_text文本获取cron_type索引
        for i, combox_text_item in enumerate(combox_list):
            if combox_text_item == item_text_3:
                item_combox_index_3 = i
                break

        # 添加动态读取的账号
        # 读取cookie配置
        item_combox_index_4 = 0
        if item_text_4 != "默认":
            key = "cookie"
            items = self.configManager.read_config("cookie")
            # print(items)
            for index, item in enumerate(items):
                if item["nickname"] == item_text_4:
                    item_combox_index_4 = index + 1
                    # print("找到", str(item_combox_index_4))
                    # print(item_text_4)
                    break
        else:
            item_combox_index_4 = 0
        # print(item_text_4)
        # print(item_combox_index_4)

        # 弹出编辑框基础配置
        # 弹出框标题
        title = "编辑定时任务"
        # 弹出框内容
        labels = [
            {
                'label': "任务名称",
                'value': item_text_1,
                'type': "QLineEdit",
            },
            {
                'label': "定时时间",
                'value': item_text_2,
                'type': "QLineEdit",
            },
            {
                'label': "任务类型",
                'value': ["下载视频", "签到做任务"],
                'default': item_combox_index_3,
                'type': "QComboBox",
            },
            {
                'label': "账号",
                'value': [""],
                'default': item_combox_index_4,
                'type': "QComboBox",
            },
            {
                'label': "备注",
                'value': item_text_5,
                'type': "QLineEdit",
            }
        ]

        # 添加动态读取的账号
        # 读取cookie配置
        key = "cookie"
        items = self.configManager.read_config("cookie")
        if items:
            nicknames = [item["nickname"] for item in items]
            nicknames.insert(0, "默认")
            labels[3]["value"] = nicknames 

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
        signal_name = edits.get("name")
        if signal_name != self.key:
            return

        status = edits.get("status")
        if status == "cancel":
            self.prompt_view.prompt(text="编辑取消", type="warning")
        else:
            row = edits.get("edit_row")
            signal_value = edits.get("value")
            item_text_1 = signal_value.get("任务名称")
            item_text_2 = signal_value.get("定时时间")
            item_text_3 = signal_value.get("任务类型")    # 是文本
            item_text_4 = signal_value.get("账号")
            item_text_5 = signal_value.get("备注", "")

            # 对定时时间进行格式化校验
            item_text_2 = self.format_cron(item_text_2)
            if not item_text_2:
                return

            # 读取配置文件数据
            items = self.configManager.read_config(self.key)
            # 除当前行外，校验是否存在其它同名数据 
            index = row - 1 # 表格行索引转配置索引，配置索引比表格行所以小1
            for i in range(0, len(items)):
                if i != index and items[i][self.unique] == item_text_1:
                    self.prompt_view.prompt(text=f"{item_text_1} 已存在", type="warning")
                    return

            # combox内容
            combox_list = ["下载视频", "签到做任务"]
            item_combox_index_3 = 0
            # 根据cron_text文本获取cron_type索引
            for i, combox_text_item in enumerate(combox_list):
                if combox_text_item == item_text_3:
                    item_combox_index_3 = i
                    break

            # 更新某一行表格中的数据
            # self.parent.ui.tableWidget_cron.setItem(row, 0, QTableWidgetItem(item_text_1))
            # self.parent.ui.tableWidget_cron.setItem(row, 1, QTableWidgetItem(item_text_2))
            # self.parent.ui.tableWidget_cron.setItem(row, 2, QTableWidgetItem(item_text_combox_3))
            # self.parent.ui.tableWidget_cron.setItem(row, 4, QTableWidgetItem(item_text_5))

            tableView = TableView(parent = self.parent, table = self.table)
            tableView.setItem(row, 0, item_text_1)
            tableView.setItem(row, 1, item_text_2)
            tableView.setItem(row, 2, item_text_3)
            tableView.setItem(row, 3, item_text_4)
            tableView.setItem(row, 4, item_text_5)

            # 更新配置文件中的数据
            if items:
                if 0 <= index < len(items):
                    items[index]["name"] = item_text_1
                    items[index]["cron"] = item_text_2
                    items[index]["type"] = item_combox_index_3
                    items[index]["nickname"] = item_text_4
                    items[index]["notes"] = item_text_5

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

    def format_cron(self, cron):
        # 对定时时间进行格式化校验
        # 定时为空
        if not cron:
            self.prompt_view.prompt(text="请填写定时时间", type="warning")
            return None
        
        # 修改格式相关
        # 去除空格
        cron = cron.replace(" ", "")
        # 中间的：为英文
        cron = cron.replace("：", ":")

        # 规范格式相关
        # 需要为 x:x格式，时在0-23之间，分在0-59之间
        # x:x格式，前后都不为空
        if len(cron.split(":")) != 2:
            self.prompt_view.prompt(text="定时时间格式错误", type="warning")
            return None
        if not cron.split(":")[0] or int(cron.split(":")[0])<0 or int(cron.split(":")[0])>23:
            self.prompt_view.prompt(text="定时时间小时错误", type="warning")
            return None
        if not cron.split(":")[1] or int(cron.split(":")[1])<0 or int(cron.split(":")[1])>59:
            self.prompt_view.prompt(text="定时时间分钟错误", type="warning")
            return None
        
        # 如果时为24:x则变为0:x，分为x:60则变为x:0
        if int(cron.split(":")[0]) == 24:
            cron = "00:" + cron.split(":")[1]
        if int(cron.split(":")[1]) == 60:
            cron = cron.split(":")[0] + ":00"

        # x:x格式，变为0x:0x
        if len(cron.split(":")[0]) == 1:
            cron = "0" + cron.split(":")[0] + ":" + cron.split(":")[1]
        if len(cron.split(":")[1]) == 1:
            cron = cron.split(":")[0] + ":0" + cron.split(":")[1]

        return cron


    # 根据任务名获取任务字典（已废弃）
    def get_cron_by_name(self, crons, cron_name):
        for cron in crons:
            if cron["name"] == cron_name:
                return cron