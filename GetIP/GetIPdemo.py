# encoding: utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import pandas as pd
import linecache
import re
from datetime import datetime
import requests
time1 = datetime.now()


#提取ip地址，去重，获取不同ip个数
def GetAccessIp(input_file_name,output_file_name):
    sep = '\n'
    sep1 = '*'*50 + '\n'
    sep2 = '\n' + '*'*50 + '\n\n'
    ip_list=[]
    timelist = []

    fLog = open(input_file_name)
    for each in fLog:
        ip=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',str(each),re.S)
        ip_list.append(ip[0])

        # 分割log中每行空格
        iptime = each.split()[3]
        timelist.append(iptime)

    count = 1
    countlist = []
    for x in range(len(timelist)-1):
        if timelist[x+1] == timelist[x]:
            count += 1
        else:
            countlist.append(count)
            count = 1

    # print(max(countlist))


    ips = list(set(ip_list))

    print("access不同ip个数:%s "% len(ips))

    #写
    fout = open(output_file_name, "a")

    for each in ips:
      # print(each)
      fout.write(each + sep)
    ip_count = {}
    for i in ips:
        ip_count[i] = ip_list.count(i)
    # print()

    fout.write(sep1 + timelist[0] + '] 至 ' + timelist[-1] + ']' + sep)
    fout.write("单秒最大访问量:%s"% max(countlist) + sep)
    fout.write("nginx访问ip个数:%s "% len(ips) + sep)
    fout.write("nginx一共访问量:%s"% len(ip_list) + sep)
    fout.write('最大5个访问ip:' + sep)
    temp = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]
    for i in temp:
        fout.write(str(i) + sep)

    fout.write('统计时间: ' + str(datetime.now()) + sep2)
    # print(ips)

    fout.close()
    fLog.close()
    print "ip提取完毕"


def GetErrorIP(input_file_name2,output_file_name2):
    sep = '\n'
    sep1 = '*'*50 + '\n'
    sep2 = '\n' + '*'*50 + '\n\n'
    ip_list = []
    err_list = []
    timelist = []
    alert_list = []
    errorL = []

    fLog = open(input_file_name2)
    for each in fLog:
        ip = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', str(each), re.S)
        # print(ip)

        err = re.findall(r'(?<=\d{6} ).*(?=, client)', str(each), re.S)
        err_list.append(err[0])

        # alert = re.findall(r'alert', str(each), re.S)
        # alert_list.append(alert[0])
        #
        # errorl = re.findall(r'error', str(each), re.S)
        # errorL.append(errorl[0])

        # err_list.append(each)
        errtime = each.split()[1]
        timelist.append(errtime)

        if ip == []:
            continue
        else:
            ip_list.append(ip[0])

    ips = list(set(ip_list))
    errs = list(set(err_list))

    # print(errs)
    print("error总数：%s" % len(err_list))
    print("error中不同ip个数:%s " % len(ips))
    print("error不同个数:%s " % len(errs))
    # print("alert个数:%s " % len(alert_list))
    # print("error个数:%s " % len(errorL))



    #写
    fout = open(output_file_name2, "a")
    for each in ips:
      # print(each)
      fout.write(each + sep)

    for each in errs:
        fout.write(each + sep)

    fout.write(sep1 + timelist[0] + ' 至 ' + timelist[-1] + sep)
    # fout.write("nginx error出现ip个数:%s "% len(ips) + sep)
    fout.write("nginx error类型个数:%s "% len(errs) + sep)
    fout.write("nginx 报错总数:%s "% len(err_list) + sep)

    # fout.write("nginx error总数:%s "% len(errorL) + sep)
    # x = len(err_list)-len(ip_list)
    # fout.write("nginx error次数:%s"% len(ip_list) + sep)
    # fout.write("nginx alert个数:%s "% x + sep)
    fout.write('统计时间: ' + str(datetime.now()) + sep2)
    # print(ips)

    fout.close()
    fLog.close()
    print "error提取完毕"



if __name__ == '__main__':
    input_file_name = "C:\\Users\\Administrator\\Desktop\\log\\access1028.log"
    output_file_name = "C:\\Users\\Administrator\\Desktop\\log\\output_access1028.txt"
    GetAccessIp(input_file_name, output_file_name)
    input_file_name2 = "C:\\Users\\Administrator\\Desktop\\log\\error1028.log"
    output_file_name2 = "C:\\Users\\Administrator\\Desktop\\log\\output_error1028.txt"
    GetErrorIP(input_file_name2, output_file_name2)
    time2 = datetime.now()
    print ('总共耗时：' + str(time2 - time1) + 's')

## (?<=\d{6} ).*(?=, client) 尝试了许久获取的截取error.log中报错信息