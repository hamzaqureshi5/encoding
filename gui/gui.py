import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui.forms.main import Ui_MainWindow  # Import the UI class from the converted Python file


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = self.setupUi(self)  # This sets up the UI created in the .ui file
        self.
