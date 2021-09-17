import os
import subprocess
import tkinter as tk
import winreg as wg
from tkinter import filedialog
import win32api
import win32con
import psutil as pt
from win32com.shell import shell
import sys
import os

seno = 0
class PyWinDesign:
    def __init__(self, startwin):
        def resource_path(relative_path):
            if getattr(sys, 'frozen', False):# 是否Bundle Resource
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        def getPidByName(Str):
            pids = pt.process_iter()
            pidList = []
            for pid in pids:
                if pid.name() == Str:
                    pidList.append(pid.pid)
            return pidList

        def getpass():
            global seno
            try:
                key = wg.OpenKey(wg.HKEY_LOCAL_MACHINE, r"SOFTWARE\TopDomain\e-Learning Class Standard\1.00")
                passwd = wg.QueryValueEx(key, "UninstallPasswd")
                win32api.MessageBox(0, "密码获取成功!密码:" + str(passwd) + "PS:中括号里的为密码", "成功!", win32con.MB_ICONQUESTION)
            except:
                seno = 1

            if seno == 1:
                try:
                    key = wg.OpenKey(wg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\TopDomain\e-Learning Class "
                                                            r"Standard\1.00")
                    passwd = wg.QueryValueEx(key, "UninstallPasswd")
                    win32api.MessageBox(0, "密码获取成功!密码:" + str(passwd) + "PS:中括号里的为密码", "成功!", win32con.MB_ICONQUESTION)
                except:
                    win32api.MessageBox(0, "获取失败", "失败", win32con.MB_ICONQUESTION)
            else:
                pass

        def tkkill():
            subprocess.run("taskkill /f /t /im studentmain.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            win32api.MessageBox(0, "操作成功完成", "完成", win32con.MB_ICONQUESTION)

        def ntsdkill():
            ntsd1 = os.path.isfile(r"C:\Windows\System32\ntsd.exe")
            ntsd2 = os.path.isfile(r"C:\Windows\ntsd.exe")
            print(ntsd1)
            print(ntsd2)
            if ntsd1:
                pass
            if not ntsd1:
                if ntsd2:
                    pass
                else:
                    win32api.MessageBox(0, "你的电脑没有ntsd,请安装", "提示", win32con.MB_ICONQUESTION)
                    return 0
            getpid = getPidByName("studentmain.exe")
            if len(getpid) == 0:
                win32api.MessageBox(0, "未找到极域进程", "提示", win32con.MB_ICONQUESTION)
                return 0
            for x in range(len(getpid)):
                subprocess.run("ntsd -c q -p %s" % getpid[+1], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            win32api.MessageBox(0, "操作成功完成", "提示", win32con.MB_ICONQUESTION)

        def superpasswd():
            win32api.MessageBox(0, "万能密码:mythware_super_password", "提示", win32con.MB_ICONQUESTION)

        def gsjy():
            floder = filedialog.askdirectory(title="选择极域路径")
            if floder == "":
                win32api.MessageBox(0, "请选择极域路径!", "提示", win32con.MB_ICONWARNING)
                return 0
            try:
                os.remove(floder + "\\studentmain.exe")
                win32api.MessageBox(0, "操作成功完成", "提示", win32con.MB_ICONQUESTION)
            except:
                win32api.MessageBox(0, "操作成功完成", "提示", win32con.MB_ICONQUESTION)
                pass

        def sethc():
            win32api.MessageBox(0, "请先提权,否则无法运行", "提示", win32con.MB_ICONWARNING)
            if shell.IsUserAnAdmin():
                subprocess.run(r"del /f /s /q %windir%\System32\sethc.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                subprocess.run(r"rename %windir%\System32\cmd.exe sethc.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                win32api.MessageBox(0, "操作成功完成,按五次shift进入cmd", "提示", win32con.MB_ICONQUESTION)
            else:
                win32api.MessageBox(0, "请以管理员身份运行程序解锁!", "提示", win32con.MB_ICONWARNING)

        def exitkiller():
            sys.exit(0)

        self.startwin = startwin
        self.startwin.title('极域杀手')
        self.startwin.resizable(width=False, height=False)
        screenwidth = self.startwin.winfo_screenwidth()
        screenheight = self.startwin.winfo_screenheight()
        size = '%dx%d+%d+%d' % (358, 293, (screenwidth - 358) / 2, (screenheight - 293) / 2)
        self.startwin.geometry(size)

        filepath = resource_path(os.path.join("config","TopImage.png"))
        self.photo = tk.PhotoImage(file=filepath)
        self.photo1 = tk.Label(self.startwin, imag=self.photo, anchor=tk.CENTER)
        self.photo1.place(x=23, y=22, width=38, height=38)

        self.bq1bt = tk.StringVar()
        self.bq1bt.set('极域杀手——By O5-3议会成员')
        self.bq1 = tk.Label(self.startwin, textvariable=self.bq1bt, anchor=tk.W)
        self.bq1.place(x=72, y=28, width=190, height=23)
        self.bq1.config(font=("微软雅黑", 10, "bold"))

        self.bq2bt = tk.StringVar()
        self.bq2bt.set('基本功能')
        self.bq2 = tk.Label(self.startwin, textvariable=self.bq2bt, anchor=tk.W)
        self.bq2.place(x=15, y=87, width=55, height=21)
        self.bq2.config(font=("微软雅黑", 10, "bold"))

        self.bu1bt = tk.StringVar()
        self.bu1bt.set('尝试获取密码')
        self.bu1 = tk.Button(self.startwin, textvariable=self.bu1bt, command=getpass)
        self.bu1.place(x=12, y=119, width=82, height=33)

        self.bu2bt = tk.StringVar()
        self.bu2bt.set('taskkill终止极域')
        self.bu2 = tk.Button(self.startwin, textvariable=self.bu2bt, command=tkkill)
        self.bu2.place(x=116, y=120, width=90, height=33)

        self.bu3bt = tk.StringVar()
        self.bu3bt.set('ntsd终止极域')
        self.bu3 = tk.Button(self.startwin, textvariable=self.bu3bt, command=ntsdkill)
        self.bu3.place(x=227, y=120, width=82, height=33)

        self.bu4bt = tk.StringVar()
        self.bu4bt.set('尝试万能密码')
        self.bu4 = tk.Button(self.startwin, textvariable=self.bu4bt, command=superpasswd)
        self.bu4.place(x=12, y=161, width=82, height=33)

        self.bu5bt = tk.StringVar()
        self.bu5bt.set('破坏极域')
        self.bu5 = tk.Button(self.startwin, textvariable=self.bu5bt, command=gsjy)
        self.bu5.place(x=119, y=161, width=82, height=33)

        self.bu5btx = tk.StringVar()
        self.bu5btx.set('退出')
        self.bu5x = tk.Button(self.startwin, textvariable=self.bu5btx, command=exitkiller)
        self.bu5x.place(x=227, y=161, width=82, height=33)

        self.bq3bt = tk.StringVar()
        self.bq3bt.set('高级功能')
        self.bq3 = tk.Label(self.startwin, textvariable=self.bq3bt, anchor=tk.W)
        self.bq3.place(x=15, y=209, width=54, height=24)
        self.bq3.config(font=("微软雅黑", 10, "bold"))

        self.bq6bt = tk.StringVar()
        self.bq6bt.set('快捷打开cmd')
        self.bq6 = tk.Button(self.startwin, textvariable=self.bq6bt, command=sethc)
        self.bq6.place(x=12, y=251, width=82, height=33)


if __name__ == '__main__':
    root = tk.Tk()
    app = PyWinDesign(root)
    root.mainloop()
