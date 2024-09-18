
from PySide6 import QtCore,QtWidgets
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QScrollArea

from Novel import Novel


class ChapterWindow(QWidget):  # 新添加
    def __init__(self, chapters, *args, **kwargs):  # 新添加
        super().__init__(*args, **kwargs)  # 新添加

        layout = QVBoxLayout(self)  # 新添加

        container = QtWidgets.QWidget()  # 新添加
        container_layout = QVBoxLayout(container)  # 新添加

        print("chapterWindow act\n")

        for chapter in chapters:  # 新添加
            label = QLabel(chapter)  # 新添加
            container_layout.addWidget(label)  # 新添加

        scroll_area = QScrollArea()  # 新添加
        scroll_area.setWidget(container)  # 新添加
        scroll_area.setWidgetResizable(True)  # 新添加

        layout.addWidget(scroll_area)  # 新添加

        self.setLayout(layout)  # 新添加


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
        print('\ncall this func')
        self.widget.resize(100,100)
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
                chapter_count, chapters = novel.parse_novel_catalog_website()

                # print(f"{chapters}")

                # Create and show the ChapterWindow with the list of chapters
                if chapters:  # MODIFIED: 检查是否成功获取章节
                    self.chapter_window = ChapterWindow(chapters)  # 新添加
                    self.chapter_window.setWindowTitle('章节列表')  # 新添加
                    self.chapter_window.resize(300, 400)  # 新添加
                    self.chapter_window.show()  # 新添加
                else:
                    err_mes = QMessageBox(self)
                    err_mes.setText('未能获取章节信息')  # MODIFIED: 如果没有章节则显示错误信息
                    err_mes.exec()










