# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get("https://www.baidu.com")    # 打开百度浏览器
wd.find_element_by_id("kw").send_keys("selenium")   # 定位输入框并输入关键字
wd.find_element_by_id("su").click()   #点击[百度一下]搜索
time.sleep(3)   #等待3秒
wd.quit()   #关闭浏览器
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
