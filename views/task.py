# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasks.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(987, 665)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Inpu = QWidget(self.groupBox)
        self.Inpu.setObjectName(u"Inpu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Inpu.sizePolicy().hasHeightForWidth())
        self.Inpu.setSizePolicy(sizePolicy)
        self.InputFileName = QLabel(self.Inpu)
        self.InputFileName.setObjectName(u"InputFileName")
        self.InputFileName.setGeometry(QRect(350, 40, 47, 13))

        self.horizontalLayout.addWidget(self.Inpu)

        self.InputBtn = QPushButton(self.groupBox)
        self.InputBtn.setObjectName(u"InputBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.InputBtn.sizePolicy().hasHeightForWidth())
        self.InputBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.InputBtn)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.InputFolderName = QLabel(self.groupBox_8)
        self.InputFolderName.setObjectName(u"InputFolderName")

        self.horizontalLayout_4.addWidget(self.InputFolderName, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.InputFileNameName = QLabel(self.groupBox_7)
        self.InputFileNameName.setObjectName(u"InputFileNameName")

        self.horizontalLayout_3.addWidget(self.InputFileNameName, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.groupBox_7)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.OutputFolderBtn = QPushButton(self.groupBox_6)
        self.OutputFolderBtn.setObjectName(u"OutputFolderBtn")

        self.verticalLayout_3.addWidget(self.OutputFolderBtn)

        self.OutputNameBtn = QPushButton(self.groupBox_6)
        self.OutputNameBtn.setObjectName(u"OutputNameBtn")

        self.verticalLayout_3.addWidget(self.OutputNameBtn)


        self.horizontalLayout_2.addWidget(self.groupBox_6)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.InputFileFormat = QLabel(self.groupBox_3)
        self.InputFileFormat.setObjectName(u"InputFileFormat")
        sizePolicy.setHeightForWidth(self.InputFileFormat.sizePolicy().hasHeightForWidth())
        self.InputFileFormat.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.InputFileFormat, 0, Qt.AlignHCenter)

        self.FormatBtn = QPushButton(self.groupBox_3)
        self.FormatBtn.setObjectName(u"FormatBtn")
        sizePolicy1.setHeightForWidth(self.FormatBtn.sizePolicy().hasHeightForWidth())
        self.FormatBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.FormatBtn)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scrollArea = QScrollArea(self.groupBox_4)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 784, 69))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox_9)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.groupBox_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.groupBox_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.ParamAddBtn = QPushButton(self.groupBox_4)
        self.ParamAddBtn.setObjectName(u"ParamAddBtn")
        sizePolicy1.setHeightForWidth(self.ParamAddBtn.sizePolicy().hasHeightForWidth())
        self.ParamAddBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.ParamAddBtn)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_10 = QGroupBox(Form)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.TaskName = QLabel(self.groupBox_11)
        self.TaskName.setObjectName(u"TaskName")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.TaskName.sizePolicy().hasHeightForWidth())
        self.TaskName.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.TaskName)

        self.pushButton = QPushButton(self.groupBox_11)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.horizontalLayout_8.addWidget(self.groupBox_11)

        self.save = QPushButton(self.groupBox_10)
        self.save.setObjectName(u"save")
        sizePolicy1.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.save)


        self.verticalLayout.addWidget(self.groupBox_10)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.InputFileName.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.InputBtn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Groupox", None))
        self.groupBox_5.setTitle("")
        self.groupBox_8.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"Folder", None))
        self.InputFolderName.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_7.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Filename", None))
        self.InputFileNameName.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_6.setTitle("")
        self.OutputFolderBtn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.OutputNameBtn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.InputFileFormat.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.FormatBtn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Key", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Value", None))
        self.ParamAddBtn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.groupBox_10.setTitle("")
        self.groupBox_11.setTitle("")
        self.TaskName.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

