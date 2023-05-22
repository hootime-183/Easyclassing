import tkinter
import tkinter.ttk
import os
import threading


def jiyu_opening():
    def _open():
        cwd = os.getcwd()
        os.chdir("C:/Program Files (x86)/Mythware")
        for r, d, f in os.walk("./"):
            os.chdir(f"./{d[0]}")
        os.system("StudentMain")
        os.chdir(cwd)

    thread = threading.Thread(target=_open)
    thread.daemon = True
    thread.start()


def killing(name):
    os.system(f"taskkill /t /f /im {name} 1>nul 2>nul")
    print("OK")


class MainTk(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Easyclassing")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="Easyclassing", font=("Calibri Light", 26))
        self.title_label.pack()
        self.maker_label = tkinter.ttk.Label(self, text="By Hootime183           ", font=("Calibri Light", 12))
        self.maker_label.pack(anchor="ne")
        self.control_button = tkinter.ttk.Button(self, text="课堂控制", command=self.open_control_page)

        self.control_button.pack()

    @staticmethod
    def open_control_page():
        control = ControlTk()
        control.mainloop()


class ControlTk(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title("Easyclassing-课堂控制")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="课堂控制", font=("微软雅黑 Light", 24))
        self.title_label.pack()
        self.maker_label = tkinter.ttk.Label(self, text="   ", font=("Calibri Light", 12))
        self.maker_label.pack(anchor="ne")
        self.open_button = tkinter.ttk.Button(self, text="打开控制", command=self.open_opening_page)

        self.open_button.pack()
        self.maker_label2 = tkinter.ttk.Label(self, text="   ", font=("Calibri Light", 6))
        self.maker_label2.pack(anchor="ne")
        self.close_button = tkinter.ttk.Button(self, text="关闭控制", command=self.open_closing_page)
        self.close_button.pack()

    @staticmethod
    def open_opening_page():
        open_tk = ControlOpenTk()
        open_tk.mainloop()

    @staticmethod
    def open_closing_page():
        close_tk = ControlCloseTk()
        close_tk.mainloop()


class ControlCloseTk(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title("Easyclassing-关闭控制")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="关闭控制", font=("微软雅黑 Light", 24))
        self.title_label.pack()
        self.maker_label = tkinter.ttk.Label(self, text="   ", font=("Calibri Light", 12))
        self.maker_label.pack(anchor="ne")
        self.combobox = tkinter.ttk.Combobox(self, state="readonly", values=["极域", "惠普", "其它"])
        self.combobox.pack()
        self.combobox.bind("<<ComboboxSelected>>", self.entry_setting)
        self.maker_label2 = tkinter.ttk.Label(self, text="   ", font=("Calibri Light", 30))
        self.maker_label2.pack(anchor="ne")
        self.name_label = tkinter.ttk.Label(self, text="映像名：", font=("微软雅黑 Light", 12))
        self.name_label.place(x=150, y=105)
        self.var = tkinter.StringVar()
        self.entry = tkinter.ttk.Entry(self, textvariable=self.var)
        self.entry.place(x=225, y=105)
        self.button = tkinter.ttk.Button(self, text="关闭控制", command=self.go)
        self.button.pack()

    def entry_setting(self, _any):
        if self.combobox.get() == "其它":
            self.entry["state"] = "normal"
            self.var.set("")
        else:
            self.entry["state"] = "normal"
            if self.combobox.get() == "极域":
                self.var.set("studentmain.exe")
            elif self.combobox.get() == "惠普":
                self.var.set("hpteach.exe")
            self.entry["state"] = "readonly"

    def go(self):
        killing(self.entry.get())


class ControlOpenTk(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title("Easyclassing-打开控制")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="打开控制", font=("微软雅黑 Light", 24))
        self.title_label.pack()
        self.maker_label = tkinter.ttk.Label(self, text="   ", font=("Calibri Light", 12))
        self.maker_label.pack(anchor="ne")
        self.open_button = tkinter.ttk.Button(self, text="极域", command=self.go_jiyu)
        self.open_button.pack()

    @staticmethod
    def go_jiyu():
        jiyu_opening()


if __name__ == '__main__':
    MainTk().mainloop()
