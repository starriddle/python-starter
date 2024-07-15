#!/usr/bin/python3

"""
网页截屏保存

使用 浏览器驱动 后台模拟页面并保存为图片

第三方库：selenium，Web 自动化测试工具
Web 驱动：chromedriver、MicrosoftWebDriver、geckodriver，保存至 python 解释器相同目录下

chromedriver：
  - 最新版：https://googlechromelabs.github.io/chrome-for-testing/#stable
  - 阿里云镜像：
    - 旧版：https://registry.npmmirror.com/binary.html?path=chromedriver/
    - 新版：https://registry.npmmirror.com/binary.html?path=chrome-for-testing/

MicrosoftWebDriver：
  - 官方：https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver?form=MA13LH

geckodriver：
  - 官方：https://github.com/mozilla/geckodriver
  - 阿里云镜像：https://registry.npmmirror.com/binary.html?path=geckodriver/
"""

from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--start-maximized')

driver = webdriver.Edge(options=options)
driver.get("https://www.baidu.com")
# 使用 javascript 获取实际页面尺寸
width = driver.execute_script("return Math.max("
                              "document.body.scrollWidth, document.body.offsetWidth, "
                              "document.documentElement.clientWidth, "
                              "document.documentElement.scrollWidth, "
                              "document.documentElement.offsetWidth);")
height = driver.execute_script("return Math.max("
                               "document.body.scrollHeight, document.body.offsetHeight, "
                               "document.documentElement.clientHeight, "
                               "document.documentElement.scrollHeight, "
                               "document.documentElement.offsetHeight);")
# 调整窗口大小
driver.set_window_size(width,height)
time.sleep(1)
driver.save_screenshot('baidu.png')
driver.quit()
