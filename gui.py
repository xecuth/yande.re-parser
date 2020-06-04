from design import Ui_MainWindow
from parser_thread import ParserThread, QtWidgets, QtCore, QtGui, os


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

        self.process_count = 12

        self.ui.savePathPushButton.clicked.connect(self.get_dir)
        self.ui.startPushButton.clicked.connect(self.settings_verification)
        self.ui.stopPushButton.clicked.connect(self.on_stop)
        self.ui.actionAuthor_2.triggered.connect(self.about_author_dlg)
        self.ui.actionMultiprocessing.triggered.connect(self.mp_settings)
        self.ui.numberOfProcessSetPushButton.clicked.connect(self.set_process_count)

    def settings_verification(self):
        self.tags_line = self.ui.tagsQueryLineEdit.text()
        self.page_count = int(self.ui.pageCountSpinBox.text())
        self.explicit_content = True if self.ui.explicitContentCheckBox.isChecked() else False

        if self.tags_line and self.page_count and self.save_path:
            self.on_start()
        else:
            self.unfilled_items_dlg()

    def on_start(self):
        self.parser_task = ParserThread({
                            'save_path': self.save_path,
                            'explicit_mode': self.explicit_content,
                            'tags': self.tags_line,
                            'page_count': self.page_count
                            }, process_count=self.process_count)


        self.ui.progressBar.setValue(0)

        self.parser_task.pb_updated.connect(self.pb_update)
        self.parser_task.status_updated.connect(self.status_update)
        self.parser_task.stop_message.connect(self.parser_task.stop)
        self.parser_task.invalid_tag.connect(self.invalid_tag_dlg)
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
        file_name = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory'))
        if file_name:
            if os.sep == '\\':
                file_name = file_name.replace('/', '\\')
            self.save_path = file_name
            self.status_update('Folder selected.')
            self.ui.savePathLineEdit.setText(self.save_path)
        else:
            return ''

    @staticmethod
    def about_author_dlg():
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('favicon.ico'))
        msg.setText(f'\nProgram written by xecuth\nLink: https://github.com/xecuth\n')
        msg.setWindowTitle('Information')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def unfilled_items_dlg(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('favicon.ico'))
        msg.setText('Some items are empty.')

        message = ''
        if not self.tags_line:
            message += 'Tag line is empty.\n'
        if not self.save_path:
            message += 'Save path is empty'

        msg.setDetailedText(message)
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    @staticmethod
    def invalid_tag_dlg():
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('favicon.ico'))
        msg.setText('Invalid tags, review them.')
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def set_process_count(self):
        self.process_count = int(self.ui.numberOfProcessesSpinBox.text())
        self.status_update(f'Number of process changed to {self.process_count}.')

    def mp_settings(self):
        if self.ui.actionMultiprocessing.text() == 'Show MP settings':
            self.resize(800, 250)
            self.setMinimumSize(QtCore.QSize(800, 250))
            self.setMaximumSize(QtCore.QSize(800, 250))
            self.ui.numberOfProcessesSpinBox.setValue(self.process_count)
            self.ui.actionMultiprocessing.setText('Close MP settings')
        else:
            self.resize(800, 200)
            self.setMinimumSize(QtCore.QSize(800, 200))
            self.setMaximumSize(QtCore.QSize(800, 200))
            self.ui.actionMultiprocessing.setText('Show MP settings')



