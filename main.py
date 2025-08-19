import sys
import os
import platform
import json

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

from PySide6.QtCore import QMutex

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


# 导入自定义逻辑模块
from src.services.home.home_service import HomeService
from src.services.dynamic.dynamic_service import DynamicService
from src.services.crontab.crontab_service import CrontabService
from src.services.log.log_service import LogService
from src.respository.config_manager import ConfigManager
from src.respository.daily_manager import DailyManager
from src.services.daily.daily_thread import DailyThread
from src.services.cookie.cookie_service import CookieService
from src.services.dynamic.dynamic_thread import DynamicThread
from src.services.log.real_time_log_service import RealTimeLogService
from src.services.download.download_service import DownloadService
from src.services.download.download_thread import DownloadThread
# 导入自定义图形模块
from src.views.element_style import ElementStyle
from src.views.bubble_widget import BubbleWidget
from src.views.prompt_view import PromptView

try:
    from ctypes import windll  # Only exists on Windows.
    # myappid = 'BiliMonitor'
    # myappid = 'mycompany.myproduct.subproduct.version'
    myappid = '哔哩哨兵'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass



class MainWindow(QMainWindow):
    main_sign = Signal(str)

    def __init__(self, is_confirm_quit: bool = True):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.is_confirm_quit = is_confirm_quit

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "哔哩哨兵"
        description = ""    # 用于监控哔哩最新视频并定时下载的软件
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

       

        #################################哔哩哨兵功能开始##################################
         # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_cookie.clicked.connect(self.buttonClick)
        widgets.btn_list.clicked.connect(self.buttonClick)
        widgets.btn_cron.clicked.connect(self.buttonClick)
        widgets.btn_history.clicked.connect(self.buttonClick)
        widgets.btn_download.clicked.connect(self.buttonClick)
        widgets.btn_setting.clicked.connect(self.buttonClick)
        widgets.btn_minimize_tray.clicked.connect(self.buttonClick)

        # 应用样式表以模仿 Element UI 风格
        self.elementStyle = ElementStyle(parent = self)
        self.elementStyle.apply_element_style()

        # 配置参数
        config_path = ".\\config\\config.json"
        daily_cookie_path =".\\exe\\win-x64\\cookies.json"
        daily_appsettings_path = ".\\exe\\win-x64\\appsettings.json"
        log_path = ".\\config\\history.json"
        video_path = ".\\video\\"    # 视频保存路径

        # cookie页配置
        cookieTable = self.ui.tableWidget_cookie
        cookieKey = "cookie"    # 数据存放key
        cookieUnique = "nickname"    # 主键

        # 动态页配置，获取最新动态视频相关
        dynamicTable = self.ui.tableWidget_list
        dynamicKey = "uids" # 数据存放key，用于获取全部数据
        dynamicUnique = "uid" # 主键，唯一值，用于保证表内数据唯一性

        # 定时任务配置
        crontabTable = self.ui.tableWidget_cron
        crontabKey = "crons"    # 数据存放key
        crontabUnique = "name"    # 主键

        # 下载页配置
        downloadTable = self.ui.tableWidget_download
        downloadKey = "download"    # 数据存放key
        downloadUnique = "url"    # 主键

        # 历史记录配置
        logTable = self.ui.tableWidget_history
        logKey = "history"  # 数据存放key
        logUnique = "start_time"  # 主键

        # 服务初始化
        self.configManager = ConfigManager(parent = self, config_path = config_path, video_path = video_path)
        self.dailyManager = DailyManager(parent = self, daily_cookie_path = daily_cookie_path, daily_appsettings_path = daily_appsettings_path, configManager = self.configManager)
        self.homeservice = HomeService(parent = self, configManager = self.configManager)
        self.cookieService = CookieService(parent = self, table = cookieTable, key = cookieKey, unique = cookieUnique, configManager = self.configManager)
        self.dynamicService = DynamicService(parent = self, table = dynamicTable, key = dynamicKey, unique = dynamicUnique, configManager = self.configManager)
        self.crontabService = CrontabService(parent = self, table = crontabTable, key = crontabKey, unique = crontabUnique, configManager = self.configManager)
        self.downloadService = DownloadService(parent = self, table = downloadTable, key = downloadKey, unique = downloadUnique, configManager = self.configManager)
        self.logService = LogService(parent = self, table = logTable, key = logKey, unique = logUnique, configManager = self.configManager, log_path = log_path)
        self.realTimeLogService = RealTimeLogService(parent = self)
        # 加载配置文件
        self.configManager.load_config()

        # 主页，HOME页
        # # 设置cookie按钮
        # self.ui.pushButton_home_1.clicked.connect(lambda: self.homeservice.save_cookie())
        # # 添加uid按钮
        # self.ui.pushButton_home_2.clicked.connect(lambda: self.dynamicService.add_id())
        # # 下一页按钮
        # self.ui.pushButton_next_1.clicked.connect(self.buttonClick)

        # 主页，HOME页
        # 下一页按钮
        self.ui.pushButton_home_next.clicked.connect(self.buttonClick)

        # cookie页-菜单
        # 添加cookie按钮
        self.ui.pushButton_cookie_1.clicked.connect(lambda: self.cookieService.table_create())
        # 右键菜单
        self.ui.tableWidget_cookie.setContextMenuPolicy(Qt.CustomContextMenu)
        self.context_menu_params = {
            "cookieUnique": cookieUnique
        }
        self.ui.tableWidget_cookie.customContextMenuRequested.connect(
            lambda pos: self.show_context_menu(pos, **self.context_menu_params)
        )
        # 下一页按钮
        self.ui.pushButton_cookie_next.clicked.connect(self.buttonClick)

        # 动态页面
        # 下一页按钮
        self.ui.pushButton_next_2.clicked.connect(self.buttonClick)
        # 右键菜单
        self.ui.tableWidget_list.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.getSelected = QAction("删除")
        self.getSelected.triggered.connect(lambda: self.dynamicService.table_delete_selected_rows())
        self.ui.tableWidget_list.addAction(self.getSelected)
        self.getEdit = QAction("编辑")
        self.getEdit.triggered.connect(lambda: self.dynamicService.table_edit())
        self.ui.tableWidget_list.addAction(self.getEdit)
        # 添加按钮
        self.ui.pushButton_list_1.clicked.connect(lambda: self.dynamicService.table_create())
        # 补全信息按钮，补全名称和备注
        # self.ui.pushButton_list_2.clicked.connect(lambda: self.dynamicService.table_fill_info(self.realTimeLogService))
        self.ui.pushButton_list_2.clicked.connect(self.buttonClick)
        # # 清空信息按钮，清空名称和备注
        # self.ui.pushButton_list_3.clicked.connect(lambda: self.dynamicService.table_clear_info())

        #定时任务页, CRON页面
        # 添加定时任务按钮
        self.ui.pushButton_cron_1.clicked.connect(lambda: self.crontabService.table_create())
        # 立即运行按钮
        self.ui.pushButton_cron_3.clicked.connect(self.run_cron)    
        # 立即结束按钮
        self.ui.pushButton_cron_4.clicked.connect(self.stop_cron)
        # 完成按钮
        self.ui.pushButton_cron_2.clicked.connect(self.buttonClick)
        # 右键菜单
        self.ui.tableWidget_cron.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.getSelected_cron = QAction("删除")
        self.getSelected_cron.triggered.connect(lambda: self.crontabService.table_delete_selected_rows())
        self.ui.tableWidget_cron.addAction(self.getSelected_cron)
        self.getEdit_cron = QAction("编辑")
        self.getEdit_cron.triggered.connect(lambda: self.crontabService.table_edit())
        self.ui.tableWidget_cron.addAction(self.getEdit_cron)

        # 下载页
        # 添加按钮
        self.ui.pushButton_download_1.clicked.connect(lambda: self.downloadService.table_create())
        # 下载按钮
        self.ui.pushButton_download_2.clicked.connect(self.download)    
        # 右键菜单
        self.ui.tableWidget_download.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.getSelected_download = QAction("删除")
        self.getSelected_download.triggered.connect(lambda: self.downloadService.table_delete_selected_rows())
        self.ui.tableWidget_download.addAction(self.getSelected_download)
        self.getEdit_download = QAction("编辑")
        self.getEdit_download.triggered.connect(lambda: self.downloadService.table_edit())
        self.ui.tableWidget_download.addAction(self.getEdit_download)
        
        # HISTORY界面，历史日志
        # 右键菜单
        self.ui.tableWidget_history.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.getSelected_history = QAction("删除")
        self.getSelected_history.triggered.connect(lambda: self.logService.table_delete_selected_rows_history())
        self.ui.tableWidget_history.addAction(self.getSelected_history)

        # SETTING界面，设置界面
        # 确认键
        self.ui.pushButton_setting_1.clicked.connect(lambda: self.dailyManager.modify_settings())
        # 重置键
        self.ui.pushButton_setting_2.clicked.connect(lambda: self.dailyManager.reset_default_config())
        # 复选框
        # 是否观看视频
        self.ui.checkBox_setting_DailyTaskConfig_IsWatchVideo.stateChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.IsWatchVideo", self.ui.checkBox_setting_DailyTaskConfig_IsWatchVideo))
        # 是否分享视频
        self.ui.checkBox_setting_DailyTaskConfig_IsShareVideo.stateChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.IsShareVideo", self.ui.checkBox_setting_DailyTaskConfig_IsShareVideo))
        # 是否开启专栏投币
        self.ui.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.stateChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.IsDonateCoinForArticle", self.ui.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle))
        # 达到六级后是否开始白嫖[false,true]
        self.ui.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.stateChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.SaveCoinsWhenLv6", self.ui.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6))
        # 投币时是否同时点赞[false,true]
        self.ui.checkBox_setting_DailyTaskConfig_SelectLike.stateChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.SelectLike", self.ui.checkBox_setting_DailyTaskConfig_SelectLike))
        # combox下拉框
        # 每日设定的投币数 [0,5]
        self.ui.comboBox_setting_DailyTaskConfig_NumberOfCoins.currentIndexChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.NumberOfCoins", self.ui.comboBox_setting_DailyTaskConfig_NumberOfCoins))
        # 每月几号自动充电[-1,31]，-1表示不指定，默认月底最后一天；0表示不充电
        self.ui.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.currentIndexChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.DayOfAutoCharge", self.ui.comboBox_setting_DailyTaskConfig_DayOfAutoCharge))
        # 每月几号自动领取会员权益的[-1,31]，-1表示不指定，默认每月1号；0表示不自动领取
        self.ui.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.currentIndexChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.DayOfReceiveVipPrivilege", self.ui.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege))
        # 每月几号执行银瓜子兑换硬币[-1,31]，-1表示不指定，默认每月最后一天；-2表示每天；0表示不进行兑换
        self.ui.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.currentIndexChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.DayOfExchangeSilver2Coin", self.ui.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin))
        # 执行客户端操作时的平台 [ios,android]
        self.ui.comboBox_setting_DailyTaskConfig_DevicePlatform.currentIndexChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.DevicePlatform", self.ui.comboBox_setting_DailyTaskConfig_DevicePlatform))
        # LineEdit，文本框
        # 要保留的硬币数量 [0,int_max]，0 为不保留，int_max 通常取 (2^31)-1
        self.ui.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.textChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.NumberOfProtectedCoins", self.ui.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins))
        # 优先选择支持的up主Id集合，多个以英文逗号分隔，如："123,456"。配置后会优先从指定的up主下挑选视频进行观看、分享和投币，不配置或配置为-1则表示没有特别支持的up，会从关注和排行耪中随机获取支持视频
        self.ui.lineEdit_setting_DailyTaskConfig_SupportUpIds.textChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.SupportUpIds", self.ui.lineEdit_setting_DailyTaskConfig_SupportUpIds))
        # 指定支持的UP主Id，-1表示自己
        self.ui.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.textChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.AutoChargeUpId", self.ui.lineEdit_setting_DailyTaskConfig_AutoChargeUpId))
        # 充电后留言
        self.ui.lineEdit_setting_DailyTaskConfig_ChargeComment.textChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.ChargeComment", self.ui.lineEdit_setting_DailyTaskConfig_ChargeComment))
        # 自定义漫画阅读 comic_id，若不清楚含义请勿修改
        self.ui.lineEdit_setting_DailyTaskConfig_CustomComicId.textChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.CustomComicId", self.ui.lineEdit_setting_DailyTaskConfig_CustomComicId))
        # 自定义漫画阅读 ep_id，若不清楚含义请勿修改
        self.ui.lineEdit_setting_DailyTaskConfig_CustomEpId.textChanged.connect(lambda: self.dailyManager.setting("DailyTaskConfig.CustomEpId", self.ui.lineEdit_setting_DailyTaskConfig_CustomEpId))

        # 线程相关
        # 定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_cron_tasks)
        self.timer.start(60000)  # 60000，即每分钟检查一次
        self.mutex = QMutex()
        # 信号和槽连接
        self.taskThread = None
        self.taskThread_signal_connected = False

        # UI显示相关
        self.prompt_view = PromptView(self)


        # # 自定义关闭按钮
        # # 创建系统托盘图标
        # self.tray_icon = QSystemTrayIcon(QIcon("images/images/PyDracula.png"), self)
        # self.tray_icon.setToolTip(title)
        # # 创建托盘菜单
        # self.tray_menu = QMenu(self)
        # self.restore_action = QAction("恢复", self)
        # self.quit_action = QAction("退出", self)
        # self.tray_menu.addAction(self.restore_action)
        # self.tray_menu.addAction(self.quit_action)
        # self.tray_icon.setContextMenu(self.tray_menu)
        # # 连接信号和槽
        # self.restore_action.triggered.connect(self.show)
        # self.quit_action.triggered.connect(self.quit_app)
        # self.tray_icon.activated.connect(self.on_tray_icon_activated)

        # # 显示托盘图标
        # self.tray_icon.show()


        # # 测试
        # self.logService.append_history("测试", "运行结束", "1", "2")
        # current_time = QTime.currentTime().toString("hh:mm")
        # print(current_time) # 13:00

        #################################哔哩哨兵功能结束##################################

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        # widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        # 初始加载主页界面
        widgets.stackedWidget.setCurrentWidget(widgets.page_home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # 主页按钮
        if btnName == "btn_home":
            # widgets.stackedWidget.setCurrentWidget(widgets.home)
            widgets.stackedWidget.setCurrentWidget(widgets.page_home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.cookieService.load_table()

        # 主页-下一步按钮
        if btnName == "pushButton_home_next":
            widgets.stackedWidget.setCurrentWidget(widgets.page_cookie) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            self.cookieService.load_table()

        # cookie页的按钮
        if btnName == "btn_cookie":
            widgets.stackedWidget.setCurrentWidget(widgets.page_cookie) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            self.cookieService.load_table()

        # cookie页的下一步按钮，跳转到下一页
        if btnName == "pushButton_cookie_next":
            widgets.stackedWidget.setCurrentWidget(widgets.page_list) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            self.dynamicService.load_table()

        # UP页
        if btnName == "btn_list":
            # widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            widgets.stackedWidget.setCurrentWidget(widgets.page_list)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.dynamicService.load_table()

        # UP页-下一步按钮
        if btnName == "pushButton_next_2":
            widgets.stackedWidget.setCurrentWidget(widgets.page_cron) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            self.crontabService.load_table()

        # UP页-UP信息补全按钮
        if btnName == "pushButton_list_2":
            # widgets.stackedWidget.setCurrentWidget(widgets.page_cron) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            cron = {"name": "UP信息补全", "type": 2}
            self.run_cron(cron)

        # 定时任务页
        if btnName == "btn_cron":
            widgets.stackedWidget.setCurrentWidget(widgets.page_cron) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            self.crontabService.load_table()

        # 定时任务页-完成按钮
        if btnName == "pushButton_cron_2":
            self.prompt_view.prompt(text="完成", type="success")
        
        # 下载页
        if btnName == "btn_download":
            widgets.stackedWidget.setCurrentWidget(widgets.page_download) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            self.downloadService.load_table()
        
        # 历史日志页
        if btnName == "btn_history":
            widgets.stackedWidget.setCurrentWidget(widgets.page_history) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            self.logService.load_table()

        # 设置页
        if btnName == "btn_setting":
            # widgets.stackedWidget.setCurrentWidget(widgets.home)
            widgets.stackedWidget.setCurrentWidget(widgets.page_setting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.dailyManager.load_settings()
        
        # 最小化到系统托盘
        if btnName == "btn_minimize_tray":
            self.minimizeToTray()


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        

    # def show_success_message(self, text="保存成功", type="success"):
    #     bubble = BubbleWidget(self, text, type)
    #     # 显示气泡提示框
    #     bubble_width = bubble.sizeHint().width()
    #     bubble_height = bubble.sizeHint().height()
    #     window_width = self.width()
    #     window_height = self.height()
    #     # 设置气泡提示框距离底部60像素
    #     bubble.setGeometry((window_width - bubble_width) // 2, window_height - bubble_height - 60, bubble_width, bubble_height)
    #     bubble.show()

    # # 折叠到系统托盘
    # def closeEvent(self, event):
    #     # 最小化到系统托盘
    #     self.hide()
    #     self.tray_icon.showMessage("最小化到系统托盘", "双击系统托盘图标可恢复，右键可选退出。", QSystemTrayIcon.Information, 1500)
    #     event.ignore()  # 忽略默认的关闭事件

    # def on_tray_icon_activated(self, reason):
    #     # 双击系统托盘图标
    #     if reason == QSystemTrayIcon.DoubleClick:
    #         self.show()
    #     if reason == QSystemTrayIcon.Trigger:
    #         self.show()

    # def quit_app(self):
    #     QApplication.quit()

    def show_context_menu(self, pos, **kwargs):
        menu = QMenu()
        # menu.setStyleSheet(element_ui_menu_style)  # 应用样式表
        menu.setStyleSheet(self.elementStyle.element_ui_menu_style) 

        delete_action = menu.addAction("删除")
        edit_action = menu.addAction("编辑")

        print(pos)
        print(self.ui.tableWidget_cookie.mapToGlobal(pos))
        action = menu.exec(self.ui.tableWidget_cookie.mapToGlobal(pos))
        if action == delete_action:
            self.cookieService.table_delete_selected_rows()
        elif action == edit_action:
            self.cookieService.table_edit()

        # # 关闭菜单栏
        # menu.close()

    # 初始化系统托盘图标和菜单
    def setup_tray_icon(self):
        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(QIcon("icon/icon.ico"), self)
        # self.tray_icon.setToolTip("BiliMonitor")
        self.tray_icon.setToolTip("哔哩哨兵")
        
        # 创建托盘菜单
        self.tray_menu = QMenu(self)
        self.restore_action = QAction("恢复", self)
        self.quit_action = QAction("退出", self)
        self.tray_menu.addAction(self.restore_action)
        self.tray_menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        
        # 连接信号和槽
        self.restore_action.triggered.connect(self.show)
        self.quit_action.triggered.connect(self.quit_app)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)

            
        # 显示系统托盘图标
        self.tray_icon.show()

    # 折叠到系统托盘
    def minimizeToTray(self):
        # 最小化到系统托盘
        self.hide()
        self.tray_icon.showMessage("最小化到系统托盘", "双击系统托盘图标可恢复，右键可选退出。", QSystemTrayIcon.Information, 1500)

    # 退出
    def quit_app(self):
        QApplication.quit()

    def on_tray_icon_activated(self, reason):
        # 双击系统托盘图标
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()
        if reason == QSystemTrayIcon.Trigger:
            self.show()

    # 提示确认退出窗口
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.is_confirm_quit:
            reply = QMessageBox.question(self, '退出', '确定退出吗?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
                self.quit_app()
            else:
                event.ignore()
        else:
            event.accept()

    def download(self):
        if self.taskThread and self.taskThread.isRunning():
            # print("已有任务正在运行")
            self.prompt_view.prompt(text="已有任务正在运行", type="warning")
            return
            
        # 创建并启动任务线程
        self.taskThread = DownloadThread(parent=self, downloadService = self.downloadService, logService = self.logService)
        if not self.taskThread_signal_connected:
            self.taskThread.started.connect(self.thread_started, Qt.QueuedConnection)
            self.taskThread.signal.connect(self.thread_signal, Qt.QueuedConnection)
            self.taskThread.finished.connect(self.thread_finished, Qt.QueuedConnection)
            self.taskThread_signal_connected = True
            self.taskThread.start()

    # 检查是否有要执行的定时任务
    def check_cron_tasks(self):
        # print("Checking cron tasks...")
        current_time = QTime.currentTime().toString("hh:mm")
        key = "crons"
        crons = self.configManager.read_config(key)
        if crons is None:
            return
        for cron in crons:
            if cron["cron"] == current_time:
                # # 执行任务
                # self.run_specific_cron(cron["name"])

                # # 传递任务字典
                # self.run_specific_cron(cron)
                self.run_cron(cron)

    def run_specific_cron(self, cron):
        # 根据cron执行特定的任务
        self.run_cron(cron)

    # 立即结束线程
    def stop_cron(self):
        if self.taskThread and self.taskThread.isRunning():
            self.taskThread.terminate()
            self.taskThread.wait()  # 等待线程终止
            self.taskThread_signal_connected = False
            self.prompt_view.prompt(text="已终止任务", type="success")
        else:
            self.prompt_view.prompt(text="没有运行的任务", type="warning")

    # 运行任务（定时或自定义任务），一次只有一个在运行
    def run_cron(self, cron):
        # cron为字典
        # 定时任务
        # cron = {"name": "任务名称", "type": "任务类型", "cron_time": "定时时间"}
        # 自定义任务
        # cron = {"name": "任务名称", "type": "任务类型"}

        # type 任务类型默认0
        # 0 下载任务，1 每日任务，
        # print(cron)

        if cron == False:
            # print("立即运行首个定时任务")
            # 取第一个任务
            crons = self.configManager.read_config("crons")
            if crons is None:
                self.prompt_view.prompt(text="没有定时任务", type="warning")
                return
            cron = crons[0]
        # print(cron)
        cron_name = cron["name"]
        # 根据config中cron中的type判断运行类型
        # key = "crons"
        # content = self.configManager.read_config(key)
        # cron = self.crontabService.get_cron_by_name(content, cron_name)
        type_cron = cron["type"]
        # print(type_cron)

        if self.taskThread and self.taskThread.isRunning():
            # print("已有任务正在运行")
            self.prompt_view.prompt(text="已有任务正在运行", type="warning")
            return

        if type_cron == 0:
            # print("运行下载视频线程...")
                
            # 创建并启动任务线程
            self.taskThread = DynamicThread(parent=self, dynamicService = self.dynamicService, logService = self.logService, cron_name=cron_name)
        elif type_cron == 1:
            # 运行做任务
            # print("运行每日任务线程...")
            # 创建并启动任务线程
            # command = "python -u main.py"   #  -u 参数来禁用缓冲
            # command = ".\exe\win-x64\Ray.BiliBiliTool.Console.exe --runTasks=Login"
            command = ".\exe\win-x64\Ray.BiliBiliTool.Console.exe --runTasks=Daily"
            # self.taskThread = OutputReaderThread(parent=self, cron_name=cron_name, command=command)
            # self.taskThread = DailyThread(parent=self, logService = self.logService, cron_name=cron_name, command=command)
            self.taskThread = DailyThread(parent=self, logService = self.logService, cron=cron, command=command, dailyManager = self.dailyManager)
            
        elif type_cron == 2:
            print("运行UP列表补全任务...")
            self.taskThread = DynamicThread(parent=self, dynamicService = self.dynamicService, logService = self.logService, cron_name=cron_name, realTimeLogService=self.realTimeLogService)

        else:
            # print("运行下载视频线程...")     
            # 创建并启动任务线程
            self.taskThread = DynamicThread(parent=self, dynamicService = self.dynamicService, logService = self.logService, cron_name=cron_name)
        
        # 启动线程
        if not self.taskThread_signal_connected:
            self.taskThread.started.connect(self.thread_started, Qt.QueuedConnection)
            self.taskThread.signal.connect(self.thread_signal, Qt.QueuedConnection)
            self.taskThread.finished.connect(self.thread_finished, Qt.QueuedConnection)
            self.taskThread_signal_connected = True
            self.taskThread.start()

    # 线程最开始执行时执行
    def thread_started(self):
        # print("Thread started")
        self.prompt_view.prompt(text="任务开始运行", type="success")
    
    # 线程结束时执行
    def thread_finished(self):
        # print("Thread finished")
        if self.taskThread:
            # with QMutexLocker(self.mutex):
            self.taskThread.deleteLater()
            self.taskThread = None  # 清理线程对象
            self.taskThread_signal_connected = False  # 重置信号和槽连接标志
            self.prompt_view.prompt(text="任务运行结束", type="success")

    # 线程信号，收到信号时执行
    def thread_signal(self, message):
        # print(f"Task signal received: {message}")

        # 处理特殊命令
        if message == "[LOG_CLEAR]":
            self.realTimeLogService.clear_log()
            return
        elif message == "[LOG_DEFAULT]":
            self.realTimeLogService.show_default_log()
            return
        
        # 正常的日志消息
        self.realTimeLogService.append_log(message)
        content = "🎉 任务完成"
        if content in message:
            self.prompt_view.prompt(text="任务运行结束", type="success")

    # 命令行窗口信息处理信号
    def thread_signal_cmd(self, message):
        # print(f"Task signal received: {message}")
        content = "🎉 任务完成"
        if content in message:
            self.prompt_view.prompt(text="任务运行结束", type="success")

    # 线程结束时执行
    def thread_finished_cmd(self):
        # print("Thread finished")
        if self.taskThread:
            # with QMutexLocker(self.mutex):
            self.taskThread.deleteLater()
            self.taskThread = None  # 清理线程对象
            self.taskThread_signal_connected = False  # 重置信号和槽连接标志
            self.prompt_view.prompt(text="每日任务运行结束", type="success")
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./icon/icon.ico"))

    window = MainWindow(is_confirm_quit=True)
    window.setup_tray_icon()  # 初始化系统托盘图标
    # sys.exit(app.exec_())
    sys.exit(app.exec())
