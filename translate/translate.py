from urllib import request
from urllib import parse
import json


def spider():
    words = input("请输入需要翻译的文字！")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {'i': words, 'doctype': 'json'}
    utf_data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    html = request.urlopen(req, data=utf_data).read().decode("utf-8")
    json_data = json.loads(html)
    print(json_data['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    while True:
        spider()
