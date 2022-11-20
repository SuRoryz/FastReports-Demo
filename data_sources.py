from views.window_database import Ui_Form as wd_d

from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

from utilWindows import *
from worker import Worker, WorkerSignals
from utils import *

from API import API

class Wind_Datasources(QWidget, wd_d):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threadpool = QThreadPool()

        self.subs = API_INSTANCE.get_subscriptions()

        self.run_in_thread(self.load_window, self.apply_data_to_list)
    
    def load_window(self):
        result = []

        sources = API_INSTANCE.get_datasources(self.subs["subscriptions"][0]["id"], take=120)
        print(self.subs["subscriptions"][0]["id"])
        for source in sources["dataSources"]:
            result.append(source)

        return result
    
    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)
    
    def apply_data_to_list(self, data):
        self.clearLayout(self.MainBodyItemsLayout)
        for source in data:
            ListItemDatasource(name=source["name"], type=source["connectionType"], item_id=source["id"], status=source["status"]).add(self)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

class ListItemDatasource():
    def __init__(self, name, type=None, status=None, item_id=0):
        self.name = name
        self.type = type
        self.status = status

        self.item_id = item_id
    
    def add(self, mainWindow):
        name = QLabel(self.name)

        name_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        name_sizePolicy.setHorizontalStretch(5)
        name_sizePolicy.setVerticalStretch(0)

        name.setSizePolicy(name_sizePolicy)

        type = QLabel(self.type)

        type_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        type_sizePolicy.setHorizontalStretch(1)
        type_sizePolicy.setVerticalStretch(0)

        type.setSizePolicy(type_sizePolicy)
        type.setAlignment(Qt.AlignCenter)

        status = QLabel(self.status)

        update_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        update_sizePolicy.setHorizontalStretch(1)
        update_sizePolicy.setVerticalStretch(0)

        status.setSizePolicy(update_sizePolicy)
        status.setAlignment(Qt.AlignCenter)

        item = CustomQGroupBoxDataSource(parent=mainWindow.MainBodyItems, item_id=self.item_id, item_type=self.type, name=self.name, status=self.status)
        item.setStyleSheet(u"QWidget QGroupBox { border: 2px solid aqua; border-radius: 2px} QGroupBox QLabel { background: none }")
        itemLayout = QHBoxLayout(item)

        itemLayout.addWidget(name)
        itemLayout.addWidget(type)
        itemLayout.addWidget(status)
        
        mainWindow.MainBodyItemsLayout.addWidget(item)    

class CustomQGroupBoxDataSource(QGroupBox):
    def __init__(self, parent=None, item_id=0, item_type="Folder", name=None, status=None) -> None:
        super().__init__(parent=parent)

        self.item_id = item_id
        self.type = item_type
        self.name = name
        self.status = status

        self.threadpool = QThreadPool()
    
    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)
    
    def mousePressEvent(self, event):
        event.accept()

        super().mousePressEvent(event)
        if event.button() == Qt.RightButton:
            p = self.mapToGlobal(event.pos()) # or QtGui.QCursor.pos()
            menu = self.create_menu_contextual()

            action = menu.exec_(p)
    
    def show_structure(self):
        box = QMessageBox()
        box.setText("Loading...")

        self.run_in_thread(lambda: API_INSTANCE.get_datasource(self.item_id)["dataStructure"], lambda x: [box.setInformativeText(x), box.setText("")])
        box.exec_()

    
    def edit(self):
        box = TextEditWindow()
        
        box.pushButton.clicked.connect(lambda x: [API_INSTANCE.put_datasource_connectionstring(self.item_id, '"json=\"' + base64.b64encode(box.textEdit.toPlainText().encode()).decode()), box.close()])
        box.textEdit.setText("Loading...")

        self.run_in_thread(lambda: API_INSTANCE.get_datasource(self.item_id)["connectionString"], lambda x: box.textEdit.setText(base64.b64decode(x.replace('json="', '').replace('"', '')).decode()))

        box.show()

    def check_status(self):
        pass

    def delete_item(self):
        pass

    def rename_item(self):
        pass


    def create_menu_contextual(self):
        menu = QMenu()

        show_action = menu.addAction("Show Structure")
        show_action.triggered.connect(self.show_structure)

        edit_action = menu.addAction("Edit")
        edit_action.triggered.connect(self.edit)

        check_action = menu.addAction("Check status")
        check_action.triggered.connect(self.check_status)

        delete_action = menu.addAction("Delete")
        delete_action.triggered.connect(self.delete_item)

        rename_action = menu.addAction("Rename")
        rename_action.triggered.connect(self.rename_item)

        menu.addAction(show_action)
        menu.addAction(edit_action)
        menu.addAction(check_action)
        menu.addAction(delete_action)
        menu.addAction(rename_action)
        return menu