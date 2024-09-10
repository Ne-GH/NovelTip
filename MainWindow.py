import sys
import time

from PySide6 import QtCore,QtWidgets
from PySide6.QtGui import QTextFrame
from PySide6.QtWidgets import QWidget, QMessageBox

from Novel import Novel

class MainWindow(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(400,400)
        self.novel_list = []

        but = QtWidgets.QPushButton(self)
        but.setText('添加小说')
        but.clicked.connect(self.betch_add_novel)

        self.widget = QtWidgets.QWidget()
        self.widget.hide()

    def betch_add_novel(self):
        print('\ncall this func')
        self.widget.resize(100,100)
        if self.layout() == None:
            layout = QtWidgets.QFormLayout(self.widget)

        self.webside_edit = QtWidgets.QLineEdit(self.widget)
        layout.addRow("网址",self.webside_edit)
        self.widget.show()
        self.webside_edit.editingFinished.connect(self.message)


    def message(self):
        message = QMessageBox(self)
        self.novel_list.append(Novel(self.webside_edit.text()))

        self.widget.close()



        for novel in self.novel_list:
            if not novel.website_is_ok:
                err_mes = QMessageBox(self)
                err_mes.setText('该网站接连失败')
                err_mes.exec()
            else:
                novel.parse_novel_catalog_website()










