# from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTimer
# from PySide6.QtGui import QPainter, QBrush, QColor, QPixmap
# from PySide6.QtCore import Qt, QPainterPath
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# 气泡提示框
class BubbleWidget(QWidget):
    def __init__(self, parent=None, text="", type="success"):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setContentsMargins(10, 10, 10, 10)

        self.label = QLabel(text, self)
        self.label.setStyleSheet("color: white; font-size: 14px;")

        # 添加图标
        self.icon_label = QLabel(self)
        if type == "success":
            pixmap = QPixmap(":/icons/images/icons/cil-check-alt.png")  # 替换为你的对勾图标路径
            self.setStyleSheet("background-color: rgba(76, 175, 80, 180);")  # 透明绿色背景
        elif type == "warning":
            pixmap = QPixmap(":/icons/images/icons/cil-fire.png")  # 替换为你的警告图标路径
            self.setStyleSheet("background-color: rgba(255, 193, 7, 180);")  # 透明黄色背景
        else:
            pixmap = QPixmap(":/icons/images/icons/cil-check-alt.png")  # 默认对勾图标
            self.setStyleSheet("background-color: rgba(76, 175, 80, 180);")  # 默认透明绿色背景

        self.icon_label.setPixmap(pixmap.scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        # 创建一个水平布局来放置图标和文本
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        horizontal_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        horizontal_layout.setSpacing(10)  # 设置图标和文本之间的间距

        layout.addLayout(horizontal_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.setSingleShot(True)

    def showEvent(self, event):
        super().showEvent(event)
        self.timer.start(1500)  # 显示1.5秒后关闭

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(self.palette().color(QPalette.Window))))  # 使用设置的背景颜色

        path = QPainterPath()
        rect = self.rect()
        path.addRoundedRect(rect, 10, 10)  # 圆角矩形

        # 添加气泡箭头
        arrow_size = 10
        arrow_x = rect.width() // 2 - arrow_size
        arrow_y = 0
        path.moveTo(arrow_x, arrow_y)
        path.lineTo(arrow_x + arrow_size, arrow_y)
        path.lineTo(arrow_x + arrow_size // 2, arrow_y - arrow_size)
        path.lineTo(arrow_x, arrow_y)
        painter.drawPath(path)