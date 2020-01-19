import requests,random,time
import urllib.request

f=open('headers.txt','r')
my_headers=[i.strip('\n').strip() for i in f]
f=open('proxy.txt','r')
ip_list=[i.strip('\n') for i in f]
# for ip in a:
#     ip_list.append(ip.strip('\n'))
print(my_headers)
print(ip_list)





# ]
# url='http://118.24.52.95/get_all/'
# header = random.choice(my_headers)

# for proxy in proxy_list:
#     try:
#         print(proxy)
#         proxies={
#             'http':'http://'+proxy,
#             'https':'https://'+proxy,
#         }
#         response=requests.get(url,headers={'User-Agent':header},proxies=proxies)
#         print('success:'+response.text)
#     except:
#         pass
#     continue
# print('oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')

# try:
# response=requests.get(url).json
# print(response)
# html=urllib.request.urlopen(response,timeout=3).read()
# print(html)
    #     response=eval(response)
#     for proxy_dict in response: 
#         if proxy_dict['proxy'] not in proxy_lists:
#             proxy_lists.append(proxy_dict['proxy'])
#             print(proxy_lists.index(proxy_dict['proxy'])+1,proxy_dict['proxy'])
#             text1.insert(tk.INSERT, ('\"'+proxy_dict['proxy']+'\"'+','+'\n'))
#             btnGet = tk.Button(Win, text=len(proxy_lists), width=6, command=btnGet_click).grid(row=2, column=0)
# except:
#     print('oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
