import random
import tkinter
import tkinter.messagebox

#HANSHU
def b_clicked():
    if name_Entry.get() == '':
        tkinter.messagebox.showerror(title='Error', message='请输入用户名字')
    else:
        cin_name = name_Entry.get()
        try:
            text_check = ''.join(j for j in age_Entry.get() if j in '0123456789')
            cin_age = int(text_check)
            text_check = ''.join(j for j in weight_Entry.get() if j in '0123456789.')
            cin_weight = float(text_check)
            text_check = ''.join(j for j in high_Entry.get() if j in '0123456789.')
            cin_high = float(text_check)
        except ValueError:
            tkinter.messagebox.showerror(title='Error', message='请输入数字')
        pi = BMI(cin_name, cin_age, cin_weight, cin_high)
        pi.search_get()


class BMI:
    def __init__(self, name, age, weight, high):
        self.name = name
        self.age = age
        self.weight = weight
        self.high = high
        self.bmi = self.weight / self.high / self.high
        if self.bmi < 18.5:
            self.status = "健康状况:偏瘦。"
        elif 18.5 <= self.bmi < 24:
            self.status = "健康状况:正常。"
        elif 24 <= self.bmi < 30:
            self.status = "健康状况:偏胖。"
        elif self.bmi > 30:
            self.status = "健康状况:肥胖。"

    def search_get(self):
        Label2['text'] = "当前用户为{}，年龄为{}，体重为{}，身高为{}，\nBMI值为{:.2f}，{}".format(self.name, self.age,
                                                                             self.weight, self.high, self.bmi,
                                                                             self.status)


if __name__ == "__main__":
    n = int(random.random() * 50 + 1)
    i = 0
    window = tkinter.Tk()
    window.title('BMI计算器')
    window.geometry('500x300')
    Label1 = tkinter.Label(window, text='BMI计算器', font=('Arial', 12), width=30, height=2)
    Label1.place(x=110, y=0, anchor='nw')
    Button1 = tkinter.Button(window, text='开始计算', font=('Arial', 12), width=20, height=1, command=b_clicked)
    Button1.place(x=150, y=50, anchor='nw')
    Label2 = tkinter.Label(window, text='请输入相关信息', bg='green', font=('Arial', 12), width=50, height=3)
    Label2.pack(side='bottom')
    name_Entry = tkinter.Entry(window, width=7, show=None)
    name_Entry.place(x=220, y=90, anchor='nw')
    age_Entry = tkinter.Entry(window, width=7, show=None)
    age_Entry.place(x=220, y=120, anchor='nw')
    weight_Entry = tkinter.Entry(window, width=7, show=None)
    weight_Entry.place(x=220, y=150, anchor='nw')
    high_Entry = tkinter.Entry(window, width=7, show=None)
    high_Entry.place(x=220, y=180, anchor='nw')
    Label3 = tkinter.Label(window, text='姓名:', font=('Arial', 10), width=4, height=1)
    Label3.place(x=180, y=90, anchor='nw')
    Label4 = tkinter.Label(window, text='年龄:', font=('Arial', 10), width=4, height=1)
    Label4.place(x=180, y=120, anchor='nw')
    Label4 = tkinter.Label(window, text='体重:', font=('Arial', 10), width=4, height=1)
    Label4.place(x=180, y=150, anchor='nw')
    Label4 = tkinter.Label(window, text='身高:', font=('Arial', 10), width=4, height=1)
    Label4.place(x=180, y=180, anchor='nw')
    window.mainloop()
