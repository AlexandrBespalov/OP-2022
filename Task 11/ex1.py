import json
import requests

from tkinter import *
from tkinter import messagebox

def getData():
    otv = Input.get()
    url = f"https://api.github.com/users/{otv}"
    data = requests.get(url).json()

    with open("getJSON.json", "w") as file:
        json.dump(data, file, indent = 3)

#В задании не указано, что нужно получить ТОЛЬКО заданные данные, поэтому я спарсил все, в том числе и необходимые.
#Если нужно было спарсить ТОЛЬКО заданные, то вот кусок кода, вместо того, который в функции getData:

    #with open("getJSON.json", "a") as file:
        #print('Company:', data['company'],file=f)
        #print('created_at:', data['created_at'],file=f)
        #print('email:', data['email'], file=f)
        #print('id:', data['id'],file=f)
        #print('name:', data['name'],file=f)
        #print('url:', data['url'],file=f)

#GUI
window = Tk()

def btn_click():
    InputWindow = Input.get()

    info_str = f'Запрос на получение данных пользователя: {str(InputWindow)}'
    messagebox.showinfo(title='Получение JSON', message=info_str)

    #messagebox.showerrоr(title='Error!', Message='Ошибка')

#window['bg'] = '#8cc2ff'
window.title('Get JSON')
window.geometry('300x250')

window.resizable(width=False, height=False)

Canvas = Canvas(window, height=300, width=250)
Canvas.pack()

frame = Frame(window)
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.7)

title = Label(frame, text='Ввод имени', font='18')
title.pack(anchor=N)

Input = Entry(frame, bg='white')
Input.pack(anchor=CENTER)

btn = Button(frame, text = 'Получить', bg='#5991ff', command=lambda:[getData(), btn_click()])
btn.pack(anchor=S)

window.mainloop()