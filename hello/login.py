import tkinter as tk
import tkinter.messagebox as msgbox


def btnOkClick():
    if entName.get() == "hjf" and entPass.get() == "123":
        mainWin = tk.Tk()
        mainWin.title("登录成功")
        mainWin.geometry("500x300+400+200")
    else:
        msgbox.showinfo("消息", "用户名或密码错误")

def btnResetClick():
    varName.set("")
    varPass.set("")


loginWin = tk.Tk()
loginWin.title('登录')
loginWin.geometry('300x200+500+200')

lblName = tk.Label(loginWin, text="用户名").grid(row=0, column=0, ipadx=20, ipady=10)

varName=tk.StringVar()
entName = tk.Entry(loginWin, textvariable=varName)
entName.grid(row=0, column=1, columnspan=2)

lblPass = tk.Label(loginWin, text="密码").grid(row=1, column=0, ipadx=20, ipady=10)

varPass=tk.StringVar()
entPass = tk.Entry(loginWin, show="*", textvariable=varPass)
entPass.grid(row=1, column=1, columnspan=2)

btnReset = tk.Button(loginWin, text="重置", width=6, command=btnResetClick).grid(row=2, column=2)
btnOk = tk.Button(loginWin, text="登录", width=6, command=btnOkClick).grid(row=2, column=1)

loginWin.mainloop()
