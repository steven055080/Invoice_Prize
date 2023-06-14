import tkinter as tk
from tkinter import ttk
import datasource
from datasource import changeMonth

last_number = changeMonth('lastNumber')
new_number = changeMonth()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.drawMidinner()

    def drawMidinner(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill = "both", expand = True,padx=10,pady=10)

        ttk.Label(self.main_frame,text=datasource.z1,font='Arial 40').pack(padx='20',pady='20')

        self.top_wrapperFrame = ttk.LabelFrame(self.main_frame,text='對獎號碼')
        self.top_wrapperFrame.pack(fill=tk.X,side='left',padx=10)
        label1 = ttk.Label(self.top_wrapperFrame,text=f'特別獎號碼: {datasource.ns}',font='50')
        label1.pack(anchor='w')
        label2 = ttk.Label(self.top_wrapperFrame,text=f'特獎號碼: {datasource.n1}',font='50')
        label2.pack(anchor='w',pady=5)
        label3 = ttk.Label(self.top_wrapperFrame,text=f'頭獎號碼: {datasource.n2[0]}\n{datasource.n2[1]}\n{datasource.n2[2]}',font='50',justify='right')
        label3.pack(anchor='w')

        top_wrapperFrame1 = ttk.LabelFrame(self.main_frame,text='對獎方式')
        top_wrapperFrame1.pack(fill=tk.X,side='left')
        label4 = ttk.Label(top_wrapperFrame1,text=f'{datasource.t1[9:]}\n\n{datasource.t2[9:]}\n\n{datasource.t3[9:]}\n\n{datasource.t4[9:]}\n\n{datasource.t5[9:]}\n\n{datasource.t6[9:]}\n\n{datasource.t7[9:]}\n\n{datasource.t8[9:]}',font='50')
        label4.pack()

        self.monthFrame = ttk.Frame(self)
        self.monthFrame.pack(pady=10)

        btn1 = tk.Button(self.monthFrame,text=new_number[:10],width=12,height=1,font=("微軟正黑體",15),borderwidth=3,command=self.on_btn1_click)
        btn1.pack(side='left',padx=10)

        btn2 = tk.Button(self.monthFrame,text=last_number[:10],width=12,height=1,font=("微軟正黑體",15),borderwidth=3,command=self.on_btn2_click)
        btn2.pack(side='left',padx=5)

        self.buttomFrame = ttk.Frame(self)
        self.buttomFrame.pack()

        label5 = ttk.Label(self.buttomFrame, text="%13s"%"對獎專區" "%s"%"\n輸入發票號碼(8碼)",font=50)
        label5.pack()
        self.numberKeyin = tk.StringVar()
        keyinNumber = tk.Entry(self.buttomFrame, textvariable=self.numberKeyin, font=20)
        keyinNumber.pack()
        matchNumber = tk.Button(self.buttomFrame, text = "對獎",font=40,command = self.on_click)
        matchNumber.pack(pady=10)
        self.label6 = tk.Label(self.buttomFrame,font=('',18))
        self.label6.pack(pady=(0,10))

        label7 = tk.Label(self.buttomFrame, text=datasource.x1,font=('',15))
        label7.pack()

    def on_btn1_click(self):
        changeMonth()
        self.main_frame.destroy()
        self.monthFrame.destroy()
        self.buttomFrame.destroy()
        self.drawMidinner()

    def on_btn2_click(self):
        changeMonth('lastNumber')
        self.main_frame.destroy()
        self.monthFrame.destroy()
        self.buttomFrame.destroy()
        self.drawMidinner()

    def on_click(self):
            entryNumber = self.numberKeyin.get()
            if len(entryNumber) != 8:
                words = "輸入字數不符，請重新輸入!!"
                self.label6.configure(text=words, fg = "red")
            elif entryNumber.isdigit() is not True:
                words = "含有數字以外的字元，請重新輸入!!"
                self.label6.configure(text=words, fg = "red")
            elif entryNumber == datasource.ns:
                words = "恭喜中1000萬!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber == datasource.n1:
                words = "恭喜中200萬!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber == datasource.n2[0] or entryNumber == datasource.n2[1] or entryNumber == datasource.n2[2]:
                words = "恭喜中20萬!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber[-7:] in [datasource.n2[0][-7:], datasource.n2[1][-7:], datasource.n2[2][-7:]]:
                words = "恭喜中4萬!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber[-6:] in [datasource.n2[0][-6:], datasource.n2[1][-6:], datasource.n2[2][-6:]]:
                words = "恭喜中1萬!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber[-5:] in [datasource.n2[0][-5:], datasource.n2[1][-5:], datasource.n2[2][-5:]]:
                words = "恭喜中4千!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber[-4:] in [datasource.n2[0][-4:], datasource.n2[1][-4:], datasource.n2[2][-4:]]:
                words = "恭喜中1千!!"
                self.label6.configure(text=words, fg = "green")
            elif entryNumber[-3:] in [datasource.n2[0][-3:], datasource.n2[1][-3:], datasource.n2[2][-3:]]:
                words = "恭喜中2百!!"
                self.label6.configure(text=words, fg = "green")
            else:
                words = "未中獎，再接再厲!!"
                self.label6.configure(text=words, fg = "brown")

def main():
    window = Window()
    window.title("發票對獎")
    window.resizable(False, False)
    window.mainloop()

if  __name__ == "__main__":
    main()