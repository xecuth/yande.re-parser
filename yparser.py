import random
import requests
import shutil
import os
from lxml import html
from PyQt5 import QtCore, QtWidgets, QtGui


class ParserThread(QtCore.QThread):
    pb_updated = QtCore.pyqtSignal(int)
    status_updated = QtCore.pyqtSignal(str)
    stop_message = QtCore.pyqtSignal()
    wrong_tag = QtCore.pyqtSignal()
    pb_max = QtCore.pyqtSignal(int)
    running = False

    def __init__(self, settings):
        super(ParserThread, self).__init__()

        self.session = requests.Session()
        self.session.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
        self.settings = settings
        self.urls_of_images = []
        self.downloaded = 0

        if not self.settings['explicit_mode']:
            self.session.cookies.set("country", "RU")
            self.session.cookies.set("vote", "1")


    @staticmethod
    def generate_random_name():
        alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        random.shuffle(alphabet)
        return f"{''.join(random.sample(alphabet, 4))}.jpg"

    def download_image(self, url):
        name = self.generate_random_name()
        img_bytes = requests.get(url, stream=True)
        try:
            if not os.path.exists(f"{self.settings['save_path']}/"):
                os.makedirs(f"{self.settings['save_path']}/")
            with open(f"{self.settings['save_path']}/{name}", 'wb') as f:
                img_bytes.raw.decode_content = True
                shutil.copyfileobj(img_bytes.raw, f)
        except Exception as e:
            self.status_updated.emit(f"ERROR: {e}")
            return None
        return name

    def get_image_urls(self):
        while self.settings['page_count'] >= 1:
            params = dict(
                tags=self.settings['tags'],
                page=self.settings['page_count'],
                commit="Search"
            )

            fs_paged = self.session.get(f"https://yande.re/post", params=params)
            fs_paged_res = html.fromstring(fs_paged.text)

            images = fs_paged_res.cssselect('ul#post-list-posts>li>a.directlink')

            if not images:
                self.status_updated.emit("Program not found arts, sorry about that(")
                self.wrong_tag.emit()
                return

            for x in images:
                self.urls_of_images.append(x.attrib["href"])

            self.settings['page_count'] -= 1
            QtCore.QThread.msleep(500)

        self.status_updated.emit(f"Found {len(self.urls_of_images)} arts, start download")
        QtCore.QThread.msleep(500)

    def parsing(self):
        self.status_updated.emit('Downloading...')
        self.running = True

        if not self.urls_of_images:
            self.get_image_urls()
        self.downloaded = 0
        for x in self.urls_of_images:
            if self.running:
                self.downloaded += 1
                pic_name = self.download_image(x)
                if pic_name:
                    self.status_updated.emit(f"[{self.downloaded}/{len(self.urls_of_images)}]\nFinal download image {pic_name}")
                else:
                    self.status_updated.emit(f"[{self.downloaded}/{len(self.urls_of_images)}]\nError while loading image")
                self.pb_updated.emit(1)
                QtCore.QThread.msleep(500)
            else:
                break

        self.status_updated.emit('All pictures downloaded')

    def stop(self):
        self.running = False

        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("favicon.ico"))
        msg.setText(f'Program end work.\nDownloaded {self.downloaded} images.')
        msg.setWindowTitle('Information')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def run(self):
        if self.get_image_urls():
            self.pb_max.emit(len(self.urls_of_images))
            self.parsing()

        if self.running:
            self.stop_message.emit()
