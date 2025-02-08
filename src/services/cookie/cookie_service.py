from ...views.prompt_view import PromptView
from ...views.table_view import TableView

class CookieService():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '') 
        self.key = kwargs.get('key', '') # 配置中的key，根据这个读取，同时作为信号量的对比值，"crons"
        self.unique = kwargs.get('unique', '')    # 唯一性校验，用于判断表格是否存在同名行，"nickname"
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
        column_order = ["nickname", "cookie", "notes"]
        column_names = {
            "nickname": "昵称",
            "cookie": "cookie",
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
                    # self.table.setItem(rowIndex + 1, colIndex, QTableWidgetItem(str(value)))
                    tableView.setItem(rowIndex + 1, colIndex, value)

    # 表格创建
    def table_create(self):
        # 弹出框标题
        title = "添加cookie"
        # 弹出框内容
        labels = [
            {
                'label': "昵称",
                'value': "昵称1",
                'type': "QLineEdit",
            },
            {
                'label': "cookie",
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
            nickname = signal_value.get("昵称")
            cookie = signal_value.get("cookie")
            notes = signal_value.get("备注", "")

            # 数据输入校验
            # 去除空格和换行
            nickname = nickname.strip()
            if not nickname:
                self.prompt_view.prompt(text="昵称不能为空", type="warning")
                return

            dict_data = {
                "nickname": nickname,
                "cookie": cookie,
                "notes": notes,
            }

            # 读取配置文件中的数据
            content = self.configManager.read_config(self.key)
            if content:
                for item in content:
                    if item[self.unique] == nickname:
                        self.prompt_view.prompt(text=f"{nickname} 已存在", type="warning")
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
        title = "编辑COOKIE"
        # 弹出框内容
        labels = [
            {
                'label': "昵称",
                'value': item_1,
                'type': "QLineEdit",
            },
            {
                'label': "cookie",
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
            item_text_1 = signal_value.get("昵称")
            item_text_2 = signal_value.get("cookie")
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
        :param unique: 比较的key，唯一
        
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