from ..respository.config_manager import ConfigManager

# 表编辑
def table_edit_list(self):
    row = parent.ui.tableWidget_list.currentRow()
    # print(f"正在编辑第 {row} 行")
    # 获取当前行的数据
    uid_item = parent.ui.tableWidget_list.item(row, 0)
    name_item = parent.ui.tableWidget_list.item(row, 1)
    notes_item = parent.ui.tableWidget_list.item(row, 2)


    if not uid_item or not name_item:
        parent.show_success_message(text="无法编辑此行", type="warning")
        return

    uid = uid_item.text()
    name = name_item.text()
    try:
        notes = notes_item.text()
    except:
        notes = ""

    # 创建一个对话框来编辑数据
    dialog = QDialog(self)
    dialog.setWindowTitle("编辑数据")
    dialog_layout = QVBoxLayout()

    uid_label = QLabel("ID:")
    uid_edit = QLineEdit(uid)
    name_label = QLabel("名称:")
    name_edit = QLineEdit(name)
    notes_label = QLabel("备注:")
    notes_edit = QLineEdit(notes)

    dialog_layout.addWidget(uid_label)
    dialog_layout.addWidget(uid_edit)
    dialog_layout.addWidget(name_label)
    dialog_layout.addWidget(name_edit)
    dialog_layout.addWidget(notes_label)
    dialog_layout.addWidget(notes_edit)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.button(QDialogButtonBox.Ok).setText("确定")
    button_box.button(QDialogButtonBox.Cancel).setText("取消")
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    dialog_layout.addWidget(button_box)
    dialog.setLayout(dialog_layout)

    if dialog.exec_() == QDialog.Accepted:
        new_uid = uid_edit.text()
        new_name = name_edit.text()
        new_notes = notes_edit.text()

        # 更新表格中的数据
        parent.ui.tableWidget_list.setItem(row, 0, QTableWidgetItem(new_uid))
        parent.ui.tableWidget_list.setItem(row, 1, QTableWidgetItem(new_name))
        parent.ui.tableWidget_list.setItem(row, 2, QTableWidgetItem(new_notes))

        # 更新配置文件中的数据
        configManger = ConfigManager()
        uids = configManger.read_config("uids")
        if uids:
            for item in uids:
                if item["uid"] == uid:
                    item["uid"] = new_uid
                    item["name"] = new_name
                    item["notes"] = new_notes
                    break
            configManger.update_config("uids", uids)

        parent.show_success_message(text="编辑成功", type="success")
    else:
        parent.show_success_message(text="编辑取消", type="warning")



# 删除表格中的某行。
def table_delete_selected_rows(parent, table, key, comp):
    """
    删除表格中的某行。
    :param table: 表格对象
    :param key: 配置文件中的key
    :param comp: 比较的key
    
    """
    # for i in parent.ui.tableWidget_list.selectedItems():
    #     print(f"获取到了第{i.row()}行，第{i.column()}列，元素为{i.text()}")
    
    row = table.currentRow()
    # 获取当前行的数据
    item = table.item(row, 0)
    if not item:
        parent.show_success_message(text="无法删除此行", type="warning")
        return

    itemtext = item.text()
    # print(itemtext)

    # 删除表格中的行
    table.removeRow(row)

    # 更新配置文件中的数据
    configManger = ConfigManager()
    content = configManger.read_config(key)
    if content:
        content = [item for item in content if item[comp] != itemtext]
        configManger.update_config(key, content)

    parent.show_success_message(text="删除成功", type="success")