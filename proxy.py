import requests,random,time
import tkinter as tk
import pyperclip
import tkinter.messagebox as msgbox

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

Win = tk.Tk()
Win.title('IP代理池')
Win.geometry('500x650+400+10')
url='http://118.24.52.95/get_all/'
proxy_lists=[ ]
proxy_testlist=[ ]

def btnGet_click():
    
    #text1.delete('1.0','end') # proxy_lists=[ ]
    try:
        response=requests.get(url).text
        response=eval(response)
        for proxy_dict in response: 
            if proxy_dict['proxy'] not in proxy_lists:
                proxy_lists.append(proxy_dict['proxy'])
                print(proxy_lists.index(proxy_dict['proxy'])+1,proxy_dict['proxy'])
                text1.insert(tk.INSERT, ('\"'+proxy_dict['proxy']+'\"'+','+'\n'))
                btnGet = tk.Button(Win, text=len(proxy_lists), width=6, command=btnGet_click).grid(row=2, column=0)
    except:
        msgbox.showerror('获取失败','请勿频繁点击')
    time.sleep(1)  

def btnCopy_click():
    pyperclip.copy(text1.get('1.0','end'))
    pyperclip.paste()
    print('copy')


def btnGet2_click():
    # btnGet_click()
    if entry1.get()=='':
        msgbox.showinfo('提醒','请先输入正确的网址')
    else:
        url=entry1.get()
        header = random.choice(my_headers)
        # proxy_lists2=eval(text1.get('1.0','end'))
        # print(text1.get('1.0','end'))
        for proxy in proxy_lists:
            try:
                print(proxy)
                proxies={
                'http':'http://'+proxy,
                'https':'https://'+proxy,
                }
                response=requests.get(url,headers={'User-Agent':header},proxies=proxies,timeout=2)
                if response.status_code==200 and proxy not in proxy_testlist:
                    proxy_testlist.append(proxy)
                    text2.insert(tk.INSERT,('\"'+proxy+'\"'+','+'\n'))
                    print('success:'+proxy)
                    print(len(proxy_testlist))            
            except:
                pass
            continue        
        print('oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
        print(len(proxy_testlist))
def btnCopy2_click():
    pyperclip.copy(text2.get('1.0','end'))
    pyperclip.paste()
    print('copy22222222')
 

label1= tk.Label(Win, text="IP池").grid(row=0, column=0,columnspan=2)
text1=tk.Text(Win,width=30,height=45)
text1.grid(row=1, column=0,columnspan=2)
btnGet = tk.Button(Win, text="获取", width=6, command=btnGet_click).grid(row=2, column=0)
btnCopy = tk.Button(Win, text="复制", width=6, command=btnCopy_click).grid(row=2, column=1)

label2= tk.Label(Win, text="筛选IP URL:").grid(row=0, column=2,columnspan=2)
varName=tk.StringVar(value='https://www.baidu.com/')
entry1= tk.Entry(Win,textvariable=varName)
entry1.grid(row=0, column=4, columnspan=2)
text2=tk.Text(Win,width=30,height=45)
text2.grid(row=1, column=3,columnspan=2)
btnGet2 = tk.Button(Win, text="筛选", width=6, command=btnGet2_click).grid(row=2, column=3)
btnCopy2 = tk.Button(Win, text="复制", width=6, command=btnCopy2_click).grid(row=2, column=4)



Win.mainloop()