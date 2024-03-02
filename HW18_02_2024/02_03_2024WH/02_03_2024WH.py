from tkinter import *

root = Tk()
root.title("Калькулятор")
root['bg'] = 'magenta2'
w1 = root.winfo_screenwidth()
h1 = root.winfo_screenheight()
root.geometry(f"500x300+{int(w1/2-250)}+{int(h1/2-250)}")

chislo = ''
chisla_mass = []
dii_mass = []


def kalk(kh):
    global chislo
    chislo += kh
    visualisation(chislo)


def dia(dia):
    global chislo
    if chislo != '':
        chisla_mass.append(int(chislo))
        chislo = ''
        dii_mass.append(dia)
        visualisation(dia)
    else:
        dii_mass.pop()
        dii_mass.append(dia)
        visualisation(dia)


def dorivnue():
    global chislo
    if chislo == '':
        dii_mass.pop()
    else:
        chisla_mass.append(int(chislo))
    res = chisla_mass[0]
    i = 0
    while i < len(dii_mass):
        if dii_mass[i] == '+':
            res += chisla_mass[i+1]
        elif dii_mass[i] == '*':
            res *= chisla_mass[i+1]
        elif dii_mass[i] == '-':
            res -= chisla_mass[i+1]
        elif dii_mass[i] == '/':
            res %= chisla_mass[i+1]
        i += 1
    remov()
    visualisation(res)
    chislo = str(res)


def remov():
    chisla_mass.clear()
    dii_mass.clear()
    global chislo
    chislo = ''
    visualisation('Тутоньки чисто')


def visualisation(text):
    pole.delete(0, END)
    pole.insert(0, str(text))


pole = Entry(root, font=(None, 35), fg='magenta2', bg='purple')
pole.grid(row=0, column=0, columnspan=8)
but_ch1 = Button(root, text='~1~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda:kalk("1"))
but_ch1.grid(row=1, column=0)
but_ch2 = Button(root, text='~2~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda:kalk("2"))
but_ch2.grid(row=1, column=1)
but_ch3 = Button(root, text='~3~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda:kalk('3'))
but_ch3.grid(row=1, column=2)
but_ch4 = Button(root, text='~4~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda:kalk('4'))
but_ch4.grid(row=2, column=0)
but_ch5 = Button(root, text='~5~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda:kalk('5'))
but_ch5.grid(row=2, column=1)
but_ch6 = Button(root, text='~6~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda:kalk('6'))
but_ch6.grid(row=2, column=2)
but_ch7 = Button(root, text='~7~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda:kalk('7'))
but_ch7.grid(row=3, column=0)
but_ch8 = Button(root, text='~8~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda:kalk('8'))
but_ch8.grid(row=3, column=1)
but_ch9 = Button(root, text='~9~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda:kalk('9'))
but_ch9.grid(row=3, column=2)
but_ch0 = Button(root, text='~0~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda:kalk('0'))
but_ch0.grid(row=4, column=0)
but_ch_point = Button(root, text='~/~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda: dia('/'))
but_ch_point.grid(row=4, column=1)
# but_ch_с = Button(root, text='~С~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda:kalk)
# but_ch_с.grid(row=2, column=4)
but_ch_plus = Button(root, text='~+~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda: dia('+'))
but_ch_plus.grid(row=1, column=3)
but_ch_minus = Button(root, text='~-~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda:dia('-'))
but_ch_minus.grid(row=2, column=3)
but_ch_result = Button(root, text='~=~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda: dorivnue())
but_ch_result.grid(row=3, column=3)
but_ch_mul = Button(root, text='~C~', font=("Verdana", 20), bg='violetred4', fg='pink4', activebackground='plum', width=4, height=1, command=lambda: remov())
but_ch_mul.grid(row=4, column=3)
but_ch_division = Button(root, text='~*~', font=("Verdana", 20), bg='violet', fg='purple', activebackground='plum', width=4, height=1, command=lambda: dia('*'))
but_ch_division.grid(row=4, column=2)
but_ch_end = Button(root, text='~Вихід~', font=("Verdana", 20), bg='purple', fg='magenta2', activebackground='plum', width=8, height=1, command=lambda: root.quit())
but_ch_end.grid(row=4, column=4)


root.mainloop()