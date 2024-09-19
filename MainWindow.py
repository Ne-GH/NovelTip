
from PySide6 import QtCore,QtWidgets
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QScrollArea

from Novel import Novel


class ChapterWindow(QWidget):
    def __init__(self, chapters, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)

        container = QtWidgets.QWidget()
        container_layout = QVBoxLayout(container)


        for chapter in chapters:
            label = QLabel(chapter)
            container_layout.addWidget(label)

        scroll_area = QScrollArea()
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)

        layout.addWidget(scroll_area)

        self.setLayout(layout)


class MainWindow(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(400,400)
        self.novel_list = []
        # self.novel_list.append(Novel('https://www.84kanshu.com/book/95298954/'))
        # self.novel_list.append(Novel('https://www.ximalaya.com/album/75949958'))

        but = QtWidgets.QPushButton(self)
        but.setText('添加小说')
        but.clicked.connect(self.betch_add_novel)

        self.widget = QtWidgets.QWidget()
        self.widget.hide()

    def betch_add_novel(self):
        self.widget.resize(100,100)
        layout = QtWidgets.QFormLayout(self.widget)

        self.webside_edit = QtWidgets.QLineEdit(self.widget)
        layout.addRow("网址",self.webside_edit)
        self.widget.show()
        self.webside_edit.editingFinished.connect(self.message)


    def message(self):
        self.novel_list.append(Novel(self.webside_edit.text()))

        self.widget.close()

        for novel in self.novel_list:
            if not novel.website_is_ok:
                err_mes = QMessageBox(self)
                err_mes.setText('该网站接连失败')
                err_mes.exec()
            else:
                chapter_count, chapters = novel.parse_novel_catalog_website()


                if chapters:
                    self.chapter_window = ChapterWindow(chapters)
                    self.chapter_window.setWindowTitle('章节列表')
                    self.chapter_window.resize(300, 400)
                    self.chapter_window.show()
                else:
                    err_mes = QMessageBox(self)
                    err_mes.setText('未能获取章节信息')
                    err_mes.exec()










