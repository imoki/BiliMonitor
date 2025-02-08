from PySide6.QtCore import QMutexLocker, QDateTime, Qt, QMetaObject, Q_ARG
import time

class RealTimeLogService():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '')

    # 清空日志
    def clear_log(self):
        # print("running clear_log...")
        with QMutexLocker(self.parent.mutex):  # 使用 QMutexLocker 确保线程安全
            self.parent.ui.plainTextEdit_cron.clear()
        # self.parent.ui.plainTextEdit_cron.clear()

            # 显示日志
    def show_log(self, text):
        # print("running show_log...")
        with QMutexLocker(self.parent.mutex):  # 使用 QMutexLocker 确保线程安全
            self.parent.ui.plainTextEdit_cron.setPlainText(text)
        # self.parent.ui.plainTextEdit_cron.setPlainText(text)
    
    # 追加日志
    def append_log(self, text):
        time.sleep(1)
        # print("running append_log...")
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        # print(current_time)
        text = f"[{current_time}] {text}"
        # print(text)
        # try:
        #     with QMutexLocker(self.parent.mutex):  # 使用 QMutexLocker 确保线程安全
        #         self.parent.ui.plainTextEdit_cron.appendPlainText(text)
        #     # self.parent.ui.plainTextEdit_cron.appendPlainText(text)
        # except Exception as e:
        #     print(f"Error in append_log: {e}")
        self.safe_append_text(text)
    
    def safe_append_text(self, text):
        QMetaObject.invokeMethod(self.parent.ui.plainTextEdit_cron, "appendPlainText", Qt.QueuedConnection, Q_ARG(str, text))
   

    # 打印默认消息
    def show_default_log(self):
        # print("running show_default_message...")
        # 当前时间
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        text = f"[{current_time}] 👻 开始运行"
        with QMutexLocker(self.parent.mutex):  # 使用 QMutexLocker 确保线程安全
            self.parent.ui.plainTextEdit_cron.appendPlainText(text)
        # self.parent.ui.plainTextEdit_cron.appendPlainText(text)



