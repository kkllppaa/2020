import random,time
from selenium import webdriver

url='https://www.yinsiduanxin.com/message/17096414261.html'
browser = webdriver.Chrome()
browser.get(url)
browser.refresh()
p=browser.find_element_by_xpath('/html/body/div/div[2]/div[5]/div/table/tbody/tr[1]')
print(p.text)
browser.close()