import requests
import re
import html
class Instagram(object):
    def __init__(self,username):
        self._username=username.strip()
        self._url='https://www.instagram.com/%s/?hl=en'%(self._username)
        self._html=self.get_html()
        self._bio=self.get_bio()
    def get_bio(self):
        string=re.findall('"biography":"(.*?)"',self._html)[0]
        return string
    def get_html(self):
        return requests.get(self._url).text

    @property
    def bio(self):
        return self._bio
if __name__=='__main__':
    Instagram('sdfgdsfgdsfgdsfgsdfgdsfgdsfgdsfgdsfgdfsgdsfgdsfgdsfgdsfgwethsdfghdsfgh')