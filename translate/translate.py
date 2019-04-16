from urllib import request
from urllib import parse
import json
import tkinter as tk
import tkinter.font as tkFont


def spider(words):
    # words = input("请输入需要翻译的文字！")
    words = words
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {'i': words, 'doctype': 'json'}
    utf_data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    html = request.urlopen(req, data=utf_data).read().decode("utf-8")
    json_data = json.loads(html)
    print(json_data['translateResult'][0][0]['tgt'])
    return json_data['translateResult'][0][0]['tgt']


def TkWindow():
    root.title("---中英文互翻器---")
    lb = tk.Label(root, text="请输入需要翻译的文字(自动检测中英文)")
    btn = tk.Button(root, text='开始翻译', command=toMP3)
    lb.pack()
    entry.pack()

    btn.pack()
    lb3.pack()
    root.geometry('800x200+800+400')
    root.maxsize(800, 200)
    root.minsize(500, 200)
    root.mainloop()


def toMP3():
    try:
        words = entry.get()
        res = spider(words)
        ft = tkFont.Font(family='Fixdsys', size=10, weight=tkFont.BOLD)
        lb3.config(text=res, font=ft, justify='left', wraplength=700)
    except:
        lb3.config(text="格式有误，请重新输入")


if __name__ == '__main__':
    # while True:
    #     spider()
    root = tk.Tk()
    entry = tk.Entry(root, width=120, fg="black")
    lb3 = tk.Label(root, text="")
    TkWindow()
