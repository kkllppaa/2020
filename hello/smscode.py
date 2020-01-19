import requests
import urllib.request
import re,random,time

# f=open('headers.txt','r')
# my_headers=[i.strip('\n')strip() for i in f]

# f=open('proxy.txt','r')
# my_proxys=[i.strip('\n') for i in f]

# proxy = random.choice(my_proxys)
# header = random.choice(my_headers)
# print (proxy, header)
# proxy_handler = urllib.request.ProxyHandler({"http" : proxy})
# opener = urllib.request.build_opener(proxy_handler)
# urllib.request.install_opener(opener)
url='https://www.yinsiduanxin.com/dl/18.html'
# res=urllib.request.Request(url,headers={'User-Agent':header})  
# html=urllib.request.urlopen(res,timeout=3).read()


res=urllib.request.Request(url)  
html=urllib.request.urlopen(res,timeout=3).read()
html=html.decode('utf-8')

reg=r'<div class="layui-col-lg4 layui-col-md4 layui-col-sm6 layui-col-xs12 card">.*?</div>'
urls=re.findall(reg,re.S)
print(urls)