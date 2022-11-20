# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1345, 779)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: white\n"
"}\n"
"\n"
"QWidget QPushButton {\n"
"	border: 2px solid aqua;\n"
"	outline: none;\n"
"	padding: 5px 0;\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QWidget QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255)\n"
"}")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.centralwidget.setStyleSheet(u"QWidget QGroupBox {\n"
"border: none;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Navbar = QGroupBox(self.centralwidget)
        self.Navbar.setObjectName(u"Navbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Navbar.sizePolicy().hasHeightForWidth())
        self.Navbar.setSizePolicy(sizePolicy1)
        self.Navbar.setMinimumSize(QSize(200, 0))
        self.Navbar.setBaseSize(QSize(500, 3))
        self.Navbar.setStyleSheet(u"QWidget#Navbar {\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 30px;\n"
"	\n"
"	font: 12pt \"Century Gothic\";\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.Navbar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.Navbar)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.NavbarDocuments = QPushButton(self.groupBox_2)
        self.NavbarDocuments.setObjectName(u"NavbarDocuments")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.NavbarDocuments.sizePolicy().hasHeightForWidth())
        self.NavbarDocuments.setSizePolicy(sizePolicy2)
        self.NavbarDocuments.setMinimumSize(QSize(70, 0))

        self.verticalLayout_4.addWidget(self.NavbarDocuments)

        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.NavbarTemplates = QPushButton(self.groupBox_7)
        self.NavbarTemplates.setObjectName(u"NavbarTemplates")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.NavbarTemplates.sizePolicy().hasHeightForWidth())
        self.NavbarTemplates.setSizePolicy(sizePolicy3)
        self.NavbarTemplates.setMinimumSize(QSize(70, 0))
        self.NavbarTemplates.setStyleSheet(u"font-size: 8pt")

        self.horizontalLayout_8.addWidget(self.NavbarTemplates, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.NavbarReports = QPushButton(self.groupBox_8)
        self.NavbarReports.setObjectName(u"NavbarReports")
        sizePolicy3.setHeightForWidth(self.NavbarReports.sizePolicy().hasHeightForWidth())
        self.NavbarReports.setSizePolicy(sizePolicy3)
        self.NavbarReports.setMinimumSize(QSize(70, 0))
        self.NavbarReports.setStyleSheet(u"font-size: 8pt")

        self.horizontalLayout_10.addWidget(self.NavbarReports, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.NavbarExports = QPushButton(self.groupBox_9)
        self.NavbarExports.setObjectName(u"NavbarExports")
        sizePolicy3.setHeightForWidth(self.NavbarExports.sizePolicy().hasHeightForWidth())
        self.NavbarExports.setSizePolicy(sizePolicy3)
        self.NavbarExports.setMinimumSize(QSize(70, 0))
        self.NavbarExports.setStyleSheet(u"font-size: 8pt")

        self.horizontalLayout_9.addWidget(self.NavbarExports, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.groupBox_9)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.Navbar)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.NavbarDatasources = QPushButton(self.groupBox_3)
        self.NavbarDatasources.setObjectName(u"NavbarDatasources")
        sizePolicy3.setHeightForWidth(self.NavbarDatasources.sizePolicy().hasHeightForWidth())
        self.NavbarDatasources.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.NavbarDatasources)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.Navbar)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.NavbarGroups = QPushButton(self.groupBox_4)
        self.NavbarGroups.setObjectName(u"NavbarGroups")
        sizePolicy3.setHeightForWidth(self.NavbarGroups.sizePolicy().hasHeightForWidth())
        self.NavbarGroups.setSizePolicy(sizePolicy3)

        self.horizontalLayout_12.addWidget(self.NavbarGroups)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.Navbar)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.NavbarUsers = QPushButton(self.groupBox_5)
        self.NavbarUsers.setObjectName(u"NavbarUsers")
        sizePolicy3.setHeightForWidth(self.NavbarUsers.sizePolicy().hasHeightForWidth())
        self.NavbarUsers.setSizePolicy(sizePolicy3)

        self.horizontalLayout_13.addWidget(self.NavbarUsers)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.Navbar)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.NavbarTasks = QPushButton(self.groupBox_6)
        self.NavbarTasks.setObjectName(u"NavbarTasks")
        sizePolicy3.setHeightForWidth(self.NavbarTasks.sizePolicy().hasHeightForWidth())
        self.NavbarTasks.setSizePolicy(sizePolicy3)

        self.horizontalLayout_14.addWidget(self.NavbarTasks)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.groupBox_10 = QGroupBox(self.Navbar)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_9 = QPushButton(self.groupBox_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.pushButton_9)


        self.verticalLayout.addWidget(self.groupBox_10)


        self.horizontalLayout_7.addWidget(self.Navbar, 0, Qt.AlignVCenter)

        self.WindowPlaceholder = QWidget(self.centralwidget)
        self.WindowPlaceholder.setObjectName(u"WindowPlaceholder")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.WindowPlaceholder.sizePolicy().hasHeightForWidth())
        self.WindowPlaceholder.setSizePolicy(sizePolicy4)
        self.WindowPlaceholder.setStyleSheet(u"QWidget#WindowPlaceholder {\n"
"	border-left: 2px solid aqua\n"
"}\n"
"\n"
"QWidget#MainHeader {\n"
"	color: rgb(192, 209, 208)\n"
"}\n"
"\n"
"QWidget#MainBodyHeader {\n"
"	border-top: 2px solid aqua;\n"
"	font: 8pt \"Century Gothic\";\n"
"}\n"
"\n"
"QWidget#MainBodyHeaderBody {\n"
"	font: 8pt \"Century Gothic\";\n"
"}\n"
"\n"
"QWidget QScrollArea {\n"
"border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {   \n"
"    background-color: rgb(170, 255, 255);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover { \n"
"    background-color: rgb(0, 255, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {   \n"
"    background-color:  rgb(0, 255, 255);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(202, 255, 252);\n"
"    height: 15px;\n"
""
                        "    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {   \n"
"    background-color: rgb(202, 255, 252);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed { \n"
"    background-color: rgb(202, 255, 252);\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(202, 255, 252);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {   \n"
"    background-color: rgb(202, 255, 252);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed { \n"
"    background-color: rgb(202, 255, 252);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"    \n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    backgr"
                        "ound: none;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.WindowPlaceholder)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_7.addWidget(self.WindowPlaceholder)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Navbar.setTitle("")
        self.groupBox_2.setTitle("")
        self.NavbarDocuments.setText(QCoreApplication.translate("MainWindow", u"Documents", None))
        self.groupBox_7.setTitle("")
        self.NavbarTemplates.setText(QCoreApplication.translate("MainWindow", u"Templates", None))
        self.groupBox_8.setTitle("")
        self.NavbarReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.groupBox_9.setTitle("")
        self.NavbarExports.setText(QCoreApplication.translate("MainWindow", u"Exports", None))
        self.groupBox_3.setTitle("")
        self.NavbarDatasources.setText(QCoreApplication.translate("MainWindow", u"Data Sources", None))
        self.groupBox_4.setTitle("")
        self.NavbarGroups.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.groupBox_5.setTitle("")
        self.NavbarUsers.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.groupBox_6.setTitle("")
        self.NavbarTasks.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.groupBox_10.setTitle("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"API Keys", None))
    # retranslateUi

