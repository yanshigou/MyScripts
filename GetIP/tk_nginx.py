# encoding: utf-8
import traceback
from email_send import sendMail
from datetime import datetime
import tkinter as tk
import tkinter.filedialog
from AnalysisLog import GetAccessIp, GetErrorIP


def TkWindow():
    root.title("---NginxLog分析器---")
    lf = tk.LabelFrame(root, text='请选择收件人')
    lf.pack()

    rb1 = tk.Checkbutton(lf, text='dzt', variable=dzt)
    rb2 = tk.Checkbutton(lf, text='dyh', variable=dyh)
    rb3 = tk.Checkbutton(lf, text='dj', variable=dj)
    rb1.grid(row=0, column=0, padx=11)
    rb2.grid(row=0, column=1, padx=11)
    rb3.grid(row=0, column=2, padx=11)
    btn = tk.Button(root, text='选择文件', command=files)
    btn2 = tk.Button(root, text='一件发送邮件', command=file)
    lb.pack()
    lb2.pack()
    # lb.grid(row=0, column=0, pady=10)
    btn.pack()
    btn2.pack()
    # btn.grid(row=20, columnspan=20, pady=20)

    root.geometry('500x200+800+400')
    # root.maxsize(500, 300)
    # root.minsize(500, 300)
    root.mainloop()


def file():
    filename = tk.filedialog.askopenfilename()
    datetime_now = datetime.now()
    date = datetime_now.strftime("%Y-%m-%d")
    print(dzt.get(), dyh.get(), dj.get())
    to_mail = []
    if dzt.get() == 1:
        to_mail.append('dongzhetong@cmx-iot.com')
    if dyh.get() == 1:
        to_mail.append('dengyuhao@cmx-iot.com')
    if dj.get() == 1:
        to_mail.append('daijian@cmx-iot.com')
    print(to_mail)
    if filename != "":
        lb2.config(text="您选择的需要发送的文件："+filename)
        f = open(filename, 'rb')
        content = ''
        for i in f.readlines():
            content += i.decode('utf-8')
        print(content)
        res = sendMail(content, date, filename, to_mail)
        if res is True:
            lb2.config(text=filename + "发送成功")
        else:
            lb2.config(text=res)
    else:
        lb2.config(text="您没有选择任何需要发送的文件")


def files():
    filenames = tkinter.filedialog.askopenfilenames()
    datetime_now = datetime.now()
    date = datetime_now.strftime("%Y-%m-%d")
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0, len(filenames)):
            path = str(filenames[i])
            # 传access.log
            # if path[-10:] == "access.log":
            #     output_access = path[:-4] + str(datetime.now())[0:10] + '.txt'
            #     print(path)
            #     print(output_access)
            # elif path[-9:] == "error.log":
            #     output_error = path[:-4] + str(datetime.now())[0:10] + '.txt'
            #     print('error')
            #     print(path)
            #     print(output_error)

            # 传access2019-04-14.log
            try:
                if "access" in path and ".log" in path:
                    # output_access = path[:-4] + '.txt'
                    # output_access = 'outLog.txt'
                    output_access = date + 'outLog.txt'
                    print(path)
                    print(output_access)
                    GetAccessIp(path, output_access)
                    string_filename += str(filenames[i]) + " 分析完成！！" + "\n"
                    print(str(filenames[i]) + " 分析完成！！" + "\n")
                elif "error" in path and ".log" in path:
                    # output_error = path[:-4] + '.txt'
                    # output_error = 'outLog.txt'
                    output_error = date + 'outLog.txt'
                    print(path)
                    print(output_error)
                    GetErrorIP(path, output_error)
                    string_filename += str(filenames[i]) + " 分析完成！！" + "\n"
                    print(str(filenames[i]) + " 分析完成！！" + "\n")
                else:
                    string_filename += str(filenames[i]) + " 分析失败！！" + "\n"
                lb.config(text="您选择的需要分析文件：" + string_filename)
            except:
                traceback.print_exc()
                lb.config(text=string_filename+"分析失败，请检查格式是否正确\n或重新单个分析")
    else:
        lb.config(text="您没有选择任何需要分析的文件")


if __name__ == '__main__':
    root = tk.Tk()
    lb = tk.Label(root, text="您没有选择任何需要分析的文件")
    lb2 = tk.Label(root, text="您没有选择任何需要发送的文件")
    dzt = tk.IntVar(root, value=0)
    dyh = tk.IntVar(root, value=0)
    dj = tk.IntVar(root, value=0)
    TkWindow()
