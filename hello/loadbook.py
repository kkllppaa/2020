import requests
import urllib.request
import re,random,time

f=open('headers.txt','r')
my_headers=[i.strip('\n')strip() for i in f]

f=open('proxy.txt','r')
my_proxys=[i.strip('\n') for i in f]

def download():
    try:
        url='http://www.quanshuwang.com/book/44/44683'
        proxy = random.choice(my_proxys)
        header = random.choice(my_headers)
        print (proxy, header)
        proxy_handler = urllib.request.ProxyHandler({"http" : proxy})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)
        res=urllib.request.Request(url,headers={'User-Agent':header})  
        html=urllib.request.urlopen(res,timeout=3).read()
        html=html.decode('gbk')
        #<li><a href="http://www.quanshuwang.com/book/1/1379/7392650.html" 
        # title="引子 穿越的，共2712字">引子 穿越的</a></li>
        reg=r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
        urls=re.findall(reg,html)
        for url in urls:
            chaptUrl,chaptTitle=url
            # print(url)
            def download_article():  
                try: 
                    print(url)
                    proxy = random.choice(my_proxys)
                    header = random.choice(my_headers)
                    print (proxy, header) 
                    date=urllib.request.Request(chaptUrl,headers={'User-Agent':header})        
                    chapt=urllib.request.urlopen(date,timeout=3).read()
                    chapt=chapt.decode('gbk')
                    # print(chapt)
                    chapter_reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'        
                    chapter_reg = re.compile(chapter_reg,re.S)        
                    chapter_content = re.findall(chapter_reg,chapt)        
                    for content in chapter_content:                
                    #打印章节的内容            
                        content = content.replace("&nbsp;","")  
                    #把"&nbsp;"字符全都替换为""            
                        content = content.replace("<br />","")      
                    #把"<br/>"字符全部替换为""            
                        print(content) 
                        print(chaptTitle+'已完成')                        
                    time.sleep(3)#打印内容
                except:
                    return download_article()
            download_article()
    except:
        return download()          
download()