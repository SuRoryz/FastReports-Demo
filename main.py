import sys
import base64
import time

from views.mainwindow import Ui_MainWindow

from API import API


from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

from utilWindows import *
from worker import Worker, WorkerSignals
from utils import *

from users import *
from groups import *
from data_sources import *
from documents import *
from tasks import *

from threading import Thread
from functools import partial

KEY = "e8xau6dh13h5sa1kz3cpp5tue38oat3f5mcddh49nuism9cgn38y"
KEY_B64 = base64.b64encode(f"apikey:{KEY}".encode()).decode()

class App(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.widget = Wind()

        self.WindowPlaceholder.layout().addWidget(self.widget)

        self.NavbarTemplates.clicked.connect(lambda: self.widget.run_in_thread(lambda: self.widget.load_window(window_="templates"), self.widget.apply_data_to_list))
        self.NavbarReports.clicked.connect(lambda: self.widget.run_in_thread(lambda: self.widget.load_window(window_="reports"), self.widget.apply_data_to_list))
        self.NavbarExports.clicked.connect(lambda: self.widget.run_in_thread(lambda: self.widget.load_window(window_="exports"), self.widget.apply_data_to_list))

        self.NavbarDocuments.clicked.connect(lambda: self.changeWindow(Wind()))
        self.NavbarDatasources.clicked.connect(lambda: self.changeWindow(Wind_Datasources()))
        self.NavbarTasks.clicked.connect(lambda: self.changeWindow(Wind_Task()))
        self.NavbarGroups.clicked.connect(lambda: self.changeWindow(Wind_Group()))
        self.NavbarUsers.clicked.connect(lambda: self.changeWindow(Wind_Users()))
    
    def changeWindow(self, w):
        widget_ = self.WindowPlaceholder.layout().takeAt(0).widget()
        widget_.deleteLater()

        self.widget = w
        self.WindowPlaceholder.layout().addWidget(w)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    API_INSTANCE = API(KEY_B64)

    mainApp = App()
    mainApp.show()
    sys.exit(app.exec_())