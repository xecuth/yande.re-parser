import os
from PyQt5 import QtWidgets
from design import Ui_MainWindow
from yparser import Parser


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.task = None

        self.tags_line = ''
        self.page_count = 0
        self.explicit_content = False
        self.save_path = ''

        self.ui.ChooseFolderPushButton.clicked.connect(self.get_dir)
        self.ui.StartPushButton.clicked.connect(self.event_checker)

    def event_checker(self):
        self.tags_line = self.ui.TagsQueryLineEdit.text()
        self.page_count = int(self.ui.PageCountSpinBox.text())
        self.explicit_content = True if self.ui.explicitContentCheckBox.isChecked() else False

        if self.tags_line and self.page_count and self.save_path:
            self.on_start()
        else:
            self.message_out('WARNING! You dont fill all items!')

    def on_start(self):
        self.task = Parser({
                            'save_path': self.save_path,
                            'explicit_mode': self.explicit_content,
                            'tags': self.tags_line,
                            'page_count': self.page_count
                            })


        self.ui.progressBar.setValue(0)

        self.task.pb_updated.connect(self.pb_update)
        self.task.message_out_update.connect(self.message_out)
        self.task.status_out_update.connect(self.status_out)
        self.task.pb_max.connect(self.pb_setmax)

        self.task.start()



    def message_out(self, msg):
        self.ui.ButtonDescriptionLabel.setText(msg)

    def status_out(self, msg):
        self.ui.ProgressBarDescriptionLabel.setText(msg)

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
            self.message_out('Folder Choosed!')
        else:
            return ""
