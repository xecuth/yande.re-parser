import random
import requests
import shutil
import os
import time
from lxml import html


class Parser:
    def __init__(self, settings, status_output=print, message_output=print, pb_inc=None):
        self.session = requests.Session()
        self.session.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
        self.settings = settings
        self.status_output = status_output
        self.message_output = message_output
        self.pb_inc = pb_inc
        self.urls_of_images = []

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
            self.message_output(f"ERROR: {e}")
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
                return self.message_output("Program not found arts, sorry about that(")

            for x in images:
                self.urls_of_images.append(x.attrib["href"])

            self.settings['page_count'] -= 1
            time.sleep(.5)

        self.message_output(f"Found {len(self.urls_of_images)} arts, start download")

    def parsing(self):
        self.message_output('Downloading...')

        if not self.urls_of_images:
            self.get_image_urls()
        pic_num = 1
        for x in self.urls_of_images:
            pic_name = self.download_image(x)
            if pic_num:
                self.status_output(f"[{pic_num}/{len(self.urls_of_images)}] Final download image {pic_name}")
            else:
                self.status_output(f"[{pic_num}/{len(self.urls_of_images)}] Error while loading image")
            pic_num += 1
            self.pb_inc()
            time.sleep(0.5)

        self.message_output('All pictures downloaded')
        self.status_output('Done!')
