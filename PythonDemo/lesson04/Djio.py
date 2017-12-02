import re
import requests
from requests.exceptions import RequestException
url='http://service.shmetro.com/czxx/index.htm'
response=requests.get(url)
print(response.text)

from requests.exceptions import RequestException
def get_url(url):
 try:
    response=requests.get(url)
    if response==200:
        return response.text
    return None
 except RequestException:
     return None

def get_sp(html):
    partern=re.compile('',re.S)
    result=re.findall(partern,html)
    for item in result:
        yield {
            'station':item[0]
        }

def main():
    url='http://service.shmetro.com/czxx/index.htm'
    html=get_url(url)
    for item in get_sp(html):
        print(item)

if __name__=='__main__':
    main()

'''
 '<div class="name"
id="lineName">.*?<a
class="selcet site".*>?
title="徐泾东">(.*?)</a>.*?<a class onclick=".*?">.*?(.*?)</a>.*?</div>‘

'''