import requests,random,time

class Proxys():
    f=open('headers.txt','r')
    my_headers=[i.strip('\n').strip() for i in f]
    proxy_lists=[ ]
    proxy_testlist=[ ]
    def proxy_get(self,url='http://118.24.52.95/get_all/'):
        try:
            response=requests.get(url).text
            # print(response)
            response=eval(response)
            for proxy_dict in response : 
                if proxy_dict['proxy'] not in self.proxy_lists:
                    self.proxy_lists.append(proxy_dict['proxy'])
                    print(len(self.proxy_lists))
        except Exception as e:
            print('eee')
        
    def proxy_test(self,url_test='http://icanhazip.com/'):
        header = random.choice(self.my_headers)
        for proxy in self.proxy_lists:
            try:
                proxies={
                'http':'http://'+proxy,
                'https':'https://'+proxy,
                }
                response=requests.get(url_test,headers={'User-Agent':header},proxies=proxies,timeout=1)
                if response.status_code==200 and proxy not in self.proxy_testlist:
                    self.proxy_testlist.append(proxy)
                    print('success:'+proxy)
                    print(len(self.proxy_testlist))         
            except:
                print('eeeeeeeeeeeeeeeeee'+proxy)
                   
        print('oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
        print(len(self.proxy_lists))
        print(len(self.proxy_testlist))

    def proxy_txt (self):
        with open("proxy.txt","w") as f:
            for proxy in self.proxy_testlist:
                f.write(proxy)
                f.write('\n')




