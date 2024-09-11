import random,sys,threading
from time import sleep, thread_time

from PySide6 import QtWidgets

import MainWindow

def loop_query(novel_list):
    while True:
        for novel in novel_list:
            novel.parse_novel_catalog_website()
            if novel.cur_chapter_count == novel.last_chapter_count:
                sleep(60 * 2)
                continue
            else:
                # 提示小说更新
                pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow.MainWindow()
    widget.show()

    # 此处开一个线程
    threading.Thread(target=loop_query, args=(widget.novel_list,)).start()


    sys.exit(app.exec())
