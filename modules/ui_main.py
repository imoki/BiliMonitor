# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 729)
        MainWindow.setMinimumSize(QSize(940, 560))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setWeight(QFont.Normal)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleLeftDescription.setFont(font3)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_cookie = QPushButton(self.topMenu)
        self.btn_cookie.setObjectName(u"btn_cookie")
        sizePolicy.setHeightForWidth(self.btn_cookie.sizePolicy().hasHeightForWidth())
        self.btn_cookie.setSizePolicy(sizePolicy)
        self.btn_cookie.setMinimumSize(QSize(0, 45))
        self.btn_cookie.setFont(font1)
        self.btn_cookie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cookie.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_cookie.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_8.addWidget(self.btn_cookie)

        self.btn_list = QPushButton(self.topMenu)
        self.btn_list.setObjectName(u"btn_list")
        sizePolicy.setHeightForWidth(self.btn_list.sizePolicy().hasHeightForWidth())
        self.btn_list.setSizePolicy(sizePolicy)
        self.btn_list.setMinimumSize(QSize(0, 45))
        self.btn_list.setFont(font1)
        self.btn_list.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_list.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_list.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-quilt.png);")

        self.verticalLayout_8.addWidget(self.btn_list)

        self.btn_cron = QPushButton(self.topMenu)
        self.btn_cron.setObjectName(u"btn_cron")
        sizePolicy.setHeightForWidth(self.btn_cron.sizePolicy().hasHeightForWidth())
        self.btn_cron.setSizePolicy(sizePolicy)
        self.btn_cron.setMinimumSize(QSize(0, 45))
        self.btn_cron.setFont(font1)
        self.btn_cron.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cron.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_cron.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_cron)

        self.btn_download = QPushButton(self.topMenu)
        self.btn_download.setObjectName(u"btn_download")
        sizePolicy.setHeightForWidth(self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy)
        self.btn_download.setMinimumSize(QSize(0, 45))
        self.btn_download.setFont(font1)
        self.btn_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_download.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_download.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloud-download.png);")

        self.verticalLayout_8.addWidget(self.btn_download)

        self.btn_setting = QPushButton(self.topMenu)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 45))
        self.btn_setting.setFont(font1)
        self.btn_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_setting.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_setting)

        self.btn_history = QPushButton(self.topMenu)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setMinimumSize(QSize(0, 45))
        self.btn_history.setFont(font1)
        self.btn_history.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_history.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_history.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-history.png);")

        self.verticalLayout_8.addWidget(self.btn_history)

        self.btn_minimize_tray = QPushButton(self.topMenu)
        self.btn_minimize_tray.setObjectName(u"btn_minimize_tray")
        sizePolicy.setHeightForWidth(self.btn_minimize_tray.sizePolicy().hasHeightForWidth())
        self.btn_minimize_tray.setSizePolicy(sizePolicy)
        self.btn_minimize_tray.setMinimumSize(QSize(0, 45))
        self.btn_minimize_tray.setFont(font1)
        self.btn_minimize_tray.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_minimize_tray.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_minimize_tray.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-coffee.png);")

        self.verticalLayout_8.addWidget(self.btn_minimize_tray)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-heart.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setMinimumSize(QSize(0, 0))
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(0, 0))
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(False)
        self.titleRightInfo.setFont(font4)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.titleRightInfo.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font5)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(0, 0))
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.pagesContainer)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(100, 30))
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.page_download = QWidget()
        self.page_download.setObjectName(u"page_download")
        self.gridLayout_7 = QGridLayout(self.page_download)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelVersion_11 = QLabel(self.page_download)
        self.labelVersion_11.setObjectName(u"labelVersion_11")
        self.labelVersion_11.setMinimumSize(QSize(100, 0))
        self.labelVersion_11.setMaximumSize(QSize(100, 16777215))
        self.labelVersion_11.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_11.setLineWidth(1)
        self.labelVersion_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.labelVersion_11, 0, 0, 1, 1)

        self.horizontalSpacer_96 = QSpacerItem(86, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_96, 0, 1, 1, 2)

        self.pushButton_download_1 = QPushButton(self.page_download)
        self.pushButton_download_1.setObjectName(u"pushButton_download_1")
        self.pushButton_download_1.setMinimumSize(QSize(100, 30))
        self.pushButton_download_1.setMaximumSize(QSize(100, 30))

        self.gridLayout_7.addWidget(self.pushButton_download_1, 0, 3, 1, 2)

        self.horizontalSpacer_72 = QSpacerItem(85, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_72, 0, 5, 1, 2)

        self.horizontalSpacer_74 = QSpacerItem(223, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_74, 0, 7, 1, 2)

        self.horizontalSpacer_73 = QSpacerItem(129, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_73, 0, 9, 1, 1)

        self.horizontalSpacer_66 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_66, 0, 10, 1, 2)

        self.pushButton_download_2 = QPushButton(self.page_download)
        self.pushButton_download_2.setObjectName(u"pushButton_download_2")
        self.pushButton_download_2.setMinimumSize(QSize(100, 30))
        self.pushButton_download_2.setMaximumSize(QSize(100, 30))

        self.gridLayout_7.addWidget(self.pushButton_download_2, 0, 12, 1, 1)

        self.horizontalSpacer_95 = QSpacerItem(127, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_95, 0, 13, 1, 1)

        self.tableWidget_download = QTableWidget(self.page_download)
        if (self.tableWidget_download.columnCount() < 4):
            self.tableWidget_download.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_download.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_download.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_download.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_download.rowCount() < 50):
            self.tableWidget_download.setRowCount(50)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.tableWidget_download.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_download.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_download.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_download.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_download.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_download.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_download.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_download.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_download.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_download.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_download.setItem(0, 3, __qtablewidgetitem13)
        self.tableWidget_download.setObjectName(u"tableWidget_download")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget_download.sizePolicy().hasHeightForWidth())
        self.tableWidget_download.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.tableWidget_download.setPalette(palette)
        self.tableWidget_download.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_download.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_download.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_download.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_download.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_download.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_download.setShowGrid(True)
        self.tableWidget_download.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_download.setSortingEnabled(False)
        self.tableWidget_download.setRowCount(50)
        self.tableWidget_download.horizontalHeader().setVisible(False)
        self.tableWidget_download.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_download.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_download.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_download.verticalHeader().setVisible(False)
        self.tableWidget_download.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_download.verticalHeader().setHighlightSections(False)
        self.tableWidget_download.verticalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.tableWidget_download, 1, 0, 1, 14)

        self.horizontalSpacer_68 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_68, 2, 0, 1, 2)

        self.horizontalSpacer_70 = QSpacerItem(92, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_70, 2, 2, 1, 2)

        self.horizontalSpacer_67 = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_67, 2, 4, 1, 2)

        self.horizontalSpacer_76 = QSpacerItem(85, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_76, 2, 6, 1, 2)

        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_77, 2, 8, 1, 1)

        self.horizontalSpacer_69 = QSpacerItem(129, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_69, 2, 9, 1, 1)

        self.horizontalSpacer_75 = QSpacerItem(137, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_75, 2, 10, 1, 1)

        self.horizontalSpacer_64 = QSpacerItem(104, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_64, 2, 11, 1, 2)

        self.horizontalSpacer_65 = QSpacerItem(127, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_65, 2, 13, 1, 1)

        self.stackedWidget.addWidget(self.page_download)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.gridLayout_3 = QGridLayout(self.page_history)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelVersion_9 = QLabel(self.page_history)
        self.labelVersion_9.setObjectName(u"labelVersion_9")
        self.labelVersion_9.setMinimumSize(QSize(150, 0))
        self.labelVersion_9.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_9.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_9.setLineWidth(1)
        self.labelVersion_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_9, 0, 2, 1, 1)

        self.tableWidget_history = QTableWidget(self.page_history)
        if (self.tableWidget_history.columnCount() < 5):
            self.tableWidget_history.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        if (self.tableWidget_history.rowCount() < 15):
            self.tableWidget_history.setRowCount(15)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font6);
        self.tableWidget_history.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_history.setVerticalHeaderItem(9, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_history.setItem(0, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_history.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_history.setItem(0, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_history.setItem(0, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_history.setItem(0, 4, __qtablewidgetitem33)
        self.tableWidget_history.setObjectName(u"tableWidget_history")
        sizePolicy3.setHeightForWidth(self.tableWidget_history.sizePolicy().hasHeightForWidth())
        self.tableWidget_history.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.BrushStyle.NoBrush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.BrushStyle.NoBrush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.BrushStyle.NoBrush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.tableWidget_history.setPalette(palette1)
        self.tableWidget_history.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_history.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_history.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_history.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_history.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_history.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_history.setShowGrid(True)
        self.tableWidget_history.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_history.setSortingEnabled(False)
        self.tableWidget_history.setRowCount(15)
        self.tableWidget_history.horizontalHeader().setVisible(False)
        self.tableWidget_history.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_history.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_history.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_history.verticalHeader().setVisible(False)
        self.tableWidget_history.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_history.verticalHeader().setHighlightSections(False)
        self.tableWidget_history.verticalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableWidget_history, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_history)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_9 = QGridLayout(self.page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_22 = QSpacerItem(181, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_22, 1, 0, 1, 1)

        self.pushButton_home_1 = QPushButton(self.page)
        self.pushButton_home_1.setObjectName(u"pushButton_home_1")
        self.pushButton_home_1.setMinimumSize(QSize(100, 30))

        self.gridLayout_9.addWidget(self.pushButton_home_1, 1, 9, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_35, 4, 1, 1, 2)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_32, 6, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 152, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 5, 5, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(166, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_29, 4, 11, 1, 1)

        self.pushButton_home_2 = QPushButton(self.page)
        self.pushButton_home_2.setObjectName(u"pushButton_home_2")
        self.pushButton_home_2.setMinimumSize(QSize(100, 30))

        self.gridLayout_9.addWidget(self.pushButton_home_2, 4, 9, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_27, 1, 8, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_26, 4, 8, 1, 1)

        self.pushButton_next_1 = QPushButton(self.page)
        self.pushButton_next_1.setObjectName(u"pushButton_next_1")
        self.pushButton_next_1.setMinimumSize(QSize(100, 30))

        self.gridLayout_9.addWidget(self.pushButton_next_1, 6, 5, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_33, 6, 4, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(181, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_28, 1, 11, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_24, 6, 0, 1, 1)

        self.textEdit_home_2 = QTextEdit(self.page)
        self.textEdit_home_2.setObjectName(u"textEdit_home_2")
        self.textEdit_home_2.setMaximumSize(QSize(16777215, 30))
        self.textEdit_home_2.setReadOnly(False)

        self.gridLayout_9.addWidget(self.textEdit_home_2, 4, 3, 1, 5)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_38, 6, 1, 1, 2)

        self.textEdit_home_1 = QTextEdit(self.page)
        self.textEdit_home_1.setObjectName(u"textEdit_home_1")
        self.textEdit_home_1.setMaximumSize(QSize(16777215, 30))
        self.textEdit_home_1.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textEdit_home_1.setReadOnly(False)
        self.textEdit_home_1.setAcceptRichText(False)

        self.gridLayout_9.addWidget(self.textEdit_home_1, 1, 3, 1, 5)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_31, 6, 7, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_34, 1, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(182, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_23, 4, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_30, 6, 9, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 152, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 3, 5, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_25, 6, 11, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 152, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 0, 5, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.gridLayout_26 = QGridLayout(self.page_setting)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId = QLineEdit(self.page_setting)
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.setObjectName(u"lineEdit_setting_DailyTaskConfig_AutoChargeUpId")
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.setMinimumSize(QSize(150, 30))
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_26.addWidget(self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId, 14, 5, 1, 1)

        self.checkBox_setting_DailyTaskConfig_IsWatchVideo = QCheckBox(self.page_setting)
        self.checkBox_setting_DailyTaskConfig_IsWatchVideo.setObjectName(u"checkBox_setting_DailyTaskConfig_IsWatchVideo")
        self.checkBox_setting_DailyTaskConfig_IsWatchVideo.setMinimumSize(QSize(150, 0))
        self.checkBox_setting_DailyTaskConfig_IsWatchVideo.setMaximumSize(QSize(150, 16777215))
        self.checkBox_setting_DailyTaskConfig_IsWatchVideo.setAutoFillBackground(False)
        self.checkBox_setting_DailyTaskConfig_IsWatchVideo.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.checkBox_setting_DailyTaskConfig_IsWatchVideo, 3, 0, 1, 1)

        self.checkBox_setting_DailyTaskConfig_SelectLike = QCheckBox(self.page_setting)
        self.checkBox_setting_DailyTaskConfig_SelectLike.setObjectName(u"checkBox_setting_DailyTaskConfig_SelectLike")
        self.checkBox_setting_DailyTaskConfig_SelectLike.setMinimumSize(QSize(150, 0))
        self.checkBox_setting_DailyTaskConfig_SelectLike.setMaximumSize(QSize(150, 16777215))
        self.checkBox_setting_DailyTaskConfig_SelectLike.setAutoFillBackground(False)
        self.checkBox_setting_DailyTaskConfig_SelectLike.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.checkBox_setting_DailyTaskConfig_SelectLike, 3, 5, 1, 1)

        self.labelVersion_setting_1 = QLabel(self.page_setting)
        self.labelVersion_setting_1.setObjectName(u"labelVersion_setting_1")
        self.labelVersion_setting_1.setMinimumSize(QSize(150, 0))
        self.labelVersion_setting_1.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_setting_1.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_setting_1.setLineWidth(1)
        self.labelVersion_setting_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_setting_1, 1, 0, 1, 15)

        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge = QComboBox(self.page_setting)
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setObjectName(u"comboBox_setting_DailyTaskConfig_DayOfAutoCharge")
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setMinimumSize(QSize(150, 0))
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setMaximumSize(QSize(150, 16777215))
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setFont(font1)
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setAutoFillBackground(False)
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setIconSize(QSize(16, 16))
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setFrame(True)

        self.gridLayout_26.addWidget(self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge, 14, 2, 1, 1)

        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin = QComboBox(self.page_setting)
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setObjectName(u"comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin")
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setMinimumSize(QSize(150, 0))
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setMaximumSize(QSize(150, 16777215))
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setFont(font1)
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setAutoFillBackground(False)
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setIconSize(QSize(16, 16))
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setFrame(True)

        self.gridLayout_26.addWidget(self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin, 16, 2, 1, 1)

        self.comboBox_setting_DailyTaskConfig_DevicePlatform = QComboBox(self.page_setting)
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.addItem("")
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.addItem("")
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.addItem("")
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setObjectName(u"comboBox_setting_DailyTaskConfig_DevicePlatform")
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setMinimumSize(QSize(150, 0))
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setMaximumSize(QSize(150, 16777215))
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setFont(font1)
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setAutoFillBackground(False)
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setIconSize(QSize(16, 16))
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setFrame(True)

        self.gridLayout_26.addWidget(self.comboBox_setting_DailyTaskConfig_DevicePlatform, 20, 2, 1, 1)

        self.labelVersion_8 = QLabel(self.page_setting)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        self.labelVersion_8.setMinimumSize(QSize(150, 0))
        self.labelVersion_8.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_8.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_8, 14, 0, 1, 1)

        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege = QComboBox(self.page_setting)
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.addItem("")
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setObjectName(u"comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege")
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setMinimumSize(QSize(150, 0))
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setMaximumSize(QSize(150, 16777215))
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setFont(font1)
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setAutoFillBackground(False)
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setIconSize(QSize(16, 16))
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setFrame(True)

        self.gridLayout_26.addWidget(self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege, 15, 5, 1, 1)

        self.checkBox_setting_DailyTaskConfig_IsShareVideo = QCheckBox(self.page_setting)
        self.checkBox_setting_DailyTaskConfig_IsShareVideo.setObjectName(u"checkBox_setting_DailyTaskConfig_IsShareVideo")
        self.checkBox_setting_DailyTaskConfig_IsShareVideo.setMinimumSize(QSize(150, 0))
        self.checkBox_setting_DailyTaskConfig_IsShareVideo.setMaximumSize(QSize(150, 16777215))
        self.checkBox_setting_DailyTaskConfig_IsShareVideo.setAutoFillBackground(False)
        self.checkBox_setting_DailyTaskConfig_IsShareVideo.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.checkBox_setting_DailyTaskConfig_IsShareVideo, 3, 2, 1, 1)

        self.labelVersion_5 = QLabel(self.page_setting)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        self.labelVersion_5.setMinimumSize(QSize(150, 0))
        self.labelVersion_5.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_5, 5, 0, 1, 1)

        self.labelVersion_6 = QLabel(self.page_setting)
        self.labelVersion_6.setObjectName(u"labelVersion_6")
        self.labelVersion_6.setMinimumSize(QSize(150, 0))
        self.labelVersion_6.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_6.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_6.setLineWidth(1)
        self.labelVersion_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_6, 5, 4, 1, 1)

        self.lineEdit_setting_DailyTaskConfig_CustomComicId = QLineEdit(self.page_setting)
        self.lineEdit_setting_DailyTaskConfig_CustomComicId.setObjectName(u"lineEdit_setting_DailyTaskConfig_CustomComicId")
        self.lineEdit_setting_DailyTaskConfig_CustomComicId.setMinimumSize(QSize(150, 30))
        self.lineEdit_setting_DailyTaskConfig_CustomComicId.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_setting_DailyTaskConfig_CustomComicId.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_26.addWidget(self.lineEdit_setting_DailyTaskConfig_CustomComicId, 19, 2, 1, 1)

        self.labelVersion_16 = QLabel(self.page_setting)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setMinimumSize(QSize(150, 0))
        self.labelVersion_16.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_16.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_16, 15, 0, 1, 1)

        self.lineEdit_setting_DailyTaskConfig_ChargeComment = QLineEdit(self.page_setting)
        self.lineEdit_setting_DailyTaskConfig_ChargeComment.setObjectName(u"lineEdit_setting_DailyTaskConfig_ChargeComment")
        self.lineEdit_setting_DailyTaskConfig_ChargeComment.setMinimumSize(QSize(150, 30))
        self.lineEdit_setting_DailyTaskConfig_ChargeComment.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_setting_DailyTaskConfig_ChargeComment.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_26.addWidget(self.lineEdit_setting_DailyTaskConfig_ChargeComment, 15, 2, 1, 1)

        self.labelVersion_15 = QLabel(self.page_setting)
        self.labelVersion_15.setObjectName(u"labelVersion_15")
        self.labelVersion_15.setMinimumSize(QSize(150, 0))
        self.labelVersion_15.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_15.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_15, 14, 4, 1, 1)

        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6 = QCheckBox(self.page_setting)
        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.setObjectName(u"checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6")
        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.setMinimumSize(QSize(150, 0))
        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.setMaximumSize(QSize(150, 16777215))
        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.setAutoFillBackground(False)
        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6, 3, 4, 1, 1)

        self.labelVersion_25 = QLabel(self.page_setting)
        self.labelVersion_25.setObjectName(u"labelVersion_25")
        self.labelVersion_25.setMinimumSize(QSize(150, 0))
        self.labelVersion_25.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_25.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_25.setLineWidth(1)
        self.labelVersion_25.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_25, 15, 4, 1, 1)

        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins = QLineEdit(self.page_setting)
        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.setObjectName(u"lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins")
        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.setMinimumSize(QSize(150, 30))
        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_26.addWidget(self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins, 5, 5, 1, 1)

        self.labelVersion_setting_3 = QLabel(self.page_setting)
        self.labelVersion_setting_3.setObjectName(u"labelVersion_setting_3")
        self.labelVersion_setting_3.setMinimumSize(QSize(150, 0))
        self.labelVersion_setting_3.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_setting_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_setting_3.setLineWidth(1)
        self.labelVersion_setting_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_setting_3, 18, 0, 1, 15)

        self.labelVersion_30 = QLabel(self.page_setting)
        self.labelVersion_30.setObjectName(u"labelVersion_30")
        self.labelVersion_30.setMinimumSize(QSize(150, 0))
        self.labelVersion_30.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_30.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_30.setLineWidth(1)
        self.labelVersion_30.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_30, 19, 4, 1, 1)

        self.labelVersion_31 = QLabel(self.page_setting)
        self.labelVersion_31.setObjectName(u"labelVersion_31")
        self.labelVersion_31.setMinimumSize(QSize(150, 0))
        self.labelVersion_31.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_31.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_31.setLineWidth(1)
        self.labelVersion_31.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_31, 20, 0, 1, 1)

        self.lineEdit_setting_DailyTaskConfig_CustomEpId = QLineEdit(self.page_setting)
        self.lineEdit_setting_DailyTaskConfig_CustomEpId.setObjectName(u"lineEdit_setting_DailyTaskConfig_CustomEpId")
        self.lineEdit_setting_DailyTaskConfig_CustomEpId.setMinimumSize(QSize(150, 30))
        self.lineEdit_setting_DailyTaskConfig_CustomEpId.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_setting_DailyTaskConfig_CustomEpId.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_26.addWidget(self.lineEdit_setting_DailyTaskConfig_CustomEpId, 19, 5, 1, 1)

        self.comboBox_setting_DailyTaskConfig_NumberOfCoins = QComboBox(self.page_setting)
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.addItem("")
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.addItem("")
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.addItem("")
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setObjectName(u"comboBox_setting_DailyTaskConfig_NumberOfCoins")
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setMinimumSize(QSize(150, 0))
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setMaximumSize(QSize(150, 16777215))
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setFont(font1)
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setAutoFillBackground(False)
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setIconSize(QSize(16, 16))
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setFrame(True)

        self.gridLayout_26.addWidget(self.comboBox_setting_DailyTaskConfig_NumberOfCoins, 5, 2, 1, 1)

        self.labelVersion_26 = QLabel(self.page_setting)
        self.labelVersion_26.setObjectName(u"labelVersion_26")
        self.labelVersion_26.setMinimumSize(QSize(150, 0))
        self.labelVersion_26.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_26.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_26.setLineWidth(1)
        self.labelVersion_26.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_26, 16, 0, 1, 1)

        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle = QCheckBox(self.page_setting)
        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.setObjectName(u"checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle")
        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.setMinimumSize(QSize(150, 0))
        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.setMaximumSize(QSize(150, 16777215))
        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.setAutoFillBackground(False)
        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle, 3, 3, 1, 1)

        self.labelVersion_28 = QLabel(self.page_setting)
        self.labelVersion_28.setObjectName(u"labelVersion_28")
        self.labelVersion_28.setMinimumSize(QSize(150, 0))
        self.labelVersion_28.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_28.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_28.setLineWidth(1)
        self.labelVersion_28.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_28, 19, 0, 1, 1)

        self.pushButton_setting_1 = QPushButton(self.page_setting)
        self.pushButton_setting_1.setObjectName(u"pushButton_setting_1")
        self.pushButton_setting_1.setMinimumSize(QSize(150, 0))
        self.pushButton_setting_1.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_26.addWidget(self.pushButton_setting_1, 21, 10, 1, 1)

        self.pushButton_setting_2 = QPushButton(self.page_setting)
        self.pushButton_setting_2.setObjectName(u"pushButton_setting_2")
        self.pushButton_setting_2.setMinimumSize(QSize(150, 0))
        self.pushButton_setting_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_26.addWidget(self.pushButton_setting_2, 21, 7, 1, 1)

        self.labelVersion_7 = QLabel(self.page_setting)
        self.labelVersion_7.setObjectName(u"labelVersion_7")
        self.labelVersion_7.setMinimumSize(QSize(150, 0))
        self.labelVersion_7.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_7.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_7.setLineWidth(1)
        self.labelVersion_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_7, 7, 0, 1, 1)

        self.lineEdit_setting_DailyTaskConfig_SupportUpIds = QLineEdit(self.page_setting)
        self.lineEdit_setting_DailyTaskConfig_SupportUpIds.setObjectName(u"lineEdit_setting_DailyTaskConfig_SupportUpIds")
        self.lineEdit_setting_DailyTaskConfig_SupportUpIds.setMinimumSize(QSize(150, 30))
        self.lineEdit_setting_DailyTaskConfig_SupportUpIds.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_setting_DailyTaskConfig_SupportUpIds.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_26.addWidget(self.lineEdit_setting_DailyTaskConfig_SupportUpIds, 7, 2, 1, 1)

        self.labelVersion_setting_2 = QLabel(self.page_setting)
        self.labelVersion_setting_2.setObjectName(u"labelVersion_setting_2")
        self.labelVersion_setting_2.setMinimumSize(QSize(150, 0))
        self.labelVersion_setting_2.setMaximumSize(QSize(150, 16777215))
        self.labelVersion_setting_2.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_setting_2.setLineWidth(1)
        self.labelVersion_setting_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelVersion_setting_2, 8, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_setting)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font6);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem57)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.BrushStyle.NoBrush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.BrushStyle.NoBrush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.BrushStyle.NoBrush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette2)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.page_setting_2 = QWidget()
        self.page_setting_2.setObjectName(u"page_setting_2")
        self.stackedWidget.addWidget(self.page_setting_2)
        self.page_cron = QWidget()
        self.page_cron.setObjectName(u"page_cron")
        self.gridLayout_8 = QGridLayout(self.page_cron)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.plainTextEdit_cron = QPlainTextEdit(self.page_cron)
        self.plainTextEdit_cron.setObjectName(u"plainTextEdit_cron")
        self.plainTextEdit_cron.setMinimumSize(QSize(200, 200))
        self.plainTextEdit_cron.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.plainTextEdit_cron.setReadOnly(True)
        self.plainTextEdit_cron.setBackgroundVisible(False)

        self.gridLayout_8.addWidget(self.plainTextEdit_cron, 2, 0, 1, 19)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 3, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_9, 0, 8, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 5, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_18, 3, 13, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_21, 3, 4, 1, 1)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_87, 3, 5, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 3, 8, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_16, 3, 14, 1, 2)

        self.pushButton_cron_1 = QPushButton(self.page_cron)
        self.pushButton_cron_1.setObjectName(u"pushButton_cron_1")
        self.pushButton_cron_1.setMinimumSize(QSize(100, 30))
        self.pushButton_cron_1.setMaximumSize(QSize(100, 30))

        self.gridLayout_8.addWidget(self.pushButton_cron_1, 0, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_15, 3, 12, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_19, 0, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 0, 14, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_43, 0, 12, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_20, 0, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 3, 3, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_17, 3, 11, 1, 1)

        self.pushButton_cron_4 = QPushButton(self.page_cron)
        self.pushButton_cron_4.setObjectName(u"pushButton_cron_4")
        self.pushButton_cron_4.setMinimumSize(QSize(100, 30))
        self.pushButton_cron_4.setMaximumSize(QSize(100, 30))

        self.gridLayout_8.addWidget(self.pushButton_cron_4, 0, 11, 1, 1)

        self.tableWidget_cron = QTableWidget(self.page_cron)
        if (self.tableWidget_cron.columnCount() < 5):
            self.tableWidget_cron.setColumnCount(5)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_cron.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_cron.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_cron.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_cron.setHorizontalHeaderItem(3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_cron.setHorizontalHeaderItem(4, __qtablewidgetitem62)
        if (self.tableWidget_cron.rowCount() < 50):
            self.tableWidget_cron.setRowCount(50)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font6);
        self.tableWidget_cron.setVerticalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_cron.setVerticalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_cron.setVerticalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_cron.setVerticalHeaderItem(3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_cron.setVerticalHeaderItem(4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_cron.setVerticalHeaderItem(5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_cron.setVerticalHeaderItem(6, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_cron.setItem(0, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_cron.setItem(0, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_cron.setItem(0, 2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_cron.setItem(0, 3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_cron.setItem(0, 4, __qtablewidgetitem74)
        self.tableWidget_cron.setObjectName(u"tableWidget_cron")
        sizePolicy3.setHeightForWidth(self.tableWidget_cron.sizePolicy().hasHeightForWidth())
        self.tableWidget_cron.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.BrushStyle.NoBrush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.BrushStyle.NoBrush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush13)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.BrushStyle.NoBrush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush14)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.tableWidget_cron.setPalette(palette3)
        self.tableWidget_cron.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_cron.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_cron.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_cron.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_cron.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_cron.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_cron.setShowGrid(True)
        self.tableWidget_cron.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_cron.setSortingEnabled(False)
        self.tableWidget_cron.setRowCount(50)
        self.tableWidget_cron.horizontalHeader().setVisible(False)
        self.tableWidget_cron.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_cron.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_cron.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_cron.verticalHeader().setVisible(False)
        self.tableWidget_cron.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_cron.verticalHeader().setHighlightSections(False)
        self.tableWidget_cron.verticalHeader().setStretchLastSection(True)

        self.gridLayout_8.addWidget(self.tableWidget_cron, 1, 0, 1, 19)

        self.pushButton_cron_3 = QPushButton(self.page_cron)
        self.pushButton_cron_3.setObjectName(u"pushButton_cron_3")
        self.pushButton_cron_3.setMinimumSize(QSize(100, 30))
        self.pushButton_cron_3.setMaximumSize(QSize(100, 30))

        self.gridLayout_8.addWidget(self.pushButton_cron_3, 0, 13, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 0, 6, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 0, 7, 1, 1)

        self.pushButton_cron_2 = QPushButton(self.page_cron)
        self.pushButton_cron_2.setObjectName(u"pushButton_cron_2")
        self.pushButton_cron_2.setMinimumSize(QSize(100, 30))
        self.pushButton_cron_2.setMaximumSize(QSize(100, 30))

        self.gridLayout_8.addWidget(self.pushButton_cron_2, 3, 6, 1, 1)

        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_88, 3, 7, 1, 1)

        self.stackedWidget.addWidget(self.page_cron)
        self.page_list = QWidget()
        self.page_list.setObjectName(u"page_list")
        self.gridLayout_6 = QGridLayout(self.page_list)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_71, 5, 13, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_54, 1, 3, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_51, 1, 7, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_56, 5, 4, 1, 1)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_55, 5, 3, 1, 1)

        self.pushButton_list_2 = QPushButton(self.page_list)
        self.pushButton_list_2.setObjectName(u"pushButton_list_2")
        self.pushButton_list_2.setMinimumSize(QSize(100, 30))
        self.pushButton_list_2.setMaximumSize(QSize(100, 30))

        self.gridLayout_6.addWidget(self.pushButton_list_2, 1, 12, 1, 1)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_82, 1, 9, 1, 1)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_61, 5, 5, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_58, 1, 6, 1, 1)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_63, 5, 14, 1, 1)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_60, 5, 1, 1, 1)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_81, 5, 6, 1, 1)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_57, 1, 5, 1, 1)

        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_78, 5, 12, 1, 1)

        self.tableWidget_list = QTableWidget(self.page_list)
        if (self.tableWidget_list.columnCount() < 3):
            self.tableWidget_list.setColumnCount(3)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_list.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_list.setHorizontalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_list.setHorizontalHeaderItem(2, __qtablewidgetitem77)
        if (self.tableWidget_list.rowCount() < 15):
            self.tableWidget_list.setRowCount(15)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font6);
        self.tableWidget_list.setVerticalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(4, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(5, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(6, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(7, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(8, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(9, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(10, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(11, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(12, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(13, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_list.setVerticalHeaderItem(14, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_list.setItem(0, 0, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_list.setItem(0, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_list.setItem(0, 2, __qtablewidgetitem95)
        self.tableWidget_list.setObjectName(u"tableWidget_list")
        sizePolicy3.setHeightForWidth(self.tableWidget_list.sizePolicy().hasHeightForWidth())
        self.tableWidget_list.setSizePolicy(sizePolicy3)
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.BrushStyle.NoBrush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush15)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.BrushStyle.NoBrush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush16)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.BrushStyle.NoBrush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush17)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush)
#endif
        self.tableWidget_list.setPalette(palette4)
        self.tableWidget_list.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_list.setShowGrid(True)
        self.tableWidget_list.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_list.setSortingEnabled(False)
        self.tableWidget_list.setWordWrap(True)
        self.tableWidget_list.setRowCount(15)
        self.tableWidget_list.horizontalHeader().setVisible(False)
        self.tableWidget_list.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_list.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_list.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_list.verticalHeader().setVisible(False)
        self.tableWidget_list.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_list.verticalHeader().setHighlightSections(False)
        self.tableWidget_list.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_list, 4, 0, 1, 16)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_53, 1, 10, 1, 1)

        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_79, 5, 10, 1, 1)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_59, 5, 2, 1, 1)

        self.pushButton_list_1 = QPushButton(self.page_list)
        self.pushButton_list_1.setObjectName(u"pushButton_list_1")
        self.pushButton_list_1.setMinimumSize(QSize(100, 30))
        self.pushButton_list_1.setMaximumSize(QSize(100, 30))

        self.gridLayout_6.addWidget(self.pushButton_list_1, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(121, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_80 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_80, 1, 4, 1, 1)

        self.pushButton_next_2 = QPushButton(self.page_list)
        self.pushButton_next_2.setObjectName(u"pushButton_next_2")
        self.pushButton_next_2.setMinimumSize(QSize(100, 30))
        self.pushButton_next_2.setMaximumSize(QSize(100, 30))

        self.gridLayout_6.addWidget(self.pushButton_next_2, 5, 7, 1, 1)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_62, 5, 15, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_52, 5, 9, 1, 1)

        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_84, 5, 8, 1, 1)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_85, 1, 8, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 13, 1, 1)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_83, 1, 14, 1, 1)

        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_86, 1, 15, 1, 1)

        self.stackedWidget.addWidget(self.page_list)
        self.page_cookie_stackedWidget = QWidget()
        self.page_cookie_stackedWidget.setObjectName(u"page_cookie_stackedWidget")
        self.stackedWidget.addWidget(self.page_cookie_stackedWidget)
        self.page_cookie = QWidget()
        self.page_cookie.setObjectName(u"page_cookie")
        self.gridLayout_5 = QGridLayout(self.page_cookie)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_cookie = QTableWidget(self.page_cookie)
        if (self.tableWidget_cookie.columnCount() < 3):
            self.tableWidget_cookie.setColumnCount(3)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_cookie.setHorizontalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_cookie.setHorizontalHeaderItem(1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_cookie.setHorizontalHeaderItem(2, __qtablewidgetitem98)
        if (self.tableWidget_cookie.rowCount() < 50):
            self.tableWidget_cookie.setRowCount(50)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setFont(font6);
        self.tableWidget_cookie.setVerticalHeaderItem(0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_cookie.setVerticalHeaderItem(1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_cookie.setVerticalHeaderItem(2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_cookie.setVerticalHeaderItem(3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_cookie.setVerticalHeaderItem(4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_cookie.setVerticalHeaderItem(5, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_cookie.setVerticalHeaderItem(6, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_cookie.setItem(0, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_cookie.setItem(0, 1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_cookie.setItem(0, 2, __qtablewidgetitem108)
        self.tableWidget_cookie.setObjectName(u"tableWidget_cookie")
        sizePolicy3.setHeightForWidth(self.tableWidget_cookie.sizePolicy().hasHeightForWidth())
        self.tableWidget_cookie.setSizePolicy(sizePolicy3)
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.BrushStyle.NoBrush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush18)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.BrushStyle.NoBrush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush19)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.BrushStyle.NoBrush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush20)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.tableWidget_cookie.setPalette(palette5)
        self.tableWidget_cookie.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_cookie.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_cookie.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_cookie.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_cookie.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_cookie.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_cookie.setShowGrid(True)
        self.tableWidget_cookie.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_cookie.setSortingEnabled(False)
        self.tableWidget_cookie.setRowCount(50)
        self.tableWidget_cookie.horizontalHeader().setVisible(False)
        self.tableWidget_cookie.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_cookie.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_cookie.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_cookie.verticalHeader().setVisible(False)
        self.tableWidget_cookie.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_cookie.verticalHeader().setHighlightSections(False)
        self.tableWidget_cookie.verticalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.tableWidget_cookie, 1, 0, 1, 9)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_40, 0, 3, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_37, 0, 2, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_36, 0, 6, 1, 1)

        self.labelVersion_10 = QLabel(self.page_cookie)
        self.labelVersion_10.setObjectName(u"labelVersion_10")
        self.labelVersion_10.setMinimumSize(QSize(100, 0))
        self.labelVersion_10.setMaximumSize(QSize(100, 16777215))
        self.labelVersion_10.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_10.setLineWidth(1)
        self.labelVersion_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelVersion_10, 0, 0, 1, 1)

        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_90, 0, 8, 1, 1)

        self.pushButton_cookie_1 = QPushButton(self.page_cookie)
        self.pushButton_cookie_1.setObjectName(u"pushButton_cookie_1")
        self.pushButton_cookie_1.setMinimumSize(QSize(100, 30))
        self.pushButton_cookie_1.setMaximumSize(QSize(100, 30))

        self.gridLayout_5.addWidget(self.pushButton_cookie_1, 0, 7, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_39, 0, 5, 1, 1)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_89, 0, 1, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_41, 0, 4, 1, 1)

        self.pushButton_cookie_next = QPushButton(self.page_cookie)
        self.pushButton_cookie_next.setObjectName(u"pushButton_cookie_next")
        self.pushButton_cookie_next.setMinimumSize(QSize(100, 30))
        self.pushButton_cookie_next.setMaximumSize(QSize(100, 30))

        self.gridLayout_5.addWidget(self.pushButton_cookie_next, 2, 4, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_42, 2, 3, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_44, 2, 2, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_45, 2, 1, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_46, 2, 0, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_47, 2, 5, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_48, 2, 6, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_49, 2, 7, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_50, 2, 8, 1, 1)

        self.stackedWidget.addWidget(self.page_cookie)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_4 = QGridLayout(self.page_home)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_98 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_98, 2, 5, 1, 1)

        self.horizontalSpacer_94 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_94, 2, 4, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 4, 3, 1, 1)

        self.pushButton_home_next = QPushButton(self.page_home)
        self.pushButton_home_next.setObjectName(u"pushButton_home_next")
        self.pushButton_home_next.setMinimumSize(QSize(100, 30))
        self.pushButton_home_next.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.pushButton_home_next, 5, 3, 1, 1)

        self.textEdit_home_new = QTextEdit(self.page_home)
        self.textEdit_home_new.setObjectName(u"textEdit_home_new")
        self.textEdit_home_new.setMaximumSize(QSize(120, 200))
        self.textEdit_home_new.setReadOnly(True)

        self.gridLayout_4.addWidget(self.textEdit_home_new, 2, 3, 1, 1)

        self.horizontalSpacer_92 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_92, 2, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 3, 3, 1, 1)

        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_97, 2, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 6, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 0, 3, 1, 1)

        self.horizontalSpacer_91 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_91, 2, 2, 1, 1)

        self.horizontalSpacer_93 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_93, 2, 6, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_home)

        self.gridLayout_10.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u54d4\u54e9\u54e8\u5175", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"github.com/imoki", None))
#if QT_CONFIG(tooltip)
        self.toggleButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u6298\u53e0", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"      \u4e3b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#if QT_CONFIG(tooltip)
        self.btn_cookie.setToolTip(QCoreApplication.translate("MainWindow", u"      cookie", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cookie.setText(QCoreApplication.translate("MainWindow", u"CK\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.btn_list.setToolTip(QCoreApplication.translate("MainWindow", u"      UP\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.btn_list.setText(QCoreApplication.translate("MainWindow", u"UP\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.btn_cron.setToolTip(QCoreApplication.translate("MainWindow", u"      \u5b9a\u65f6\u4efb\u52a1", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cron.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u4efb\u52a1", None))
#if QT_CONFIG(tooltip)
        self.btn_download.setToolTip(QCoreApplication.translate("MainWindow", u"      \u4e0b\u8f7d\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.btn_setting.setToolTip(QCoreApplication.translate("MainWindow", u"      \u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.btn_history.setToolTip(QCoreApplication.translate("MainWindow", u"      \u5386\u53f2\u65e5\u5fd7", None))
#endif // QT_CONFIG(tooltip)
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u65e5\u5fd7", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize_tray.setToolTip(QCoreApplication.translate("MainWindow", u"      \u6700\u5c0f\u5316\u5230\u7cfb\u7edf\u6258\u76d8", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize_tray.setText(QCoreApplication.translate("MainWindow", u"\u6536\u8fdb\u6258\u76d8", None))
#if QT_CONFIG(tooltip)
        self.toggleLeftBox.setToolTip(QCoreApplication.translate("MainWindow", u"      \u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.extraLabel.setText("")
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**\u5173\u4e8e&\u53c2\u8003\u9879\u76ee**\n"
"\n"
"**\u54d4\u54e9\u54e8\u5175\uff0c\u4e00\u6b3e\u76d1\u63a7\u6700\u65b0\u89c6\u9891\u3001\u5b9a\u65f6\u4e0b\u8f7d\u53ca\u6267\u884c\u6bcf\u65e5\u4efb\u52a1\u7684\u8f6f\u4ef6\uff01**\n"
"\n"
"PyDracula\uff1a\n"
"\n"
"[github.com/Wanderson-Magalhaes](https://github.com/Wanderson-Magalhaes)\n"
"\n"
"\u54d4\u54e9\u54d4\u54e9-API\u6536\u96c6\u6574\u7406\uff1a\n"
"\n"
"[github.com/](https://github.com/Wanderson-Magalhaes)\n"
"[SocialSisterYi](https://github.com/SocialSisterYi/bilibili-API-collect)\n"
"\n"
"BiliBilToolPro\uff1a\n"
"\n"
"[github.com/RayWangQvQ](https://github.com/RayWangQvQ/BiliBiliToolPro)\n"
"\n"
"**\u4f5c\u8005\u4ed3\u5e93&\u7559\u8a00**\n"
"\n"
"[github.com/imoki/BiliMonitor](https://github.com/Zhouqluo)\n"
"\n"
"\u5982\u679c\u559c\u6b22\u7684\u8bdd\uff0c\u6b22\u8fce\u5173\u6ce8\u4e00\u952e\u4e09\u8fde\u5440\n"
"\n"
"**\u4ea4\u6d41\u6e20\u9053**\n"
"\n"
"B\u7ad9\uff1a\u65e0\u76d0\u4e03\n"
"\n"
"QQ\u7fa4\uff1a963592267\n"
"\n"
"\u516c\u4f17\u53f7\uff1a"
                        "\u9ed8\u5e93\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700; color:#aa00ff;\">\u5173\u4e8e&amp;\u53c2\u8003\u9879\u76ee</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u54d4\u54e9\u54e8\u5175\uff0c\u4e00\u6b3e\u76d1\u63a7\u6700\u65b0\u89c6"
                        "\u9891\u3001\u5b9a\u65f6\u4e0b\u8f7d\u53ca\u6267\u884c\u6bcf\u65e5\u4efb\u52a1\u7684\u8f6f\u4ef6\uff01</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PyDracula\uff1a</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Wanderson-Magalhaes\"><span style=\" text-decoration: underline; color:#003e92;\">github.com/Wanderson-Magalhaes</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u54d4\u54e9\u54d4\u54e9-API\u6536\u96c6\u6574\u7406\uff1a</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https"
                        "://github.com/Wanderson-Magalhaes\"><span style=\" text-decoration: underline; color:#003e92;\">github.com/</span></a><a href=\"https://github.com/SocialSisterYi/bilibili-API-collect\"><span style=\" text-decoration: underline; color:#003e92;\">SocialSisterYi</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BiliBilToolPro\uff1a</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/RayWangQvQ/BiliBiliToolPro\"><span style=\" text-decoration: underline; color:#003e92;\">github.com/RayWangQvQ</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700; color:#aa00ff;\">\u4f5c\u8005\u4ed3\u5e93&amp;\u7559\u8a00</span></p>\n"
"<p align=\"cente"
                        "r\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Zhouqluo\"><span style=\" text-decoration: underline; color:#003e92;\">github.com/imoki/BiliMonitor</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u5982\u679c\u559c\u6b22\u7684\u8bdd\uff0c\u6b22\u8fce\u5173\u6ce8\u4e00\u952e\u4e09\u8fde\u5440</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700; color:#aa00ff;\">\u4ea4\u6d41\u6e20\u9053</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">B\u7ad9\uff1a\u65e0\u76d0\u4e03</span></p>\n"
"<p "
                        "align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">QQ\u7fa4\uff1a963592267</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u516c\u4f17\u53f7\uff1a\u9ed8\u5e93</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.titleRightInfo.setToolTip(QCoreApplication.translate("MainWindow", u"\u54d4\u54e9\u54e8\u5175", None))
#endif // QT_CONFIG(tooltip)
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u54d4\u54e9\u54e8\u5175", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelVersion_11.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868", None))
        self.pushButton_download_1.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_download_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        ___qtablewidgetitem = self.tableWidget_download.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget_download.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget_download.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget_download.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget_download.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget_download.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget_download.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget_download.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget_download.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget_download.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_download.isSortingEnabled()
        self.tableWidget_download.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.tableWidget_download.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740", None));
        ___qtablewidgetitem11 = self.tableWidget_download.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None));
        ___qtablewidgetitem12 = self.tableWidget_download.item(0, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem13 = self.tableWidget_download.item(0, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None));
        self.tableWidget_download.setSortingEnabled(__sortingEnabled)

        self.labelVersion_9.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u65e5\u5fd7", None))
        ___qtablewidgetitem14 = self.tableWidget_history.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem15 = self.tableWidget_history.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem16 = self.tableWidget_history.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem17 = self.tableWidget_history.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem18 = self.tableWidget_history.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem19 = self.tableWidget_history.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget_history.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget_history.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget_history.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget_history.verticalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget_history.verticalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget_history.verticalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget_history.verticalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget_history.verticalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_history.verticalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_history.isSortingEnabled()
        self.tableWidget_history.setSortingEnabled(False)
        ___qtablewidgetitem29 = self.tableWidget_history.item(0, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem30 = self.tableWidget_history.item(0, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem31 = self.tableWidget_history.item(0, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u540d", None));
        ___qtablewidgetitem32 = self.tableWidget_history.item(0, 3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None));
        ___qtablewidgetitem33 = self.tableWidget_history.item(0, 4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.tableWidget_history.setSortingEnabled(__sortingEnabled1)

        self.pushButton_home_1.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.pushButton_home_2.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_next_1.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.textEdit_home_2.setDocumentTitle("")
        self.textEdit_home_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199UID\uff0c\u53ef\u6dfb\u52a0\u591a\u6b21", None))
        self.textEdit_home_1.setDocumentTitle("")
        self.textEdit_home_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199bilibili\u7684cookie\uff0c\u70b9\u51fb\u786e\u8ba4\u4fdd\u5b58", None))
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.setText("")
        self.lineEdit_setting_DailyTaskConfig_AutoChargeUpId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-1\u8868\u793a\u81ea\u5df1", None))
        self.checkBox_setting_DailyTaskConfig_IsWatchVideo.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u89c2\u770b\u89c6\u9891", None))
        self.checkBox_setting_DailyTaskConfig_SelectLike.setText(QCoreApplication.translate("MainWindow", u"\u6295\u5e01\u65f6\u540c\u65f6\u70b9\u8d5e", None))
        self.labelVersion_setting_1.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u65e5\u57fa\u7840\u4efb\u52a1\u8bbe\u7f6e\uff1a", None))
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_setting_DailyTaskConfig_DayOfAutoCharge.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_setting_DailyTaskConfig_DayOfExchangeSilver2Coin.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_setting_DailyTaskConfig_DevicePlatform.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.labelVersion_8.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5145\u7535", None))
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_setting_DailyTaskConfig_DayOfReceiveVipPrivilege.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.checkBox_setting_DailyTaskConfig_IsShareVideo.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5206\u4eab\u89c6\u9891", None))
        self.labelVersion_5.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u65e5\u6295\u5e01\u6570", None))
        self.labelVersion_6.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7559\u786c\u5e01\u6570", None))
        self.lineEdit_setting_DailyTaskConfig_CustomComicId.setText("")
        self.lineEdit_setting_DailyTaskConfig_CustomComicId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u82e5\u4e0d\u6e05\u695a\u542b\u4e49\u52ff\u6539", None))
        self.labelVersion_16.setText(QCoreApplication.translate("MainWindow", u"\u5145\u7535\u540e\u7559\u8a00", None))
        self.lineEdit_setting_DailyTaskConfig_ChargeComment.setText("")
        self.lineEdit_setting_DailyTaskConfig_ChargeComment.setPlaceholderText("")
        self.labelVersion_15.setText(QCoreApplication.translate("MainWindow", u"\u5145\u7535\u6307\u5b9aup\u4e3bID", None))
        self.checkBox_setting_DailyTaskConfig_SaveCoinsWhenLv6.setText(QCoreApplication.translate("MainWindow", u" Lv6\u786c\u5e01\u767d\u5ad6\u6a21\u5f0f", None))
        self.labelVersion_25.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u9886\u53d6\u4f1a\u5458\u6743\u76ca", None))
        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.setText("")
        self.lineEdit_setting_DailyTaskConfig_NumberOfProtectedCoins.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0 \u4e3a\u4e0d\u4fdd\u7559", None))
        self.labelVersion_setting_3.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a\u81ea\u5b9a\u4e49\uff1a", None))
        self.labelVersion_30.setText(QCoreApplication.translate("MainWindow", u"\u6f2b\u753b\u9605\u8bfbep_id", None))
        self.labelVersion_31.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u7aef\u64cd\u4f5c\u5e73\u53f0", None))
        self.lineEdit_setting_DailyTaskConfig_CustomEpId.setText("")
        self.lineEdit_setting_DailyTaskConfig_CustomEpId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u82e5\u4e0d\u6e05\u695a\u542b\u4e49\u52ff\u6539", None))
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_setting_DailyTaskConfig_NumberOfCoins.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.labelVersion_26.setText(QCoreApplication.translate("MainWindow", u"\u94f6\u74dc\u5b50\u5151\u6362\u786c\u5e01", None))
        self.checkBox_setting_DailyTaskConfig_IsDonateCoinForArticle.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u4e13\u680f\u6295\u5e01", None))
        self.labelVersion_28.setText(QCoreApplication.translate("MainWindow", u"\u6f2b\u753b\u9605\u8bfbcomic_id", None))
        self.pushButton_setting_1.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.pushButton_setting_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.labelVersion_7.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u652f\u6301up\u4e3bID", None))
        self.lineEdit_setting_DailyTaskConfig_SupportUpIds.setText("")
        self.lineEdit_setting_DailyTaskConfig_SupportUpIds.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5982\uff1a123,456", None))
        self.labelVersion_setting_2.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u6708\u51e0\u53f7\u6267\u884c\u8bbe\u7f6e\uff1a", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem34 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem35 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem36 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem37 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem38 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem43 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem44 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem45 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem48 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem53 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem54 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem55 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem56 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem57 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.plainTextEdit_cron.setPlainText("")
        self.plainTextEdit_cron.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u8fd0\u884c\u65e5\u5fd7", None))
        self.pushButton_cron_1.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b9a\u65f6", None))
        self.pushButton_cron_4.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u4efb\u52a1", None))
        ___qtablewidgetitem58 = self.tableWidget_cron.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem59 = self.tableWidget_cron.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem60 = self.tableWidget_cron.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem61 = self.tableWidget_cron.horizontalHeaderItem(3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem62 = self.tableWidget_cron.horizontalHeaderItem(4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem63 = self.tableWidget_cron.verticalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem64 = self.tableWidget_cron.verticalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem65 = self.tableWidget_cron.verticalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem66 = self.tableWidget_cron.verticalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem67 = self.tableWidget_cron.verticalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem68 = self.tableWidget_cron.verticalHeaderItem(5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem69 = self.tableWidget_cron.verticalHeaderItem(6)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.tableWidget_cron.isSortingEnabled()
        self.tableWidget_cron.setSortingEnabled(False)
        ___qtablewidgetitem70 = self.tableWidget_cron.item(0, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u540d", None));
        ___qtablewidgetitem71 = self.tableWidget_cron.item(0, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u65f6\u95f4", None));
        ___qtablewidgetitem72 = self.tableWidget_cron.item(0, 2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem73 = self.tableWidget_cron.item(0, 3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None));
        ___qtablewidgetitem74 = self.tableWidget_cron.item(0, 4)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.tableWidget_cron.setSortingEnabled(__sortingEnabled3)

        self.pushButton_cron_3.setText(QCoreApplication.translate("MainWindow", u"\u7acb\u5373\u8fd0\u884c", None))
        self.pushButton_cron_2.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210", None))
        self.pushButton_list_2.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5168\u4fe1\u606f", None))
        ___qtablewidgetitem75 = self.tableWidget_list.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem76 = self.tableWidget_list.horizontalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem77 = self.tableWidget_list.horizontalHeaderItem(2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem78 = self.tableWidget_list.verticalHeaderItem(0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem79 = self.tableWidget_list.verticalHeaderItem(1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem80 = self.tableWidget_list.verticalHeaderItem(2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem81 = self.tableWidget_list.verticalHeaderItem(3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem82 = self.tableWidget_list.verticalHeaderItem(4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem83 = self.tableWidget_list.verticalHeaderItem(5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem84 = self.tableWidget_list.verticalHeaderItem(6)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem85 = self.tableWidget_list.verticalHeaderItem(7)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem86 = self.tableWidget_list.verticalHeaderItem(8)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem87 = self.tableWidget_list.verticalHeaderItem(9)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem88 = self.tableWidget_list.verticalHeaderItem(10)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem89 = self.tableWidget_list.verticalHeaderItem(11)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem90 = self.tableWidget_list.verticalHeaderItem(12)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem91 = self.tableWidget_list.verticalHeaderItem(13)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem92 = self.tableWidget_list.verticalHeaderItem(14)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.tableWidget_list.isSortingEnabled()
        self.tableWidget_list.setSortingEnabled(False)
        ___qtablewidgetitem93 = self.tableWidget_list.item(0, 0)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"UP\u7a7a\u95f4ID", None));
        ___qtablewidgetitem94 = self.tableWidget_list.item(0, 1)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem95 = self.tableWidget_list.item(0, 2)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.tableWidget_list.setSortingEnabled(__sortingEnabled4)

        self.pushButton_list_1.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_next_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        ___qtablewidgetitem96 = self.tableWidget_cookie.horizontalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem97 = self.tableWidget_cookie.horizontalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem98 = self.tableWidget_cookie.horizontalHeaderItem(2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem99 = self.tableWidget_cookie.verticalHeaderItem(0)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem100 = self.tableWidget_cookie.verticalHeaderItem(1)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem101 = self.tableWidget_cookie.verticalHeaderItem(2)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem102 = self.tableWidget_cookie.verticalHeaderItem(3)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem103 = self.tableWidget_cookie.verticalHeaderItem(4)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem104 = self.tableWidget_cookie.verticalHeaderItem(5)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem105 = self.tableWidget_cookie.verticalHeaderItem(6)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled5 = self.tableWidget_cookie.isSortingEnabled()
        self.tableWidget_cookie.setSortingEnabled(False)
        ___qtablewidgetitem106 = self.tableWidget_cookie.item(0, 0)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"\u6635\u79f0", None));
        ___qtablewidgetitem107 = self.tableWidget_cookie.item(0, 1)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"cookie", None));
        ___qtablewidgetitem108 = self.tableWidget_cookie.item(0, 2)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.tableWidget_cookie.setSortingEnabled(__sortingEnabled5)

        self.labelVersion_10.setText(QCoreApplication.translate("MainWindow", u"CK\u5217\u8868", None))
        self.pushButton_cookie_1.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_cookie_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.pushButton_home_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.textEdit_home_new.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">\u54d4\u54e9\u54e8\u5175</span></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \u65e0\u76d0\u4e03", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v5.7.0", None))
    # retranslateUi

