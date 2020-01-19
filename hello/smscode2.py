import random,time
from selenium import webdriver

url='https://www.yinsiduanxin.com/dl/1.html'
browser = webdriver.Chrome()
browser.get(url)
browser.refresh()
online_lists=[]
offline_lists=[]
while offline_lists==[]:

    time.sleep(2)
# browser.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()
    ee1=browser.find_elements_by_class_name('layui-card')
    for e in ee1:
        try:
            p = e.find_element_by_class_name('layuiadmin-big-font')
            if '接收中'in e.text:
                print(p.get_attribute('id'))
                online_lists.append(p.get_attribute('id'))
                print(len(online_lists))
                with open('smscode.txt', 'a') as f:
                    f.write(p.get_attribute('id'))
                    f.write('\n')
            elif '离线中'in e.text:
                offline_lists.append(p.get_attribute('id'))
                print('fffffffffffff'+p.get_attribute('id'))

        except Exception as e:
            print(e)
            pass
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/ul/li[last()]/a').click()
print('ooooooooooooooooooooooooooooooooooooooo')
print(len(online_lists))

    # ee1=browser.find_elements_by_class_name('clickA')
    # print(len(ee1))
    # for e in ee1:
    #     print(e.text)

