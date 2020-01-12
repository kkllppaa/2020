import tkinter as tk
from tkinter import messagebox
import requests

transWin = tk.Tk()
transWin.title('中英互译')
transWin.geometry('400x100+500+200')


def btnTrans_Click():
    content=ent1.get().strip()
    if content=="":
        messagebox.showinfo("提示","请输入要翻译的文字")
    else:
        
        """ i: hello
            from: AUTO
            to: AUTO
            smartresult: dict
            client: fanyideskweb
            salt: 15783843777672
            sign: b2caf7443f8a3b7d94f0f19d8ae204de
            ts: 1578384377767
            bv: c25ca85e2b75734d758fc2a6d81c50e7
            doctype: json
            version: 2.1
            keyfrom: fanyi.web
            action: FY_BY_CLICKBUTTION"""
        dic={}
        dic["i"]=content
        #dic["from"]="AUTO"
        #dic["to"]="AUTO"
        #dic["smartresult"]="dict"
        dic["doctype"]="json"
        #dic["version"]="2.1"
        #dic["keyfrom"]="fanyi.web"
        #dic["action"]="FY_BY_CLICKBUTTION"
       
        
        
        url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        res= requests.post(url,data=dic)
        result=res.json()
        trans=result["translateResult"][0][0]["tgt"]
        print(trans)
        varTrans.set(trans)

lbl1 = tk.Label(transWin, text="请输入要翻译的文字")
lbl1.grid(row=0, column=0, ipadx=20,)
lbl2 = tk.Label(transWin, text="翻译结果")
lbl2.grid(row=1, column=0, ipadx=20,ipady=10)

ent1 = tk.Entry(transWin)
ent1.grid(row=0, column=1, columnspan=2)
varTrans=tk.StringVar()
ent2 = tk.Entry(transWin, textvariable=varTrans)
ent2.grid(row=1, column=1, columnspan=2)
btnTrans = tk.Button(transWin, text="翻译", width=20, command=btnTrans_Click)
btnTrans.grid(row=2, column=1)


transWin.mainloop()