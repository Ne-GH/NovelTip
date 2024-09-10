import random,sys
from PySide6 import QtWidgets

import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow.MainWindow()
    widget.show()
    sys.exit(app.exec())
