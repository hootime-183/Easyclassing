import os
import re
import threading
import time


setting_text: str


def tasklist():
    os.popen("tasklist > tasks.txt")
    time.sleep(0.3)
    file_in = open("tasks.txt", "r")
    out = file_in.read()
    file_in.close()
    os.popen("del tasks.txt")
    return out


def first_check():
    global tk_name, settings_txt

    if not os.path.exists(f"D:/.ec"):
        os.mkdir("D:/.ec")
        file_in = open("D:/.ec/settings", "w+")
        file_in.write("style=tkinter.ttk\n")
        settings_txt = file_in.read()
        file_in.close()
    file_in = open("D:/.ec/settings", "r")
    settings_txt = file_in.read()
    file_in.close()
    print(re.findall("style=(.*?)\n", settings_txt), settings_txt)
    tk_name = re.findall("style=(.*?)\n", settings_txt)

    tasks = tasklist()
    if "Studentmain" in tasks:
        return "极域"
    elif "REDAgent" in tasks:
        if os.path.exists("C:/Program Files (x86)/3000soft/Red Spider"):
            finish = False
            cwd = os.getcwd()
            os.chdir("C:/Program Files (x86)/3000soft")

            def _kill(_name):
                while not finish:
                    killing(_name)

            thread = threading.Thread(target=_kill, args=("REDAgent.exe",))
            thread.daemon = True
            thread.start()
            print(os.path.exists("C:/Program Files (x86)/3000soft/Red Spider"))
            while os.path.exists("C:/Program Files (x86)/3000soft/Red Spider"):
                os.rename("Red Spider", "Red Spider EC")
                print(os.path.exists("C:/Program Files (x86)/3000soft/Red Spider"))
            finish = True
            os.chdir("C:/Program Files (x86)/3000soft/Red Spider EC")
            time.sleep(0.1)
            os.popen("REDAgent.exe")

            os.chdir(cwd)
        return "红蜘蛛"
    else:
        return "其它"


first_check()
file = open("D:/.ec/settings", "r")
settings_txt = file.read()
file.close()
print(re.findall("style=(.*?)\n", settings_txt), settings_txt)
tk_name = re.findall("style=(.*?)\n", settings_txt)


def get_tk(name):
    import tkinter
    import tkinter.ttk
    import sv_ttk

    if name == "tkinter.ttk":
        class ReturnTk:
            def __init__(self):
                self.Tk = tkinter.Tk
                self.Toplevel = tkinter.Toplevel
                self.StringVar = tkinter.StringVar
                self.ttk = tkinter.ttk
        return ReturnTk()
    elif name == "sv_ttk.light":
        class Tk(tkinter.Tk):
            def mainloop(self, **kwargs):
                sv_ttk.set_theme("light")
                tkinter.Tk.mainloop(self)

        class ReturnTk:
            def __init__(self):
                self.Tk = Tk
                self.Toplevel = tkinter.Toplevel
                self.StringVar = tkinter.StringVar
                self.ttk = tkinter.ttk
        return ReturnTk()
    elif name == "sv_ttk.dark":
        class Tk(tkinter.Tk):
            def mainloop(self, **kwargs):
                sv_ttk.set_theme("dark")
                tkinter.Tk.mainloop(self)

        class ReturnTk:
            def __init__(self):
                self.Tk = Tk
                self.Toplevel = tkinter.Toplevel
                self.StringVar = tkinter.StringVar
                self.ttk = tkinter.ttk
        return ReturnTk()


def jiyu_opening():
    def _open():
        cwd = os.getcwd()
        os.chdir("C:/Program Files (x86)/Mythware")
        for r, d, f in os.walk("./"):
            os.chdir(f"./{d[0]}")
        os.popen("StudentMain")
        os.chdir(cwd)

    thread = threading.Thread(target=_open)
    thread.daemon = True
    thread.start()


def red_agent_opening():
    def _open():
        cwd = os.getcwd()
        os.chdir("C:/Program Files (x86)/3000soft/Red Spider EC")
        os.popen("REDAgent")
        os.chdir(cwd)

    thread = threading.Thread(target=_open)
    thread.daemon = True
    thread.start()


def killing(name):
    os.popen(f"taskkill /t /f /im {name} 1>nul 2>nul")
    print("OK")


def killing_loop(name):
    def _kill(_name):
        while True:
            killing(_name)

    thread = threading.Thread(target=_kill, args=(name,))
    thread.daemon = True
    thread.start()


tkinter = get_tk(tk_name[0])
print(os.path.basename(__file__))


def restart_tk():
    global main
    if os.path.basename(__file__).split(".")[-1] == "py":
        print(f"python {os.path.basename(__file__)}")
        os.popen(f"python {os.path.basename(__file__)}")
    else:
        os.popen(os.path.basename(__file__))
    main.destroy()


class MainTk(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        first_check()
        self.title("Easyclassing")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="Easyclassing", font=("Calibri Light", 26))
        self.title_label.pack()
        self.maker_label = tkinter.ttk.Label(self, text="By Hootime183           ", font=("Calibri Light", 12))
        self.maker_label.pack(anchor="ne")
        self.control_button = tkinter.ttk.Button(self, text="课堂控制", command=self.open_control_page)
        self.control_button.pack()
        self.settings_button = tkinter.ttk.Button(self, text="设置", command=self.open_settings_page, width=10)
        self.settings_button.pack(side="bottom", anchor="e", padx=5, pady=5)

    @staticmethod
    def open_control_page():
        control = ControlTk()
        control.mainloop()

    @staticmethod
    def open_settings_page():
        settings = SettingsTk()
        settings.mainloop()


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
        self.values = ["极域", "惠普", "红蜘蛛", "其它"]
        self.title("Easyclassing-关闭控制")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="关闭控制", font=("微软雅黑 Light", 24))
        self.title_label.pack()
        self.maker_label = tkinter.ttk.Label(self, text="   ", font=("Calibri Light", 12))
        self.maker_label.pack(anchor="ne")
        self.combobox = tkinter.ttk.Combobox(self, state="readonly", values=self.values)
        self.combobox.pack()
        self.combobox.bind("<<ComboboxSelected>>", self.entry_setting)
        self.combobox.set(first_check())
        self.entry_frame = tkinter.ttk.Frame(self, width=150, height=30)
        self.entry_frame.pack()
        self.name_label = tkinter.ttk.Label(self.entry_frame, text="映像名：", font=("微软雅黑 Light", 12))
        self.name_label.pack(side="left")
        self.var = tkinter.StringVar()
        self.entry = tkinter.ttk.Entry(self.entry_frame, textvariable=self.var)
        self.entry.pack(side="left")
        self.button = tkinter.ttk.Button(self, text="关闭控制", command=self.go)
        self.button.pack()
        self.entry_setting(None)

    def entry_setting(self, event):
        if self.combobox.get() == "其它":
            self.entry["state"] = "normal"
            self.var.set("")
        else:
            self.entry["state"] = "normal"
            if self.combobox.get() == "极域":
                self.var.set("studentmain.exe")
            elif self.combobox.get() == "惠普":
                self.var.set("hpteach.exe")
            elif self.combobox.get() == "红蜘蛛":
                self.var.set("REDAgent.exe")
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
        self.open_jiyu_button = tkinter.ttk.Button(self, text="极域", command=self.go_jiyu)
        self.open_jiyu_button.pack()
        self.open_red_agent_button = tkinter.ttk.Button(self, text="红蜘蛛", command=self.go_red_agent)
        self.open_red_agent_button.pack()

    @staticmethod
    def go_jiyu():
        jiyu_opening()

    @staticmethod
    def go_red_agent():
        red_agent_opening()


class SettingsTk(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title("Easyclassing-设置")
        self.geometry("512x288")
        self.resizable(False, False)
        self.title_label = tkinter.ttk.Label(self, text="设置", font=("微软雅黑 Light", 24))
        self.title_label.pack()
        self.combobox = tkinter.ttk.Combobox(self, state="readonly", values=["tkinter.ttk", "sv_ttk.light", "sv_ttk.dark"])
        self.combobox.pack(pady=5)
        self.button = tkinter.ttk.Button(self, text="完成", command=self.complete)
        self.button.pack(pady=5)

    def complete(self):
        global tk_name, settings_txt
        print(re.sub(tk_name[0], self.combobox.get(), settings_txt))
        file_in = open("D:/.ec/settings", "w+")
        file_in.write(re.sub(tk_name[0], self.combobox.get(), settings_txt))
        file_in.close()
        restart_tk()


main = MainTk()


if __name__ == '__main__':
    print(tasklist())
    main.mainloop()
