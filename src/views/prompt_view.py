from PySide6.QtWidgets import QMessageBox
from .bubble_widget import BubbleWidget

class PromptView:
    def __init__(self, parent):
        self.parent = parent

    def prompt(self, text="保存成功", type="success"):
        bubble = BubbleWidget(self.parent, text, type)
        # 显示气泡提示框
        bubble_width = bubble.sizeHint().width()
        bubble_height = bubble.sizeHint().height()
        window_width = self.parent.width()
        window_height = self.parent.height()
        # 设置气泡提示框距离底部60像素
        bubble.setGeometry((window_width - bubble_width) // 2, window_height - bubble_height - 60, bubble_width, bubble_height)
        bubble.show()