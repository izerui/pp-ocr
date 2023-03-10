# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reader.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QListView, QMainWindow, QMenuBar, QScrollArea,
    QSizePolicy, QSplitter, QStatusBar, QTabWidget,
    QTextBrowser, QToolBar, QWidget)

from controller.component import ImageLabel
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.openFileAction = QAction(MainWindow)
        self.openFileAction.setObjectName(u"openFileAction")
        icon = QIcon()
        icon.addFile(u":/logo/logo/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFileAction.setIcon(icon)
        self.ocrAction = QAction(MainWindow)
        self.ocrAction.setObjectName(u"ocrAction")
        icon1 = QIcon()
        icon1.addFile(u":/logo/logo/ocr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ocrAction.setIcon(icon1)
        self.largeAction = QAction(MainWindow)
        self.largeAction.setObjectName(u"largeAction")
        icon2 = QIcon()
        icon2.addFile(u":/logo/logo/large.png", QSize(), QIcon.Normal, QIcon.Off)
        self.largeAction.setIcon(icon2)
        self.smallAction = QAction(MainWindow)
        self.smallAction.setObjectName(u"smallAction")
        icon3 = QIcon()
        icon3.addFile(u":/logo/logo/small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.smallAction.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView = QListView(self.tab)
        self.listView.setObjectName(u"listView")
        self.listView.setMaximumSize(QSize(130, 16777215))
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_2.addWidget(self.listView)

        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.widget_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.scrollArea = QScrollArea(self.splitter_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 588, 73))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = ImageLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter_2.addWidget(self.scrollArea)
        self.textBrowser = QTextBrowser(self.splitter_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 400))
        self.splitter_2.addWidget(self.textBrowser)

        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menubar.setSizeIncrement(QSize(0, 0))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.openFileAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.largeAction)
        self.toolBar.addAction(self.smallAction)

        self.retranslateUi(MainWindow)
        self.toolBar.actionTriggered.connect(MainWindow.actionTriggered)
        self.listView.clicked.connect(MainWindow.pageClicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u6587\u5b57\u8bc6\u522b\u7a0b\u5e8f", None))
        self.openFileAction.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.openFileAction.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.ocrAction.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.largeAction.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5927", None))
        self.smallAction.setText(QCoreApplication.translate("MainWindow", u"\u7f29\u5c0f", None))
#if QT_CONFIG(tooltip)
        self.smallAction.setToolTip(QCoreApplication.translate("MainWindow", u"\u7f29\u5c0f", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

