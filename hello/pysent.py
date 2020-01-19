from pymouse import PyMouse
from pykeyboard import PyKeyboard
 
from win32 import win32gui
import tkinter as tk
import tkinter.messagebox as msgbox
import os,time,random
import schedule

sentWin = tk.Tk()
sentWin.title('自动发送')
sentWin.geometry('400x100+500+200')

k=PyKeyboard()
m=PyMouse()
names=['福','fly']  
a= win32gui.FindWindow("ChatWnd",names[0]) # 获取窗口的句柄，参数1: 类名，参数2： 标题QQ
b= win32gui.FindWindow("ChatWnd",names[1])
list1=['11111','2222222222','33333333']


def wxlogin():
    os.system(r'"C:\Program Files\Tencent\WeChat\WeChat.exe"')
    if a==0 and b==0:
        msgbox.showinfo('提醒','请先登录微信并打开所有要发送用户或者群窗口')
        sentWin.quit()
    else:
        msgbox.showinfo('提醒','登录成功')
    
def senta():
    list=random.sample(list1,1)[0]
    win32gui.SetForegroundWindow(a)
    print(list)
    time.sleep(3)

    k.tap_key(k.enter_key)
    k.type_string(list)
    time.sleep(3)
    k.tap_key(k.enter_key)
    k.tap_key(k.enter_key)
     
def sentb():
    list=random.sample(list1,1)[0]
    win32gui.SetForegroundWindow(b)
    print(list)
    time.sleep(3)

    k.tap_key(k.enter_key)
    k.type_string(list)
    time.sleep(3)
    k.tap_key(k.enter_key)
    k.tap_key(k.enter_key)

def sent():
    if a!=0 and b!=0:
        schedule.every(15).seconds.do(senta)
        time.sleep(5)
        schedule.every(30).seconds.do(sentb)
        while True:
            schedule.run_pending()
    elif a==0 and b!=0:
        schedule.every(30).seconds.do(sentb)
        while True:
            schedule.run_pending()
    elif a!=0 and b==0:
        schedule.every(15).seconds.do(senta)
        while True:
            schedule.run_pending()

btnLogin = tk.Button(sentWin, text="登录", width=20, command=wxlogin)
btnLogin.grid(row=0, column=1)
btnLogin = tk.Button(sentWin, text="发送", width=20, command=sent)
btnLogin.grid(row=0, column=2)
sentWin.mainloop()



    # schedule.every(1).minutes.do(job3)
    # schedule.every().day.at('17:49').do(job4)
    # schedule.every(5).to(10).seconds.do(job5)
