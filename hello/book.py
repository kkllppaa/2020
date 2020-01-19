
import random,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# f=open('headers.txt','r')
# my_headers=[i.strip('\n').strip() for i in f]
# f=open('proxy.txt','r')
# my_proxys=[i.strip('\n') for i in f]
# header=random.choice(my_headers)
# # proxy = random.choice(my_proxys)
# chome_options = webdriver.ChromeOptions()
# # chome_options.add_argument(('--proxy-server=http://' + proxy))
# chome_options.add_argument(header)
# browser = webdriver.Chrome(chrome_options=chome_options)
browser = webdriver.Chrome()
url = 'http://www.quanshuwang.com/'
browser.get(url)
browser.find_element_by_xpath('//*[@id="bdcsMain"]').send_keys('斗罗大陆',Keys.ENTER)
time.sleep(1)
windows=browser.window_handles
browser.switch_to_window(windows[-1])
time.sleep(1)
try:
    for i in range(2):
        try:
            title=browser.find_element_by_xpath("//span/a[@title='斗罗大陆']").click()
        except:
            nextto=browser.find_element_by_xpath('//*[@id="pagelink"]/a[5]').click()  
except:
    print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
time.sleep(1)
windows=browser.window_handles
browser.switch_to_window(windows[-1])
reader=browser.find_element_by_xpath('//*[@id="container"]/div[2]/section/div/div[1]/div[2]/a[1]').click()  
time.sleep(1)                                     
hrefs=browser.find_element_by_xpath('//*[@id="chapter"]/div[3]/div[3]/ul/div[2]').find_elements_by_tag_name('a')
print(len(hrefs))
for href in hrefs:
    print(href.text,href.get_attribute('href'))

time.sleep(10)


