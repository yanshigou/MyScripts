# -*- coding: utf-8 -*-
__author__ = 'dzt'
__date__ = '2018/09/10 12:13'

from django.core.mail import send_mail
from test_celery.settings import EMAIL_FROM
import requests
from time import sleep
from datetime import datetime


def send_register_email(email, res=None, error=None):
    if res is None:
        email_title = u'监听nginx情况{0}'.format(datetime.now())
        email_body = u'Nginx服务器似乎出了问题，\r\n{0}，\r\n请立即查看'.format(error)
    else:
        status_code = res.status_code
        json = res.json()
        email_title = u'监听nginx情况{0}'.format(datetime.now())
        email_body = u'Nginx服务器似乎出了问题，\r\n状态码{0}，\r\n{1}，\r\n请立即查看。'.format(status_code, json)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass


def listen_nginx():
    url = '访问地址'
    res = requests.get(url=url)
    # print(res.status_code)
    # print(type(res.status_code))
    return res


if __name__ == '__main__':
    c = 0
    while True:
        sleep(60)
        try:
            res = listen_nginx()
            if res.status_code != 200:
                print('not 200', datetime.now())
                c += 1
                send_register_email('dongzhetong@cmx-iot.com', res)
                if c == 5:
                    break
            else:
                print("is's ok", datetime.now(), c)
        except Exception as e:
            c += 1
            print('Exception！', datetime.now(), c)
            send_register_email('dongzhetong@cmx-iot.com', None, e)
            if c == 5:
                break

