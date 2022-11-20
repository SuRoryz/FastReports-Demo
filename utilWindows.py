from views.textedit import Ui_Form as te
from views.group_users import Ui_Form as gu
from views.window_user import Ui_Form as wd_uu
from views.task import Ui_Form as t

from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

from utilWindows import *
from worker import Worker, WorkerSignals
from utils import *

from API import API

class TextEditWindow(QWidget, te):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class UserWindow(QWidget, wd_uu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class GroupUsersEditWindow(QWidget, gu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.users_in = []
        self.lables = []
    
    def completeWindow(self, users, users_out):
        users = users["users"]

        for user in users:
            user_label = QLabel(user["userId"])
            user_label.mouseDoubleClickEvent = lambda x: self.transerUser(to="out", user=user_label)

            self.users_in.append(user["userId"])
            self.lables.append(user_label)

            self.inGroup.layout().addWidget(user_label)
        
        for user in users_out["users"]:
            u = user["userId"]

            if u in self.users_in:
                continue

            user_label = QLabel(user["userId"])
            user_label.mouseDoubleClickEvent = lambda x: self.transerUser(to="in", user=user_label)

            self.lables.append(user_label)

            self.outGroup.layout().addWidget(user_label)
    
    def transerUser(self, to, user):
            if to == "out":
                new_user = QLabel(user.text())

                try:
                    self.users_in.remove(user)
                except:
                    pass

                self.inGroup.layout().removeWidget(user)
                self.inGroup.adjustSize() 
                user.deleteLater()

                new_user.mouseDoubleClickEvent = lambda x: self.transerUser(to="in", user=new_user)

                self.lables.append(new_user)
                self.users_in.append(new_user)

                self.outGroup.layout().addWidget(new_user)
    
            if to == "in":
                new_user = QLabel(user.text())

                self.outGroup.layout().removeWidget(user)
                self.outGroup.adjustSize() 
                user.deleteLater()

                new_user.mouseDoubleClickEvent = lambda x: self.transerUser(to="out", user=new_user)

                self.lables.append(new_user)
                self.users_in.append(new_user)

                self.inGroup.layout().addWidget(new_user)


class TaskEditWindow(QWidget, t):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.withInp = False
        self.withOut = False
    
    def actionInputBtn(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 'New file: ')
        self.InputFileName.setText(name)
    
    def actionOutputFolderBtn(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 'Output folder: ')
        self.InputFolderName.setText(name)

    def actionOutputNameBtn(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 'Output file name: ')
        self.InputFileNameName.setText(name)
    
    def actionChangeName(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 'New task name: ')
        self.TaskName.setText(name)
    
    def actionChangeFormat(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 'New format: ')
        self.InputFileFormat.setText(name)

    def completeWindow(self, taskObj):
        if "inputFile" in taskObj:
            self.InputFileName.setText(taskObj["inputFile"]["fileName"])

            self.withInp = True
        if "outputFile" in taskObj:
            self.InputFolderName.setText(taskObj["outputFile"]["folderId"])
            self.InputFileNameName.setText(taskObj["outputFile"]["fileName"])

            self.withOut = True

        self.InputFileFormat.setText(taskObj["format"])
        self.TaskName.setText(taskObj["name"])

        self.FormatBtn.clicked.connect(self.actionChangeFormat)
        self.InputBtn.clicked.connect(self.actionInputBtn)
        self.OutputFolderBtn.clicked.connect(self.actionOutputFolderBtn)
        self.OutputNameBtn.clicked.connect(self.actionOutputNameBtn)
        self.pushButton.clicked.connect(self.actionChangeName)