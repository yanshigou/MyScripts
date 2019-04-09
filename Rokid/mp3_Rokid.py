# encoding: utf-8
import requests
import json
# 转换音频格式
# from pydub import AudioSegment
import base64
import sys

api = 'https://apigwrest.open.rokid.com/api/v1/tts/TtsProxy/Tts'
headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=替换;device_type_id=替换;device_id=替换;service=rest;version=1;time=1553483554;sign=替换;',
        'User-Agent':
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    }


def post_api(text):
    body = {
        "text": text,
        "declaimer": "zh",
        "codec": "mp3"
    }
    res = requests.post(api, headers=headers, data=json.dumps(body))
    return res


def write_mp3(mp3):
    decode_mp3 = base64.b64decode(mp3)
    print(decode_mp3)
    f = open('a.mp3', 'wb+')
    f.write(decode_mp3)
    f.close()


if __name__ == '__main__':
    # text = "没有网络，请连接后再试"
    text = sys.argv[1].decode('gbk')
    mp3_name = sys.argv[2]
    res = post_api(text).json()
    mp3 = b'{}'.format(res['voice'])
    decode_mp3 = base64.b64decode(mp3)
    # print(decode_mp3)
    f = open(mp3_name, 'wb+')
    f.write(decode_mp3)
    f.close()
    print('ok')
    # test = AudioSegment.from_file('C:\\Users\\Administrator\\Desktop\\test.mp3', format='mp3')
    # print(test)


