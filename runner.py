#coding=utf-8
from common import common
from HTMLTestReportCN import HTMLTestReportCN
import unittest
import time
import os

casefile = "./testCase/"
def createsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(casefile,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit

for root,dirs,files in os.walk("./result/screen"):
    for name in files:
        device = common.deviceModel()
        if name.startswith(device):
            os.remove(os.path.join(root,name))
            print("删除截图：" + os.path.join(root,name))

now = time.strftime("%Y-%m-%d_%H%M",time.localtime())
filepath = './result/report/' + now +'.html'
fp = open(filepath,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title='自动化报告',
    tester='lin'
)
runner.run(createsuite())
fp.close()