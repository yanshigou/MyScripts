# encoding: utf-8
import re
import numpy as np
from datetime import datetime
time1 = datetime.now()


#提取ip地址，去重，获取不同ip个数
def GetAccessIp(input_file_name, output_file_name):
    sep = '\n'
    sep1 = '*'*50 + '\n'
    sep1 = '*'*50 + '\n'
    sep2 = '\n' + '*'*50 + '\n\n'
    ip_list=[]
    timelist = []
    alltimelist = []
    requestlist = []
    requestlist2 = []

    fLog = open(input_file_name)
    for each in fLog:
        #匹配ip
        ip=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', str(each), re.S)
        ip_list.append(ip[0])

        # 分割log中每行空格
        iptime = each.split()[3]
        # print(iptime[-8:])  #为00:00:00格式时间
        timelist.append(iptime)
        #匹配每个小时
        alltime = re.findall(r'\:(20|21|22|23|[0-1]\d)', str(iptime), re.S)
        alltimelist.append(int(alltime[0]))

        #匹配请求类型
        request = re.findall(r'(?<= ").*(?=\?)', str(each), re.S)
        if request == []:
            request = re.findall(r'(?<= ").*(?= HTTP)', str(each), re.S)
            if request == []:
                request = re.findall(r'(?<= ").*', str(each), re.S)
        # print(request)
        requestlist.append(request[0])
    # print(requestlist)

    # 再在requestlist中匹配地址
    for ea in requestlist:
        request2 = re.findall(r'.*(?=\?)', str(ea), re.S)
        if request2 == []:
            request2 = re.findall(r'.*(?= HTTP)', str(ea), re.S)
            if request2 == []:
                request2 = re.findall(r'.*', str(ea), re.S)

        # print(request2)
        requestlist2.append(request2[0])
    # print(requestlist2)


    # 计算每个小时访问次数
    count1 = 1
    countlist1 = []
    alltimelist.sort()
    all = list(set(alltimelist))
    all.sort(key=alltimelist.index)

    for x in range(len(alltimelist)-1):
        if alltimelist[x+1] == alltimelist[x]:
            count1 += 1
        else:
            countlist1.append(count1)
            count1 = 1


    # #计算每种请求地址访问次数
    # count2 = 1
    # countlist2 = []
    # requestlist2.sort()
    # r = list(set(requestlist2))
    # r.sort()
    # # list2.sort(key=list1.index)
    # # print(requestlist2)
    #
    # for x in range(len(requestlist2)-1):
    #     if requestlist2[x+1] == requestlist2[x]:
    #         count2 += 1
    #     else:
    #         countlist2.append(count2)
    #         count2 = 1
    # # print(r)
    # # print(countlist2)

    #计算每秒最大访问量
    count = 1
    countlist = []
    tlists = []
    timelist.sort()

    for x in range(len(timelist)-1):
        if timelist[x] == timelist[x+1]:
            count += 1
        else:
            tlists.append(timelist[x])
            countlist.append(count)
            count = 1
    # print(countlist)
    print(max(countlist))
    aa = np.array(countlist)
    # print(a)
    # b为索引的排序的列表 从小到大排列  b[-1]为最大
    ba = np.argsort(aa)
    # print(b)
    # countlist.sort(key=countlist.index)

    #取出最大访问量的时间
    bb = list(ba[-20:])
    print(bb)
    maxtime = []
    maxcountlist = []
    for i in bb:
        maxtime.append(tlists[i])
        maxcountlist.append(countlist[i])
    print(maxtime)
    print(maxcountlist)

    # print(tlist)
    # print(len(tlists))
    # for x in range(len(countlist)-1):
    #     if countlist[x] == max(countlist):
    #         maxtime = tlists[x]
    #         break

    ips = list(set(ip_list))

    print("access不同ip个数:%s " % len(ips))

    #写
    fout = open(output_file_name, 'a+')
    a = all
    b = countlist1

    # API次数
    # c = r
    # d = countlist2



    # for each in ips:
      # print(each)
      # fout.write(each + sep)
    # ip_count = {}
    # for i in ips:
    #     ip_count[i] = ip_list.count(i)
    # print()

    fout.write(sep1 + timelist[0] + '] 至 ' + timelist[-1] + ']' + sep)
    fout.write("访问量:%s" % len(ip_list) + sep)
    fout.write("IP个数:%s " % len(ips) + sep)
    fout.write("单秒最大访问量:%s" % max(countlist) + sep)
    fout.write("单秒最大访问量时间:%s" % maxtime[-1] + sep)
    for h in range(len(a)-1):
        fout.write("%s点至%s点，访问量：%s次" % (a[h], a[h]+1, b[h])+sep)
    # API次数
    # for q in range(len(c)-1):
    #     fout.write("%s，%s次"%(c[q],d[q]) + sep)

    for i in range(1, len(maxtime)+1):
        fout.write("%s，%s次" % (maxtime[-i], maxcountlist[-i]) + sep)

    # fout.write('最大5个访问ip:' + sep)
    # temp = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]
    # for i in temp:
    #     fout.write(str(i) + sep)

    fout.write('统计时间: ' + str(datetime.now()) + sep2)

    fout.close()
    fLog.close()
    print("ip提取完毕")


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

        err = re.findall(r'(?<=\*).*(?=, client)', str(each), re.S)
        # err_list.append(err[0])
        # print(err[0])
        e = err[0].split()[1:]
        error = ' '.join(e)
        err_list.append(error)
        # print(error)

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
    # for each in ips:
    #   # print(each)
    #   fout.write(each + sep)

    for each in errs:
        fout.write(each + sep)

    fout.write(sep1 + timelist[0] + ' 至 ' + timelist[-1] + sep)
    # fout.write("nginx error出现ip个数:%s "% len(ips) + sep)
    fout.write("error类型个数:%s " % len(errs) + sep)
    fout.write("报错总数:%s " % len(err_list) + sep)

    # fout.write("nginx error总数:%s "% len(errorL) + sep)
    # x = len(err_list)-len(ip_list)
    # fout.write("nginx error次数:%s"% len(ip_list) + sep)
    # fout.write("nginx alert个数:%s "% x + sep)
    fout.write('统计时间: ' + str(datetime.now()) + sep2)
    # print(ips)

    fout.close()
    fLog.close()
    print("error提取完毕")


if __name__ == '__main__':
    input_file_name = "D:\\work_CMX\\log\\access2019-01-11.log"
    output_file_name = "D:\\work_CMX\\log\\output2019-01-11.txt"
    GetAccessIp(input_file_name, output_file_name)
    input_file_name2 = "D:\\work_CMX\\log\\error2019-01-11.log"
    # output_file_name2 = "D:\\work_CMX\\log\\output_error2018-11-18.txt"
    GetErrorIP(input_file_name2, output_file_name)
    time2 = datetime.now()
    print('总共耗时：' + str(time2 - time1) + 's')

## (?<=\d{6} ).*(?=, client) 尝试了许久获取的截取error.log中报错信息\
## (20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d 匹配时间
## (?<= ").*(?=\?) 匹配GET POST PUT地址