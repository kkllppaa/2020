import tkinter as tk
import random
import pyperclip


def btnCopyClick():
    print(varName.get())
    pyperclip.copy(entName.get())
    pyperclip.paste()
    print("copy" )

def btnGetClick():
    x=['11111111111','22222222222','33333333333']
    a=random.sample(x,1)
    varName.set(a)
 

regWin = tk.Tk()
regWin.title('注册验证码')
regWin.geometry('300x200+500+200')
#手机号
lblName = tk.Label(regWin, text="手机号").grid(row=0, column=0, ipadx=20, ipady=10)
varName=tk.StringVar()
entName = tk.Entry(regWin, textvariable=varName)
entName.grid(row=0, column=1, columnspan=2)
btnGet = tk.Button(regWin, text="取号", width=6, command=btnGetClick).grid(row=1, column=1)
btnCopy = tk.Button(regWin, text="复制", width=6, command=btnCopyClick).grid(row=1, column=2)

# 验证码
lblCode = tk.Label(regWin, text="验证码").grid(row=2, column=0, ipadx=20, ipady=10)
varCode=tk.StringVar()
entCode = tk.Entry(regWin, textvariable=varCode)
entCode.grid(row=2, column=1, columnspan=2)

btnGet2 = tk.Button(regWin, text="接收", width=6, command=btnGetClick).grid(row=3, column=1)
btnCopy2 = tk.Button(regWin, text="复制", width=6, command=btnCopyClick).grid(row=3, column=2)

regWin.mainloop()