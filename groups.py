from views.window_group import Ui_Form as wd_g

from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

from utilWindows import *
from worker import Worker, WorkerSignals
from utils import *

from API import API

class Wind_Group(QWidget, wd_g):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threadpool = QThreadPool()

        self.subs = API_INSTANCE.get_subscriptions()

        self.MainBodyBody.mousePressEvent = self._mousePressEvent
        self.MainBodyItems.mousePressEvent = lambda event: event.accept()

        self.run_in_thread(self.load_window, self.apply_data_to_list)
    
    def load_window(self):
        result = []

        sources = API_INSTANCE.get_groups(self.subs["subscriptions"][0]["id"], take=120)
        print(sources)
        for source in sources["groups"]:
            result.append(source)

        return result
    
    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)
    
    def apply_data_to_list(self, data):
        self.clearLayout(self.MainBodyItemsLayout)
        print(data)
        for source in data:
            ListItemGroups(name=source["name"], item_id=source["id"]).add(self)
    
    def create_item(self):
        self.run_in_thread(lambda: print(API_INSTANCE.post_group(self.subs["subscriptions"][0]["id"])), lambda: self.load_window())

    def _mousePressEvent(self, event):
        if event.button() == Qt.RightButton:

            p = self.MainBodyBody.mapToGlobal(event.pos()) # or QtGui.QCursor.pos()
            menu = self.create_menu_contextual()
            action = menu.exec_(p)
            print(action.text())

    def create_menu_contextual(self):
        menu = QMenu()

        create_action = menu.addAction("Create")
        create_action.triggered.connect(self.create_item)

        menu.addAction(create_action)
        return menu

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

class ListItemGroups():
    def __init__(self, name, item_id=0):
        self.name = name
        self.item_id = item_id
    
    def add(self, mainWindow):
        name = QLabel(self.name)

        name_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        name_sizePolicy.setHorizontalStretch(5)
        name_sizePolicy.setVerticalStretch(0)

        name.setSizePolicy(name_sizePolicy)

        item = CustomQGroupBoxGroups(parent=mainWindow.MainBodyItems, item_id=self.item_id, name=self.name, mainWindow=mainWindow)
        item.setStyleSheet(u"QWidget QGroupBox { border: 2px solid aqua; border-radius: 2px} QGroupBox QLabel { background: none }")
        itemLayout = QHBoxLayout(item)

        itemLayout.addWidget(name)
        
        mainWindow.MainBodyItemsLayout.addWidget(item) 

class CustomQGroupBoxGroups(QGroupBox):
    def __init__(self, parent=None, item_id=0, name=None, mainWindow=None) -> None:
        super().__init__(parent=parent)

        self.item_id = item_id
        self.name = name
        self.mainWindow = mainWindow

        self.threadpool = QThreadPool()
    
    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)
    
    def mouseDoubleClickEvent(self, event):
        box = GroupUsersEditWindow()
        
        def _after_proc(r):
            self.run_in_thread(lambda: API_INSTANCE.get_group_users(self.item_id), lambda x: box.completeWindow(x, r))

        self.run_in_thread(lambda: API_INSTANCE.get_users(self.mainWindow.subs["subscriptions"][0]["id"]), _after_proc)

        box.show()

    def mousePressEvent(self, event):
        event.accept()

        super().mousePressEvent(event)
        if event.button() == Qt.RightButton:
            p = self.mapToGlobal(event.pos()) # or QtGui.QCursor.pos()
            menu = self.create_menu_contextual()

            action = menu.exec_(p)

    def delete_item(self):
        self.run_in_thread(lambda: API_INSTANCE.delete_group(self.item_id), lambda: self.mainWindow.load_window())

    def create_menu_contextual(self):
        menu = QMenu()

        delete_action = menu.addAction("Delete")
        delete_action.triggered.connect(self.delete_item)

        menu.addAction(delete_action)
        return menu