import requests

from src.db.authentication_data import AuthenticationData
from pyquery import PyQuery


class HttpUtils:
    @staticmethod
    def document(url):
        r = requests.get(url, auth=AuthenticationData.get())
        return r.content.decode("utf-8", "strict")

    @staticmethod
    def pages(project_url):
        user = AuthenticationData.get()
        r = requests.get(project_url, auth=AuthenticationData.get())
        pq = PyQuery(r.content.decode("utf-8", "strict"))
        result = {}
        for link in pq('a'):
            result[link.text] = {
                'url': link.attrib['href']
            }
        return result
