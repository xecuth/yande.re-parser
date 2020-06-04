import os
from design import Ui_MainWindow
from parser_thread import ParserThread, QtWidgets, QtGui


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.parser_task = None

        self.tags_line = ''
        self.page_count = 0
        self.explicit_content = False
        self.save_path = ''

        self.ui.savePathPushButton.clicked.connect(self.get_dir)
        self.ui.startPushButton.clicked.connect(self.event_checker)
        self.ui.stopPushButton.clicked.connect(self.on_stop)
        self.ui.actionAuthor_2.triggered.connect(self.about_author_dlg)

    def event_checker(self):
        self.tags_line = self.ui.tagsQueryLineEdit.text()
        self.page_count = int(self.ui.pageCountSpinBox.text())
        self.explicit_content = True if self.ui.explicitContentCheckBox.isChecked() else False

        if self.tags_line and self.page_count and self.save_path:
            self.on_start()
        else:
            self.unfilled_items()

    def on_start(self):
        self.parser_task = ParserThread({
                            'save_path': self.save_path,
                            'explicit_mode': self.explicit_content,
                            'tags': self.tags_line,
                            'page_count': self.page_count
                            })


        self.ui.progressBar.setValue(0)

        self.parser_task.pb_updated.connect(self.pb_update)
        self.parser_task.status_updated.connect(self.status_update)
        self.parser_task.stop_message.connect(self.parser_task.stop)
        self.parser_task.wrong_tag.connect(self.wrong_tag_dlg)
        self.parser_task.pb_max.connect(self.pb_setmax)

        self.parser_task.start()

    def on_stop(self):
        if self.parser_task:
            self.parser_task.stop()

    def status_update(self, msg):
        self.ui.statusLabel.setText(msg)
        self.ui.statusLabel.adjustSize()

    def pb_update(self, val):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + val)

    def pb_setmax(self, val):
        self.ui.progressBar.setMaximum(val)

    def get_dir(self):
        file_name = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file_name:
            if os.sep == '\\':
                file_name = file_name.replace('/', '\\')
            self.save_path = file_name
            self.status_update('Folder Choosed!')
            self.ui.savePathLineEdit.setText(self.save_path)
        else:
            return ""

    @staticmethod
    def about_author_dlg():
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("favicon.ico"))
        msg.setText(f'Program written by xecuth\nLink: https://github.com/xecuth')
        msg.setWindowTitle('Information')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def unfilled_items(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("favicon.ico"))
        msg.setText('You dont fill all items')

        message = ''
        if not self.tags_line:
            message += 'You dont fill tags\n'
        if not self.save_path:
            message += 'You dont choose save path'

        msg.setDetailedText(message)
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    @staticmethod
    def wrong_tag_dlg():
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("favicon.ico"))
        msg.setText('Wrong tag line')
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
