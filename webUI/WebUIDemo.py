#调用安装好的selenium模块
from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
#无头模式添加，无浏览器弹出
option.add_argument('headless')
#生成一个ChromeDriver
driver = webdriver.Chrome()
#访问指定的url
driver.get('http://www.baidu.com')

#输入"腾讯"
driver.find_element_by_id('kw').send_keys('腾讯')
#点击'百度一下'按钮
driver.find_element_by_id('su').click()
#等待
sleep(2)
#点击第一条链接
driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').click()