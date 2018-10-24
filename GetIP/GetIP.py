# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
    print("不同ip个数:%s "% len(ips))

    #写
    fout = open(output_file_name, "a")

    for each in ips:
      # print(each)
      fout.write(each + sep)

    fout.write(sep1 + timelist[0] + '] 至 ' + timelist[-1] + ']' + sep)
    fout.write("单秒最大访问量:%s"% max(countlist) + sep)
    fout.write("nginx访问ip个数:%s "% len(ips) + sep)
    fout.write("nginx一共访问量:%s"% len(ip_list) + sep)

    fout.write('统计时间: ' + str(datetime.now()) + sep2)
    # print(ips)

    fout.close()
    fLog.close()
    print "ip提取完毕"


def GetErrorIP(input_file_name,output_file_name):
    sep = '\n'
    sep1 = '*'*30 + '\n'
    sep2 = '\n' + '*'*30 + '\n\n'
    ip_list=[]
    pass





if __name__ == '__main__':
    input_file_name = "D:\\dzt\\access.log"
    output_file_name = "D:\\dzt\\output_access.txt"
    GetAccessIp(input_file_name, output_file_name)
    input_file_name2 = "D:\\dzt\\error.log"
    output_file_name2 = "D:\\dzt\\output_error.txt"
    GetErrorIP(input_file_name2, output_file_name2)
    time2 = datetime.now()
    print ('总共耗时：' + str(time2 - time1) + 's')