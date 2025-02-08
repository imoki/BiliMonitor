from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QMessageBox, QComboBox
from PySide6.QtCore import Qt

class TableEditView:
    def __init__(self, parent):
        self.parent = parent

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