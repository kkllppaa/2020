import requests
import urllib.request
import re,random,time


my_headers = [    
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",    
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",    
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",    
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",    
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',    
    'Opera/9.25 (Windows NT 5.1; U; en)',    
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',    
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',    
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',    
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',    
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",    
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
    ]
my_proxys = [
    "123.57.152.252:3128",
    "31.220.55.166:8080",
    "37.187.116.199:80",
    "101.95.115.196:8080",
    "14.20.235.7:808",
    "183.154.54.242:9999",
    "196.22.249.124:80",
    "202.112.51.45:3128",
    "46.105.51.183:80",
    "43.254.168.56:53281",
    "101.4.136.34:81"

]

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