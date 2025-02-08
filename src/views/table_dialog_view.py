from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QDialogButtonBox
import re

class TableDialogView:
    @staticmethod
    def create_dialog(parent, title, labels, placeholders, combo_items=None):
        dialog = QDialog(parent)
        dialog.setWindowTitle(title)
        dialog_layout = QVBoxLayout()

        edits = []
        for label_text, placeholder in zip(labels, placeholders):
            label = QLabel(label_text)
            edit = QLineEdit(placeholder)
            dialog_layout.addWidget(label)
            dialog_layout.addWidget(edit)
            edits.append(edit)

        if combo_items:
            combo_label = QLabel(combo_items['label'])
            combo = QComboBox()
            for item in combo_items['items']:
                combo.addItem(item)
            dialog_layout.addWidget(combo_label)
            dialog_layout.addWidget(combo)
            edits.append(combo)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.button(QDialogButtonBox.Ok).setText("确定")
        button_box.button(QDialogButtonBox.Cancel).setText("取消")
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        dialog_layout.addWidget(button_box)
        dialog.setLayout(dialog_layout)

        return dialog, edits
    @staticmethod
    def handle_dialog_accept(dialog, edits, config_manager, key, prompt_view, load_table, unique_key, combo_items=None):
        if dialog.exec_() == QDialog.Accepted:
            values = []

            for edit in edits[:-1]:
                values.append(edit.text())

            if combo_items:
                # Use currentText() for QComboBox
                combo = edits[-1]
                # type_selected_text = combo.currentText()
                # values.append(type_selected_text)
                type_selected_index = combo.currentIndex()
                values.append(type_selected_index)

            # Validate cron time
            cron_time = values[1]
            if not TableDialogView.is_valid_cron(cron_time):
                prompt_view.prompt(text="定时时间格式不正确，请使用 HH:MM 格式", type="warning")
                return

            dict = {
                unique_key: values[0],
                "cron": cron_time,
                "notes": "",
            }

            if combo_items:
                dict["type"] = values[-1]
            else:
                dict["cookie"] = values[1]

            content = config_manager.read_config(key)

            if content:
                for item in content:
                    if item[unique_key] == values[0]:
                        prompt_view.prompt(text=f"{values[0]} 已存在", type="warning")
                        return

                content.append(dict)
                config_manager.update_config(key, content)
                prompt_view.prompt(text="编辑成功", type="success")
                load_table()
            else:
                content = [dict]
                config_manager.update_config(key, content)
                prompt_view.prompt(text="编辑成功", type="success")
                load_table()
        else:
            prompt_view.prompt(text="取消添加", type="warning")

    @staticmethod
    def is_valid_cron(cron_time):
        # Validate cron time in HH:MM format
        pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        return re.match(pattern, cron_time) is not None