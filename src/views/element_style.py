

class ElementStyle():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '')

        # 右键菜单
        self.element_ui_menu_style = """
        QMenu {
            background-color: #fff;
            border: 1px solid #dcdcdc;
            border-radius: 4px;
            padding: 5px 0;
            font-size: 14px;
        }

        QMenu::item {
            padding: 10px 20px;
            color: #606266;
        }

        QMenu::item:selected {
            background-color: #ecf5ff;
            color: #409eff;
        }
        """


    def apply_element_style(self):
        style_sheet = """
            QMenu {
                background-color: white;
                border: 1px solid #e4e7ed;
                border-radius: 4px;
                padding: 2px;
            }
            QMenu::item {
                padding: 8px 20px;
                margin: 2px 0;
                background-color: transparent;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #f0f2f5;
                color: #606266;
            }
            QMenu::separator {
                height: 1px;
                background-color: #e4e7ed;
                margin: 4px 0;
            }
            QLineEdit {
                background-color: #f5f7fa;
                border: 1px solid #dcdfe6;
                border-radius: 4px;
                padding: 10px 15px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #409EFF;
                outline: none;
            }
            QLabel {
                color: #606266;
                font-size: 14px;
            }
            QDialog {
                background-color: white;
                border: 1px solid #e4e7ed;
                border-radius: 4px;
                padding: 20px;
            }
            QDialogButtonBox QPushButton {
                background-color: #409EFF;
                border: none;
                color: white;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 14px;
            }
            QDialogButtonBox QPushButton:hover {
                background-color: #66b1ff;
            }
            QDialogButtonBox QPushButton:pressed {
                background-color: #3a8ee6;
            }
            QDialogButtonBox QPushButton:disabled {
                background-color: #c0c4cc;
                color: #ffffff;
            }

            QComboBox {
                background-color: #f5f7fa;
                border: 1px solid #dcdfe6;
                border-radius: 4px;
                padding: 10px 15px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #dcdfe6;
                border-left-style: solid;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
            QComboBox::down-arrow {
                image: url(:/icons/images/icons/cil-arrow-bottom.png);
                width: 12px;
                height: 12px;
            }
            QComboBox::down-arrow:on {
                top: 1px;
                left: 1px;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid #e4e7ed;
                border-radius: 4px;
                padding: 2px;
            }
            QComboBox QAbstractItemView::item {
                padding: 8px 20px;
                margin: 2px 0;
                background-color: transparent;
                border-radius: 4px;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #f0f2f5;
                color: #606266;
            }
        """
        self.parent.setStyleSheet(style_sheet)
