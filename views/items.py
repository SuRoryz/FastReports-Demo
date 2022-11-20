# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'items.ui'
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
        MainWindow.resize(1280, 740)
        MainWindow.setStyleSheet(u"background-color: white")
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainHeader = QGroupBox(self.centralwidget)
        self.MainHeader.setObjectName(u"MainHeader")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainHeader.sizePolicy().hasHeightForWidth())
        self.MainHeader.setSizePolicy(sizePolicy1)
        self.MainHeader.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.MainHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainHeaderUtils = QGroupBox(self.MainHeader)
        self.MainHeaderUtils.setObjectName(u"MainHeaderUtils")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MainHeaderUtils.sizePolicy().hasHeightForWidth())
        self.MainHeaderUtils.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.MainHeaderUtils)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.AddBtnWrapper = QGroupBox(self.MainHeaderUtils)
        self.AddBtnWrapper.setObjectName(u"AddBtnWrapper")
        self.AddBtnWrapper.setStyleSheet(u"position: fixed;\n"
"")
        self.AddBtnWrapper.setFlat(False)
        self.AddBtnLayout = QGridLayout(self.AddBtnWrapper)
        self.AddBtnLayout.setObjectName(u"AddBtnLayout")
        self.AddBtnLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.widget = QWidget(self.AddBtnWrapper)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")

        self.AddBtnLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.AddBtnWrapper, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.MainHeaderUtils)


        self.verticalLayout.addWidget(self.MainHeader)

        self.MainBody = QGroupBox(self.centralwidget)
        self.MainBody.setObjectName(u"MainBody")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.MainBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.MainBodyHeader = QGroupBox(self.MainBody)
        self.MainBodyHeader.setObjectName(u"MainBodyHeader")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.MainBodyHeader.sizePolicy().hasHeightForWidth())
        self.MainBodyHeader.setSizePolicy(sizePolicy4)
        self.MainBodyHeader.setMinimumSize(QSize(0, 60))
        self.MainBodyHeader.setBaseSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.MainBodyHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MainBodyHeaderSelected = QGroupBox(self.MainBodyHeader)
        self.MainBodyHeaderSelected.setObjectName(u"MainBodyHeaderSelected")

        self.horizontalLayout_2.addWidget(self.MainBodyHeaderSelected)

        self.MainBodyHeaderBody = QGroupBox(self.MainBodyHeader)
        self.MainBodyHeaderBody.setObjectName(u"MainBodyHeaderBody")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(70)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.MainBodyHeaderBody.sizePolicy().hasHeightForWidth())
        self.MainBodyHeaderBody.setSizePolicy(sizePolicy5)
        self.MainBodyHeaderBody.setStyleSheet(u"font-size: 20px")
        self.MainBodyHeaderBody.setFlat(False)
        self.horizontalLayout_4 = QHBoxLayout(self.MainBodyHeaderBody)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.MainBodyHeaderBody)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.MainBodyHeaderBody)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.MainBodyHeaderBody)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"f")
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.MainBodyHeaderBody)


        self.verticalLayout_2.addWidget(self.MainBodyHeader)

        self.MainBodyBody = QGroupBox(self.MainBody)
        self.MainBodyBody.setObjectName(u"MainBodyBody")
        sizePolicy3.setHeightForWidth(self.MainBodyBody.sizePolicy().hasHeightForWidth())
        self.MainBodyBody.setSizePolicy(sizePolicy3)
        self.MainBodyBody.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.MainBodyBody)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.MainBodyBodySelected = QGroupBox(self.MainBodyBody)
        self.MainBodyBodySelected.setObjectName(u"MainBodyBodySelected")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.MainBodyBodySelected.sizePolicy().hasHeightForWidth())
        self.MainBodyBodySelected.setSizePolicy(sizePolicy7)

        self.horizontalLayout_3.addWidget(self.MainBodyBodySelected)

        self.MainBodyItems = QGroupBox(self.MainBodyBody)
        self.MainBodyItems.setObjectName(u"MainBodyItems")
        sizePolicy5.setHeightForWidth(self.MainBodyItems.sizePolicy().hasHeightForWidth())
        self.MainBodyItems.setSizePolicy(sizePolicy5)
        self.MainBodyItems.setStyleSheet(u"font-size: 20px")
        self.MainBodyItemsLayout = QVBoxLayout(self.MainBodyItems)
        self.MainBodyItemsLayout.setObjectName(u"MainBodyItemsLayout")
        self.groupBox = QGroupBox(self.MainBodyItems)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.MainBodyItemsLayout.addWidget(self.groupBox)


        self.horizontalLayout_3.addWidget(self.MainBodyItems, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.MainBodyBody)


        self.verticalLayout.addWidget(self.MainBody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainHeader.setTitle("")
        self.MainHeaderUtils.setTitle("")
        self.AddBtnWrapper.setTitle("")
        self.MainBody.setTitle("")
        self.MainBodyHeader.setTitle("")
        self.MainBodyHeaderSelected.setTitle("")
        self.MainBodyHeaderBody.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Update", None))
        self.MainBodyBody.setTitle("")
        self.MainBodyBodySelected.setTitle("")
        self.MainBodyItems.setTitle("")
        self.groupBox.setTitle("")
    # retranslateUi

