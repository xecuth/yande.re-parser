import os
from PyQt5 import QtWidgets
from design import Ui_MainWindow
from yparser import Parser


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.parser = None

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
            self.parse()
        else:
            self.btn_desc('WARNING! You dont fill all items!')

    def parse(self):
        self.parser = Parser({
                            'save_path': self.save_path,
                            'explicit_mode': self.explicit_content,
                            'tags': self.tags_line,
                            'page_count': self.page_count
                            },
                            status_output=self.pb_desc,
                            message_output=self.btn_desc,
                            pb_inc=self.pb_increase)

        self.parser.get_image_urls()
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(len(self.parser.urls_of_images))
        self.parser.parsing()

    def btn_desc(self, msg):
        self.ui.ButtonDescriptionLabel.setText(msg)

    def pb_desc(self, msg):
        self.ui.ProgressBarDescriptionLabel.setText(msg)

    def pb_increase(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

    def get_dir(self):
        file_name = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file_name:
            if os.sep == '\\':
                file_name = file_name.replace('/', '\\')
            self.save_path = file_name
            self.btn_desc('Folder Choosed!')
        else:
            return ""
