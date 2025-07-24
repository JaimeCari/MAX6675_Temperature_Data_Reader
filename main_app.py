import sys
from PyQt5.QtWidgets import QApplication
from app_gui import ArduinoControlApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArduinoControlApp()
    window.show()
    sys.exit(app.exec_())
