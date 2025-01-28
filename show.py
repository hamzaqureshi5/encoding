import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
# from main import Ui_MainWindow  # Import the UI class from the converted Python file
from forms.main import Ui_MainWindow  # Import the UI class from the converted Python file



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # This sets up the UI created in the .ui file

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application event loop
