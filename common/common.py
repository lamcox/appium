#encoding:utf-8
import re
import subprocess

#app安装包的路径
appLocation = "//Users//yaulola//Public//appium-Android//app//android-debug.apk"

def get_desiredCaps():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = platformVersion()
    desired_caps['deviceName'] = deviceName()
    desired_caps['appPackage'] = appPackage()
    desired_caps['appActivity'] = appActivity()
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    return desired_caps

def url():
    u = "http://127.0.0.1:4723/wd/hub"
    return u

def deviceName():
    cmd = "adb devices"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = output.split()[4].decode()
    return result

def platformVersion():
    cmd = "adb shell getprop ro.build.version.release"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = output.split()[0].decode()
    return result

def deviceModel():
    cmd = "adb shell getprop ro.product.model"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = ''.join(output.decode().split())
    return result

def appPackage():
    cmd = "aapt dump badging "+appLocation
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        #通过正则获取appPackage
        result = re.findall(r"name='(.+?)' versionCode",output.decode())[0]
    return result

def appActivity():
    cmd = "aapt dump badging "+appLocation
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        #通过正则获取appActivity
        result = re.findall(r"name='(.+?)'  label",output.decode())[0]
    return result