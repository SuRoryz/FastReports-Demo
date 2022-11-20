from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QSize
from PySide2.QtGui import *

class CustomQLabel(QLabel):
    def __init__(self, parent=None, folder_name=None, folder_id=0) -> None:
        print(folder_name)
        super().__init__(text=folder_name, parent=parent)

        self.folder_id = folder_id
    
    def mousePressEvent(self, event):
        event.accept()

        if event.button() == Qt.LeftButton:
            mainApp.widget.current_folder = self.folder_id

            mainApp.widget.run_in_thread(mainApp.widget.load_folder, mainApp.widget.apply_data_to_list)

            while True:
                item = self.parent().layout().takeAt(self.parent().layout().count()-2)
                print(item, item.widget(), self.text())
                widget_ = item.widget()

                if widget_ == self:
                    self.parent().layout().insertWidget(self.parent().layout().count()-1, widget_)
                    break
                
                widget_.deleteLater()