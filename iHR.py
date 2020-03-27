#!/usr/bin/env python3
# www.iots.vip  
# Alliot  
# 2020-1-8  
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from time import strftime, localtime
# 忽略 requests 请求认证警告
requests.packages.urllib3.disable_warnings()
# 邮件设置
server = 'smtp.163.com'
port = '25'
sender = '发件人邮箱'
passwd = '密码(授权码)'
receiver = '收件人'
# i 人事签到接口地址
url = "https://www.ihr360.com/gateway/attendance/aggregate/attendance/api/sign/doSign"
# 抓包签到请求头
headersValue = {
    'Cookie': 'SESSION=XXXXXXXXXXXXXX; Path=/; HttpOnly',
    'accept': 'application/json;charset=UTF-8',
    'appKey': 'com.irenshi.personneltreasure',
    'appVersion': 'XXXX',
    'osVersion': 'XXXX',
    'udid': 'XXXXXX',
    'user-agent': 'IRENSHI_APP_AGENT',
    'os': 'Android',
    'irenshilocale': 'zh_CN',
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': '272',
    'Host': 'www.ihr360.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}
# 抓包请求 json
jsonValue = {
    "deviceToken": " ",
    "deviceType": "NORMAL",
    "latitude": XXX,
    "locationName": "XXX",
    "longitude": XXX,
    "phoneName": "MI6",
    "signSource": "APP",
    "wifiMac": "XXX",
    "wifiName": "Alliot",
}
# 签到方法
def doSign(url, jsonValue, headersValue):
    r = requests.post(url, json=jsonValue, headers=headersValue, verify=False)
    global results
    results = json.loads(r.text)
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    return results
# 邮件提醒方法
def sendMail(server, port, sender, passwd, msg):
    smtp = smtplib.SMTP()
    smtp.connect(server, port)
    smtp.login(sender, passwd)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()
    print('邮件发送成功email has send out !')
def newMail(status):
    msg = MIMEText(str(results), 'plain', 'utf-8')
    msg['From'] = formataddr(["AlliotSigner", sender])
    msg['To'] = formataddr(["Alliot", receiver])
    if status == None:
        msg['Subject'] = '打卡失败-_-!'
        print("打卡失败")
    else:
        msg['Subject'] = '自动打卡成功'
        print("打卡成功")
    sendMail(server, port, sender, passwd, msg)
# 签到并邮件通知结果,不用通知则改为 doSign(url, jsonValue, headersValue) 即可
newMail(doSign(url, jsonValue, headersValue)["data"])
# doSign(url, jsonValue, headersValue)
