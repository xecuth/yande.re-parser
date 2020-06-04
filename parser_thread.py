import os
import io
import random
import requests
from PIL import Image
from lxml import html
from PyQt5 import QtCore, QtWidgets, QtGui
from multiprocessing.pool import ThreadPool


class ParserThread(QtCore.QThread):
    pb_updated = QtCore.pyqtSignal(int)
    status_updated = QtCore.pyqtSignal(str)
    stop_message = QtCore.pyqtSignal()
    wrong_tag = QtCore.pyqtSignal()
    pb_max = QtCore.pyqtSignal(int)
    running = False

    def __init__(self, settings, process_count):
        super(ParserThread, self).__init__()

        self.session = requests.Session()
        self.session.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
        self.settings = settings
        self.urls_of_images = []
        self.downloaded = 0
        self.mp_processes = process_count

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
        res = requests.get(url, stream=True)
        if not os.path.exists(f"{self.settings['save_path']}/"):
            os.makedirs(f"{self.settings['save_path']}/")

        img = Image.open(io.BytesIO(res.content))
        img.save(self.settings['save_path'] + '\\' + name)
        return name

    def get_image_urls(self):
        self.status_updated.emit('Image urls searching. It can take some time..')
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

        self.status_updated.emit(f"Found {len(self.urls_of_images)} arts, start download")

    def parsing(self):
        self.status_updated.emit('Downloading...')
        self.running = True

        self.downloaded = 0

        image_pool = ThreadPool(self.mp_processes).imap_unordered(self.download_image, self.urls_of_images)

        for i in image_pool:
            self.status_updated.emit(f"[{self.downloaded}/{len(self.urls_of_images)}]Final download image {i}")
            self.downloaded += 1
            self.pb_updated.emit(1)

        self.status_updated.emit('All pictures downloaded')

    def stop(self):
        self.running = False

        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("favicon.ico"))
        msg.setText(f'Program end work.\nDownloaded {self.downloaded} images.')
        msg.setWindowTitle('Information')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.status_updated.emit('Program stopped')
        msg.exec_()

    def run(self):
        self.get_image_urls()
        self.pb_max.emit(len(self.urls_of_images))
        self.parsing()

        if self.running:
            self.stop_message.emit()
