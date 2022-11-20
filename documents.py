from views.window import Ui_Form as wd

from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

from utilWindows import *
from worker import Worker, WorkerSignals
from utils import *

from API import API

class Wind(QWidget, wd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threadpool = QThreadPool()

        self.current_folder = None
        self.current_folder_name = None
        self.location = None

        self.MainBodyBody.mousePressEvent = self._mousePressEvent
        self.MainBodyItems.mousePressEvent = lambda event: event.accept()

        self.first_folder = CustomQLabel(parent=self.MainBodyItems, folder_name="Templates")
        self.horizontalLayout.insertWidget(self.horizontalLayout.count()-1, self.first_folder)

        self.subs = API_INSTANCE.get_subscriptions()
        print(self.subs)

        self.run_in_thread(self.load_window, self.apply_data_to_list)


    def load_window(self, window_="templates"):
        if window_ == "templates":
            subs = self.subs["subscriptions"][0]["templatesFolder"]["folderId"]
            self.current_folder_name = "Templates"

        elif window_ == "reports":
            subs = self.subs["subscriptions"][0]["reportsFolder"]["folderId"]
            self.current_folder_name = "Reports"

        elif window_ == "exports":
            subs = self.subs["subscriptions"][0]["exportsFolder"]["folderId"]
            self.current_folder_name = "Exports"
        
        self.current_folder = subs
        self.first_folder.folder_id = subs
        self.first_folder.setText(self.current_folder_name)
        
        while self.MainHeader.layout().count() >= 3:
            w = self.MainHeader.layout().takeAt(self.MainHeader.layout().count()-2).widget()
            w.deleteLater()

        self.location = window_
        return self.load_folder(self.current_folder)
    
    def load_folder(self, folder_id=None, folder_name=None):
        result = []

        count = max(1, int(eval(f"API_INSTANCE.get_{self.location}_folder_and_files_count")(folder_id if folder_id else self.current_folder)["count"]))
        files = eval(f"API_INSTANCE.get_{self.location}_folder_and_files")(folder_id if folder_id else self.current_folder, take=count)
        print(files)
        for folder in files["files"]:
            result.append(folder)

        return result

    def run_in_thread(self, func, result_func, *args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        worker.signals.result.connect(result_func)

        self.threadpool.start(worker)

    def _mousePressEvent(self, event):
        if event.button() == Qt.RightButton:

            p = self.MainBodyBody.mapToGlobal(event.pos()) # or QtGui.QCursor.pos()
            menu = self.create_menu_contextual()
            action = menu.exec_(p)
            print(action.text())

    def create_folder(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Folder name:')

        self.run_in_thread(lambda: print(eval(f"API_INSTANCE.post_{self.location}_folder")(self.current_folder, name=name)), lambda: self.run_in_thread(self.load_folder, self.apply_data_to_list))
    
    def create_file(self):
        filepath = QFileDialog.getOpenFileName(self, "Select File")[0]
        name = filepath.split("/")[-1]
        print("EEEEEEEE", filepath, name)

        self.run_in_thread(lambda: print(eval(f"API_INSTANCE.post_{self.location}_file")(self.current_folder, name=name, file_path=filepath)), lambda: self.run_in_thread(self.load_folder, self.apply_data_to_list))

    def create_menu_contextual(self):
        menu = QMenu()

        create_action = menu.addAction("Создать папку")
        create_action.triggered.connect(self.create_folder)
        create_action_file = menu.addAction("Загрузить файл")
        create_action_file.triggered.connect(self.create_file)

        menu.addAction(create_action)
        menu.addAction(create_action_file)
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

    def apply_data_to_list(self, data):
        self.clearLayout(self.MainBodyItemsLayout)
        for folder in data:
            print(folder["id"])
            ListItemDocument(name=folder["name"], size=folder["size"] if folder["type"] == "File" else None, item_id=folder["id"], item_type=folder["type"]).add(self)

class ListItemDocument():
    def __init__(self, name, size="", last_update=None, item_id=0, item_type="folder"):
        self.name = name
        self.size = size
        self.last_update = last_update

        self.item_id = item_id
        self.item_type = item_type

        self.hover_enter_signal = Signal()
        self.hover_leave_signal = Signal()
    
    def add(self, mainWindow):
        name = QLabel(self.name)

        name_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        name_sizePolicy.setHorizontalStretch(5)
        name_sizePolicy.setVerticalStretch(0)

        name.setSizePolicy(name_sizePolicy)

        size = QLabel(str(self.size if self.size else ""))

        size_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        size_sizePolicy.setHorizontalStretch(1)
        size_sizePolicy.setVerticalStretch(0)

        size.setSizePolicy(size_sizePolicy)
        size.setAlignment(Qt.AlignCenter)

        last_update = QLabel(self.last_update)

        update_sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        update_sizePolicy.setHorizontalStretch(1)
        update_sizePolicy.setVerticalStretch(0)

        last_update.setSizePolicy(update_sizePolicy)
        last_update.setAlignment(Qt.AlignCenter)

        item = CustomQGroupBoxDocuments(parent=mainWindow.MainBodyItems, item_id=self.item_id, item_type=self.item_type, name=self.name)
        item.setStyleSheet(u"QWidget QGroupBox { border: 2px solid aqua; border-radius: 2px} QGroupBox QLabel { background: none }")
        itemLayout = QHBoxLayout(item)

        itemLayout.addWidget(name)
        itemLayout.addWidget(size)
        itemLayout.addWidget(last_update)
        
        mainWindow.MainBodyItemsLayout.addWidget(item)

class CustomQGroupBoxDocuments(QGroupBox):
    def __init__(self, parent=None, item_id=0, item_type="Folder", name=None) -> None:
        super().__init__(parent=parent)

        self.item_id = item_id
        self.type = item_type
        self.name = name

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
    
    def mouseDoubleClickEvent(self, event):
        if self.type == "Folder":
            mainApp.widget.current_folder = self.item_id
            mainApp.widget.run_in_thread(mainApp.widget.load_folder, mainApp.widget.apply_data_to_list)

            fld = CustomQLabel(parent=mainApp.widget.MainBodyItems, folder_name="> " + self.name, folder_id=self.item_id)
            mainApp.widget.horizontalLayout.insertWidget(mainApp.widget.horizontalLayout.count()-1, fld)

    def delete_item(self):
        print("ID:", self.item_id, self.type)

        def _delete_folder(id):
            result = eval(f"API_INSTANCE.delete_{mainApp.widget.location}_folder")(id)

            print(result)

            if result and 'status' in result and result['status'] == 403:
                print("No perms")
        
        def _delete_file(id):
            result = eval(f"API_INSTANCE.delete_{mainApp.widget.location}_file")(id)
            print(result)

            if result and 'status' in result and result['status'] == 403:
                print("No perms")

        if self.type == "Folder":
            self.run_in_thread(lambda: _delete_folder(self.item_id), lambda: mainApp.run_in_thread(mainApp.widget.load_folder, mainApp.widget.apply_data_to_list))
        else:
            self.run_in_thread(lambda: _delete_file(self.item_id), lambda: mainApp.widget.run_in_thread(mainApp.widget.load_folder, mainApp.widget.apply_data_to_list))

    def rename_item(self):
        name, ok = QInputDialog.getText(self, 'Input Dialog', 
            'New name:')

        def _rename_folder(id):
            result = eval(f"API_INSTANCE.put_{mainApp.widget.location}_folder")(id, name)

            print(result)

            if result and 'status' in result and result['status'] == 403:
                print("No perms")
        
        def _rename_file(id):
            result = eval(f"API_INSTANCE.put_{mainApp.widget.location}_file")(id, name)
            print(result)

            if result and 'status' in result and result['status'] == 403:
                print("No perms")

        if self.type == "Folder":
            self.run_in_thread(lambda: _rename_folder(self.item_id), lambda: mainApp.widget.run_in_thread(mainApp.widget.load_folder, mainApp.widget.apply_data_to_list))
        else:
            self.run_in_thread(lambda: _rename_file(self.item_id), lambda: mainApp.widget.run_in_thread(mainApp.widget.load_folder, mainApp.widget.apply_data_to_list))
        
    def create_menu_contextual(self):
        menu = QMenu()

        delete_action = menu.addAction("Удалить")
        delete_action.triggered.connect(self.delete_item)

        rename_action = menu.addAction("Переименовать")
        rename_action.triggered.connect(self.rename_item)

        menu.addAction(delete_action)
        menu.addAction(rename_action)

        return menu