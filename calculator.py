import tkinter as tk

window=tk.Tk()

window.title('Calculator')

window.geometry('500x600')

label=tk.Label(window, text='hello Tkinter').pack()

e=tk.Entry(window)
e.delete(0,'end')
e.place(x=10,y=20,width=300,height=40)

def set_entry_button(num):
    def button_selector():
        e.insert('end',num)
    return button_selector


def result():
    res=e.get()
    trans=eval(res)
    e.delete(0,'end')
    e.insert(0,trans)

def delete():
    e.delete(0,'end')


button1=tk.Button(window, text='Numero 1', command=set_entry_button('1'))
button1.place(x=10,y=70,width=110,height=60)

button2=tk.Button(window, text='Numero 2', command=set_entry_button('2'))
button2.place(x=140,y=70,width=110,height=60)

button3=tk.Button(window, text='Numero 3', command=set_entry_button('3'))
button3.place(x=260,y=70,width=110,height=60)

plus=tk.Button(window,text='+',command=set_entry_button('+'))
plus.place(x=380,y=70,width=110,height=60)

button4=tk.Button(window, text='Numero 4', command=set_entry_button('4'))
button4.place(x=10,y=140,width=110,height=60)

button5=tk.Button(window, text='Numero 5', command=set_entry_button('5'))
button5.place(x=140,y=140,width=110,height=60)

button6=tk.Button(window, text='Numero 6', command=set_entry_button('6'))
button6.place(x=260,y=140,width=110,height=60)

minus=tk.Button(window,text='-',command=set_entry_button('-'))
minus.place(x=380,y=140,width=110,height=60)

button7=tk.Button(window, text='Numero 7', command=set_entry_button('7'))
button7.place(x=10,y=210,width=110,height=60)

button8=tk.Button(window, text='Numero 8', command=set_entry_button('8'))
button8.place(x=140,y=210,width=110,height=60)

button9=tk.Button(window, text='Numero 9', command=set_entry_button('9'))
button9.place(x=260,y=210,width=110,height=60)

times=tk.Button(window,text='x',command=set_entry_button('*'))
times.place(x=380,y=210,width=110,height=60)

paren=tk.Button(window, text='(', command=set_entry_button('('))
paren.place(x=10,y=280,width=110,height=60)

zero=tk.Button(window, text='Numero 0', command=set_entry_button('0'))
zero.place(x=140,y=280,width=110,height=60)

paren2=tk.Button(window, text=')', command=set_entry_button(')'))
paren2.place(x=260,y=280,width=110,height=60)

div=tk.Button(window,text='/',command=set_entry_button('/'))
div.place(x=380,y=280,width=110,height=60)

point=tk.Button(window, text='.', command=set_entry_button('.'))
point.place(x=10,y=350,width=110,height=60)

clear=tk.Button(window, text='C', command=delete)
clear.place(x=140,y=350,width=110,height=60)

result=tk.Button(window,text='=',command=result)
result.place(x=260,y=350,width=220,height=60)

window.mainloop()