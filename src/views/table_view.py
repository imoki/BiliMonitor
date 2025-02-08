from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QMessageBox, QComboBox, QTableWidgetItem
from PySide6.QtCore import Qt
import re
from .prompt_view import PromptView
from PySide6.QtCore import Signal, QObject

class TableView(QObject):
    # dialog_accepted_cron = Signal(dict)  # 信号，传递编辑内容
    # dialog_accepted_cookie = Signal(dict)
    table_dialog_accepted = Signal(dict)
    # table_combox_signal = Signal(dict)

    def __init__(self, **kwargs):
        super().__init__()
        self.parent = kwargs.get('parent', '')
        self.table = kwargs.get('table', '')

        # 表格内容
        self.table_dict = kwargs.get('table_dict', '')  # 含有key标识signal类型，labels记录数据
        if self.table_dict != '':
            self.key = self.table_dict["key"]
            self.title = self.table_dict["title"]
            self.labels = self.table_dict["labels"]

        # 表格编辑指定行
        self.edit_row = kwargs.get('edit_row', -1)

        self.prompt_view = PromptView(self.parent)
        self.dialog = None
        self.edits = None 

    # 加载配置表格
    def setItem(self, rowIndex, colIndex, value):
        self.table.setItem(rowIndex, colIndex, QTableWidgetItem(str(value)))

    # 创建弹出编辑框，弹出编辑框预处理、渲染处理
    def create_dialog(self):
        dialog = QDialog(self.parent)
        dialog.setWindowTitle(self.title)
        dialog_layout = QVBoxLayout()

        edits = []
        labels = self.labels
        for item in labels:
            item_type = item["type"]
            item_label = item["label"]
            item_value = item["value"]

            label = QLabel(item_label)
            dialog_layout.addWidget(label)
            if item_type == "QLineEdit":
                edit = QLineEdit(item_value)
                dialog_layout.addWidget(edit)
                edits.append(edit)
            elif item_type == "QComboBox":
                combo = QComboBox()
                for combo_value in item_value:
                    combo.addItem(combo_value)
                # 设置默认值
                combo.setCurrentIndex(item["default"])
                dialog_layout.addWidget(combo)
                edits.append(combo)


        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.button(QDialogButtonBox.Ok).setText("确定")
        button_box.button(QDialogButtonBox.Cancel).setText("取消")
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        dialog_layout.addWidget(button_box)
        dialog.setLayout(dialog_layout)
        self.dialog = dialog
        self.edits = edits

        return dialog, edits

    # 编辑框后处理
    def handle_dialog_accept(self):
        if self.dialog.exec_() == QDialog.Accepted:
            data = []
            # print(self.edits)
            for item in self.edits:
                if isinstance(item, QComboBox):
                    # <PySide6.QtWidgets.QComboBox(0x2c89b5319a0) at 0x000002C8AC525F40>
                    # print("QComboBox")
                    # value = item.currentIndex()
                    # value_text = item.currentText()
                    value = item.currentText()
                    # print(value_text)
                else:
                    # <PySide6.QtWidgets.QLineEdit(0x2c896b0a250) at 0x000002C8AC517E00>
                    # print("QLineEdit")
                    value = item.text()
                # print(value)
                data.append(value) 
            labels =  [item["label"] for item in self.labels]
            result = {}
            result["status"] = "accept"
            result["name"] = self.key  # 如：crons
            result["value"] = dict(zip(labels, data)) 
            result["edit_row"] = self.edit_row
            self.table_dialog_accepted.emit(result)
        else:
            result = {}
            result["status"] = "cancel"
            result["name"] = self.key  # 如：crons
            self.table_dialog_accepted.emit(result)

    # def is_valid_cron(self, cron_time):
    #     # Validate cron time in HH:MM format
    #     pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
    #     return re.match(pattern, cron_time) is not None


    def show_edit_dialog(self, title, labels, initial_values, input_types):
        dialog = QDialog(self.parent)
        dialog.setWindowTitle(title)
        dialog_layout = QVBoxLayout()

        widgets = []
        for label_text, initial_value, input_type in zip(labels, initial_values, input_types):
            label = QLabel(label_text)
            if input_type == "QLineEdit":
                widget = QLineEdit(initial_value)
            elif input_type == "QComboBox":
                widget = QComboBox()
                widget.addItems(initial_value)
            else:
                raise ValueError(f"Unsupported input type: {input_type}")
            dialog_layout.addWidget(label)
            dialog_layout.addWidget(widget)
            widgets.append(widget)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.button(QDialogButtonBox.Ok).setText("确定")
        button_box.button(QDialogButtonBox.Cancel).setText("取消")
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        dialog_layout.addWidget(button_box)
        dialog.setLayout(dialog_layout)

        if dialog.exec_() == QDialog.Accepted:
            return [widget.text() if isinstance(widget, QLineEdit) else widget.currentText() for widget in widgets]
        else:
            return None

    def show_success_message(self, text="操作成功", type="success"):
        msg_box = QMessageBox(self.parent)
        msg_box.setWindowTitle("提示")
        msg_box.setText(text)

        if type == "success":
            msg_box.setIcon(QMessageBox.Information)
        elif type == "warning":
            msg_box.setIcon(QMessageBox.Warning)
        elif type == "error":
            msg_box.setIcon(QMessageBox.Critical)

        msg_box.exec_()