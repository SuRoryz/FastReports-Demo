from views.window_users import Ui_Form as wd_u

from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

from utilWindows import *
from worker import Worker, WorkerSignals
from utils import *

from API import API

class Wind_Users(QWidget, wd_u):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threadpool = QThreadPool()

        self.subs = API_INSTANCE.get_subscriptions()
        self.users = []

        self.run_in_thread(self.load_window, lambda data: self.run_in_thread(self.apply_data_to_list(data), lambda x: x))
    
    def load_window(self):
        result = []

        sources = API_INSTANCE.get_users(self.subs["subscriptions"][0]["id"], take=120)
        for source in sources["users"]:
            result.append(source)

        return result
    
    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)
    
    def apply_data_to_list(self, data):
        self.clearLayout(self.MainBodyItemsLayout)

        def proc_(main, x):
            if x.item_id in main.users:
                return
            
            main.users.append(x.item_id)
            x.add(main)

        for source in data:
            try:
                self.run_in_thread(lambda: ListItemUsers(item_id=source["userId"], name=API_INSTANCE.get_user(source["userId"])["name"]), lambda x: proc_(self, x))
            except:
                pass

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

class ListItemUsers():
    def __init__(self, name, item_id=0):
        self.item_id = item_id
        self.name = name
    
    def add(self, mainWindow):
        name = QLabel(self.name)


        item = CustomQGroupBoxUsers(parent=mainWindow.MainBodyItems, item_id=self.item_id, mainWindow=mainWindow)
        item.setStyleSheet(u"QWidget QGroupBox { border: 2px solid aqua; border-radius: 2px} QGroupBox QLabel { background: none }")
        itemLayout = QHBoxLayout(item)

        itemLayout.addWidget(name)
        
        mainWindow.MainBodyItemsLayout.addWidget(item)      

class CustomQGroupBoxUsers(QGroupBox):
    def __init__(self, parent=None, item_id=0, mainWindow=None) -> None:
        super().__init__(parent=parent)

        self.item_id = item_id
        self.mainWindow = mainWindow

        self.threadpool = QThreadPool()
    
    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)
    
    def mouseDoubleClickEvent(self, event):
        def _proc(obj):
            box.ID.setText(obj["id"])
            box.Name.setText(obj["name"])
            box.Username.setText(obj["username"])
            box.Email.setText(obj["email"])

        box = UserWindow()
        
        self.run_in_thread(lambda: API_INSTANCE.get_user(self.item_id), lambda x: _proc)

        box.save.clicked.connect(lambda x: box.close())

        print(box.Email.text())
        box.show()