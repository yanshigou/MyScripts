# encoding: utf-8
import requests
import json
# 转换音频格式
# from pydub import AudioSegment
import base64
import tkinter as tk

api = 'https://apigwrest.open.rokid.com/api/v1/tts/TtsProxy/Tts'
headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=B5047C0D83B24C7588AB32A491E8061D;device_type_id=67739C5235964E44BD9BF2DEC1ACDEA3;device_id=725B7C36879A46F3A9A649B7E8A0F911;service=rest;version=1;time=1553483554;sign=7A9D102FD8F896FD0D2A59F19E008138;',
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


def TkWindow():
    root.title("---Rokid语音转换器---")
    lb = tk.Label(root, text="请输入需要转换的文字")
    lb2 = tk.Label(root, text="请输入转换后的文件名")

    btn = tk.Button(root, text='开始转换', command=toMP3)
    lb.pack()
    entry.pack()
    lb2.pack()
    entry2.pack()
    btn.pack()
    lb3.pack()
    root.geometry('300x200+800+400')
    # root.maxsize(500, 300)
    # root.minsize(500, 300)
    root.mainloop()


def toMP3():
    try:
        text = entry.get()
        mp3_name = entry2.get()
        print(mp3_name[-3:])
        if mp3_name[-3:] != "mp3":
            mp3_name += ".mp3"
        res = post_api(text).json()
        mp3 = '{}'.format(res['voice'])
        decode_mp3 = base64.b64decode(mp3)
        # print(decode_mp3)
        f = open(mp3_name, 'wb+')
        f.write(decode_mp3)
        f.close()
        print('ok')
        lb3.config(text="转换完成：" + mp3_name)
    except:
        lb3.config(text="格式有误，请重新输入")


if __name__ == '__main__':
    # text = "没有网络，请连接后再试"
    # text = sys.argv[1]
    # mp3_name = sys.argv[2]
    # res = post_api(text).json()
    # mp3 = '{}'.format(res['voice'])
    # decode_mp3 = base64.b64decode(mp3)
    # # print(decode_mp3)
    # f = open(mp3_name, 'wb+')
    # f.write(decode_mp3)
    # f.close()
    # print('ok')
    # test = AudioSegment.from_file('C:\\Users\\Administrator\\Desktop\\test.mp3', format='mp3')
    # print(test)
    root = tk.Tk()
    entry = tk.Entry(root, fg="black")
    entry2 = tk.Entry(root, fg="black")
    lb3 = tk.Label(root, text="")
    TkWindow()


