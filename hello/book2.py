import random,time
from selenium import webdriver

start=time.perf_counter()
browser = webdriver.Chrome()
browser.set_page_load_timeout(5)
# browser.get('http://www.quanshuwang.com/')
urls=[]
def get_hrefs():
    try:
        url = 'http://www.quanshuwang.com/book/44/44683'
        browser.get(url)
        time.sleep(3)
        hrefs = browser.find_element_by_xpath('//*[@id="chapter"]/div[3]/div[3]/ul/div[2]').find_elements_by_tag_name(
            'a')
        for href in hrefs:
            urls.append([href.text,href.get_attribute('href')])
        print(len(urls))
    except Exception as e:
        print(e)
        print('11111111111111111111111')
        time.sleep(2)
        return get_hrefs()

    for list in urls:
        title,url=list
        def get_contents():
            try:
                print(title, url)
                browser.get(url)
                contents=browser.find_element_by_xpath('//*[@id="content"]').text
                with open ('dldl.txt','a')as f:
                    f.write(contents)
                    print('oooooooooooooooooooo')
                    time.sleep(2)
            except :
                # browser.refresh()
                print('22222222222222222')
                time.sleep(2)
                return  get_contents()
        get_contents()
get_hrefs()
time.sleep(10)
end=time.perf_counter()
print(end-start )

