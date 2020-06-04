# -*- coding: utf-8 -*-
import sys
import gui

if __name__ == '__main__':
    app = gui.QtWidgets.QApplication([])
    application = gui.MyWindow()
    application.show()

    sys.exit(app.exec())
