import random,time
from selenium import webdriver

fh=open('headers.txt','r')
my_headers=[i.strip('\n').strip() for i in fh]
fp=open('proxy.txt','r')
my_proxys=[i.strip('\n') for i in fp]
header=random.choice(my_headers)
proxy = random.choice(my_proxys)
chome_options = webdriver.ChromeOptions()
chome_options.add_argument(('--proxy-server=http://' + proxy))
chome_options.add_argument(header)
browser = webdriver.Chrome(chrome_options=chome_options)
url = 'http://www.baidu.com'
browser.get(url)

time.sleep(1000)