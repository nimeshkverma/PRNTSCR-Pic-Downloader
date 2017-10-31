import re
import sys
import uuid
import requests
import shutil


class PrntscrPicDownloader(object):
    """Class for PrntscrPicDownloader"""

    def __init__(self, prntscr_urls):
        self.prntscr_urls = prntscr_urls
        self.pic_urls = self.__get_pic_urls()

    def __get_pic_url_from_html(self, html_code):
        pic_url = None
        pic_url_patterns = re.findall(
            r"<img class=\"image__pic js-image-pic\" src=\"([a-zA-Z,0-9,:,/,\.]+)\" alt", html_code)
        if pic_url_patterns:
            pic_url = pic_url_patterns[0]
        return pic_url

    def __get_pic_urls(self):
        pic_urls = dict()
        for prntscr_url in self.prntscr_urls:
            pic_webpage_response = requests.get(prntscr_url)
            pic_webpage_response_html = pic_webpage_response.text
            if pic_webpage_response.status_code is not 200:
                pic_webpage_response_html = ''
            pic_urls[prntscr_url] = self.__get_pic_url_from_html(
                pic_webpage_response.text)
        return pic_urls

    def __get_file_name(self, pic_url, prntscr_url):
        pic_url_paterns = re.findall(r"http://prntscr.com/([a-zA-Z,0-9])")
        prntscr_url_paterns = re.findall(
            r"https://image.prntscr.com/image/([a-zA-Z,0-9,\.])")
        if pic_url_paterns:
            return pic_url_paterns[0] + ".png"
        elif prntscr_url_paterns:
            return prntscr_url_paterns[0]
        else:
            return uuid.uuid4().hex

    def go(self):
        for prntscr_url, pic_url in self.pic_urls.iteritems():
            response = requests.get(prntscr_url, stream=True)
            file_name = self.__get_file_name(pic_url, prntscr_url)
            if response.status_code == 200:
                with open(file_name, 'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
            else:
                print "Can't download the Pic for the {url}".format(url=prntscr_url)

if __name__ == '__main__':
    PrntscrPicDownloader(sys.argv[1:]).go()
