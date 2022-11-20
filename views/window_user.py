# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_user.ui'
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
        Form.resize(475, 239)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.ID = QLabel(self.groupBox_2)
        self.ID.setObjectName(u"ID")

        self.horizontalLayout_3.addWidget(self.ID)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.Name = QLabel(self.groupBox_3)
        self.Name.setObjectName(u"Name")

        self.horizontalLayout_4.addWidget(self.Name)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.Username = QLabel(self.groupBox_4)
        self.Username.setObjectName(u"Username")

        self.horizontalLayout.addWidget(self.Username)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.Email = QLabel(self.groupBox_5)
        self.Email.setObjectName(u"Email")

        self.horizontalLayout_2.addWidget(self.Email)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.save = QPushButton(self.groupBox)
        self.save.setObjectName(u"save")

        self.verticalLayout_2.addWidget(self.save)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"ID:", None))
        self.ID.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.Name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_4.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.Username.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_5.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.Email.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.save.setText(QCoreApplication.translate("Form", u"Ok", None))
    # retranslateUi

