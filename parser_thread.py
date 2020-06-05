# -*- coding: utf-8 -*-
import os
import random
import shutil
import requests
from lxml import html
from PyQt5 import QtCore, QtWidgets, QtGui
from multiprocessing.pool import ThreadPool


class ParserThread(QtCore.QThread):
    pb_updated = QtCore.pyqtSignal(int)
    status_updated = QtCore.pyqtSignal(str)
    stop_message = QtCore.pyqtSignal()
    invalid_tag = QtCore.pyqtSignal()
    pb_max = QtCore.pyqtSignal(int)
    running = False

    def __init__(self, settings, process_count, image_format):
        super(ParserThread, self).__init__()

        self.session = requests.Session()
        self.session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
        self.settings = settings
        self.urls_of_images = []
        self.downloaded = 0
        self.mp_processes = process_count
        self.image_format = image_format

        if not self.settings['explicit_mode']:
            self.session.cookies.set('country', 'RU')
            self.session.cookies.set('vote', '1')

    def generate_random_name(self):
        alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        random.shuffle(alphabet)
        return f"{''.join(random.sample(alphabet, 4))}.{self.image_format}"

    def download_image(self, url):
        name = self.generate_random_name()

        img_bytes = requests.get(url, stream=True)
        try:
            if not os.path.exists(f"{self.settings['save_path']}\\"):
                os.makedirs(f"{self.settings['save_path']}\\")

            with open(f"{self.settings['save_path']}\\{name}", 'wb') as f:
                img_bytes.raw.decode_content = True
                shutil.copyfileobj(img_bytes.raw, f)
        except Exception as e:
            print(f"ERROR: {e}")
            return None

        return name

    def get_image_urls(self):
        self.status_updated.emit('Image urls searching. It can take some time..')
        while self.settings['page_count'] >= 1:
            params = dict(
                tags=self.settings['tags'],
                page=self.settings['page_count'],
                commit='Search'
            )

            fs_paged = self.session.get(f'https://yande.re/post', params=params)
            fs_paged_res = html.fromstring(fs_paged.text)

            images = fs_paged_res.cssselect('ul#post-list-posts>li>a.directlink')

            if not images:
                self.status_updated.emit('Program not found arts.')
                self.invalid_tag.emit()
                return

            for x in images:
                self.urls_of_images.append(x.attrib['href'])

            self.settings['page_count'] -= 1

        self.status_updated.emit(f'Found {len(self.urls_of_images)} arts, start download')
        return True



    def parsing(self):
        self.status_updated.emit('Downloading...')
        self.running = True

        self.downloaded = 0
        image_pool = ThreadPool(self.mp_processes)

        for i in image_pool.imap_unordered(self.download_image, self.urls_of_images):
            if self.running:
                self.status_updated.emit(f'[{self.downloaded}/{len(self.urls_of_images)}]Final download image {i}')
                self.downloaded += 1
                self.pb_updated.emit(1)
                QtCore.QThread.msleep(50)
            else:
                image_pool.terminate()
                return

        self.status_updated.emit('All pictures downloaded')

    def stop(self):
        self.running = False

        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('favicon.ico'))
        msg.setText(f'Program finished work.\nDownloaded {self.downloaded} images.')
        msg.setWindowTitle('Information')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.status_updated.emit('Program stopped.')
        msg.exec_()

    def run(self):
        if self.get_image_urls():
            self.pb_max.emit(len(self.urls_of_images))
            self.parsing()

        if self.running:
            self.stop_message.emit()
