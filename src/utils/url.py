import re


class UrlUtils:
    @staticmethod
    def name(url):
        m = re.search('htmlonelove.top/([^/]*)/?', url)
        if m:
            return m.group(1)

    @staticmethod
    def page_name(url):
        m = re.search('htmlonelove.top/([^/]*)/([^/\.]*)/?', url)
        if m:
            return m.group(2)


