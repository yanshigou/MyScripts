# -*- coding: utf-8 -*-
__author__ = 'dzt'
__date__ = '2019/02/12 16:13'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase


def sendMail(body, date, attachment=None, to_mail=None):
    try:
        smtp_server = 'smtp.qq.com'
        from_mail = 'yanshigou@foxmail.com'
        mail_pass = 'tofjtcnjcplcbbbh'
        # to_mail = ['dongzhetong@cmx-iot.com', 'daijian@cmx-iot.com']  # 列表多个
        if to_mail == (None or []):
            print('None or []')
            return "请勾选收件人"
        # 构造一个MIMEMultipart对象代表邮件本身
        msg = MIMEMultipart()
        # Header对中文进行转码
        # msg['From'] = ('dongzhetong@cmx-iot.com<%s>' % from_mail)
        msg['From'] = ('董哲彤<%s>' % "dongzhetong@cmx-iot.com")
        msg['To'] = ','.join(to_mail)
        msg['Subject'] = Header("【日常log分析】" + date, 'utf-8').encode()
        # plain代表纯文本
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        # 二进制方式模式文件
        with open(attachment, 'rb') as f:
            file_name = attachment.split('/')[-1]
            # MIMEBase表示附件的对象
            mime = MIMEBase('text', 'txt', filename=attachment)
            # filename是显示附件名字
            mime.add_header('Content-Disposition', 'attachment', filename=file_name)
            # 获取附件内容
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            # 作为附件添加到邮件
            msg.attach(mime)
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_mail, mail_pass)
        # print('kaishi')
        # print(type(msg))
        server.sendmail(from_mail, to_mail, msg.as_string())  # as_string()把MIMEText对象变成str
        server.quit()
        return True
    except Exception as e:
        print(e)
        return e


# if __name__ == "__main__":
#     f = open('outLog.txt', 'rb')
#     content = ''
#     for i in f.readlines():
#         content += i.decode('utf-8')
#     print(content)
#     sendMail(content)
