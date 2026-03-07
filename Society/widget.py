# This Python file uses the following encoding: utf-8
# import sys

# from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QPushButton
from PySide6 import QtUiTools
import sys

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Now you can access widgets directly as attributes
        self.stacked = self.ui.stackedPages

        # Connect buttons to stacked pages
        self.ui.btnInventory.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        self.ui.btnStock.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        self.ui.btnBilling.clicked.connect(lambda: self.stacked.setCurrentIndex(2))
        self.ui.btnUpload.clicked.connect(lambda: self.stacked.setCurrentIndex(3))
        self.ui.btnCreate.clicked.connect(lambda: self.stacked.setCurrentIndex(4))
        self.ui.btnShop.clicked.connect(lambda: self.stacked.setCurrentIndex(5))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
