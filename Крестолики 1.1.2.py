from tkinter import *
from tkinter import ttk
from tkinter.ttk import Button
from PIL import ImageTk, Image
from tkinter import messagebox
labelsnol=[]
labelskres=[]
list_krestic = []
list_nolic = []
all_list=[]
a,b=int(200),int(200)
nolkres=True
def on_closing():
    if messagebox.askokcancel('Выход из приложения','Хотите выйти из приложения?\nТочно?\nТочно точно?'):
        window.destroy()

window=Tk()
window.protocol('WM_DELETE_WINDOW',on_closing)
window.title('Крестолики')
window.state('zoomed')
window.resizable(width=False,height=False)
window.image=PhotoImage(file='фон.png')
bg_phon=Label(window,image=window.image)

image1=Image.open('крестик.png')
image1=image1.resize((a,b))
krestic=ImageTk.PhotoImage(image1)
image2=Image.open('frame2.png')
image2=image2.resize((a,b))
nolic=ImageTk.PhotoImage(image2)

for i in range(30):
    window.rowconfigure(i,weight=True)
    window.columnconfigure(i,weight=True)

bg_phon.grid(row=0,column=0,columnspan=30,rowspan=30,sticky='nesw')
buttons=[]
coordinate=[[5,8],[5,13],[5,18],[12,8],[12,13],[12,18],[19,8],[19,13],[19,18]]
all = int(0)
def spawn_button(num):
    global button_back
    button_play.destroy()
    list_krestic = [[] * num for i in range(num)]
    list_nolic = [[] * num for i in range(num)]
    button_back=Button(text='←',command=dalee)
    button_back.grid(row=0,column=0,rowspan=5,columnspan=5,sticky='nesw')
    for i in range(num):
        button=ttk.Button()
        button.grid(row=coordinate[i][0],column=coordinate[i][1],rowspan=7,columnspan=5,sticky='nesw')
        button.bind('<Button-1>', lambda event,number = i: button_press(number,list_krestic,list_nolic,num))
        buttons.append(button)

def button_press(index,list_krestic,list_nolic,num):
    global all
    global nolkres
    buttons[index].destroy()
    all+=1
    if nolkres:
        label=Label(image=krestic)
        label.grid(row=coordinate[index][0],column=coordinate[index][1],rowspan=7,columnspan=5)
        labelskres.append(label)
        nolkres=False
        list_krestic[index]=1
        all_list.append(label)
    else:
        label = Label(image=nolic)
        label.grid(row=coordinate[index][0], column=coordinate[index][1], rowspan=7, columnspan=5)
        labelsnol.append(label)
        nolkres = True
        list_nolic[index]=1
        all_list.append(label)
    wins(list_krestic,list_nolic,num,all)

def game():
    global button_play
    button_play.destroy()
    spawn_button(num=9)

def wins(list_krestic,list_nolic,num,all):
    global winkrestic, winnolic
    winkrestic=False
    winnolic=False
    if (list_krestic[0]==1 and list_krestic[1]==1 and list_krestic[2]==1) or (list_krestic[0]==1 and list_krestic[3]==1 and list_krestic[6]==1):
            winkrestic = True
    elif (list_krestic[3] == 1 and list_krestic[4] == 1 and list_krestic[5] == 1) or (list_krestic[1] == 1 and list_krestic[4] == 1 and list_krestic[7] == 1):
        winkrestic = True
    elif (list_krestic[6]==1 and list_krestic[7]==1 and list_krestic[8]==1) or (list_krestic[2]==1 and list_krestic[5]==1 and list_krestic[8]==1):
            winkrestic = True
    elif (list_nolic[0]==1 and list_nolic[1]==1 and list_nolic[2]==1) or (list_nolic[0]==1 and list_nolic[3]==1 and list_nolic[6]==1):
            winnolic = True
    elif (list_nolic[3]==1 and list_nolic[4]==1 and list_nolic[5]==1) or (list_nolic[1]==1 and list_nolic[4]==1 and list_nolic[7]==1):
            winnolic = True
    elif (list_nolic[6]==1 and list_nolic[7]==1 and list_nolic[8]==1) or (list_nolic[2]==1 and list_nolic[5]==1 and list_nolic[8]==1):
            winnolic = True
    elif (list_krestic[0]==1 and list_krestic[4]==1 and list_krestic[8]==1) or (list_krestic[2]==1 and list_krestic[4]==1 and list_krestic[6]==1):
            winkrestic=True
    elif (list_nolic[0]==1 and list_nolic[4]==1 and list_nolic[8]==1) or (list_nolic[2]==1 and list_nolic[4]==1 and list_nolic[6]==1):
            winnolic=True
    if winkrestic:
        for i in buttons:
            i.destroy()
        label=Label(text='Игрок, играющий за крестики победил!')
        label.grid(row=0,column=10,rowspan=2,columnspan=10,sticky='nesw')
        button = Button(text='Далее',command=dalee)
        button.grid(row=2, column=10, rowspan=2, columnspan=10, sticky='nesw')
        all_list.append(label)
        all_list.append(button)
    if winnolic:
        for i in buttons:
            i.destroy()
        label = Label(text='Игрок, играющий за нолики победил!')
        label.grid(row=0, column=10, rowspan=2, columnspan=10, sticky='nesw')
        button = Button(text='Далее',command=dalee)
        button.grid(row=2, column=10, rowspan=2, columnspan=10, sticky='nesw')
        all_list.append(label)
        all_list.append(button)
    if all==(num) and not winkrestic and not winnolic:
        label = Label(text='Ничья!')
        label.grid(row=0, column=10, rowspan=2, columnspan=10, sticky='nesw')
        button=Button(text='Далее',command=dalee)
        button.grid(row=2, column=10, rowspan=2, columnspan=10, sticky='nesw')
        all_list.append(label)
        all_list.append(button)

def dalee():
    global all, winkrestic, winnolic, button_back
    winkrestic = False
    winnolic = False
    all=int(0)
    for i in all_list:
        i.destroy()
    for i in labelskres:
        i.destroy()
    for i in labelsnol:
        i.destroy()
    for i in buttons:
        i.destroy()
    button_back.destroy()
    all_list.clear()
    labelskres.clear()
    labelsnol.clear()
    list_krestic.clear()
    list_nolic.clear()
    buttons.clear()
    button_play_def()

def minus():
    global image1,a,b,krestic, nolic,image2
    if a>20 and b>20:
        a-=10
        b-=10
    image1=image1.resize((a,b))
    krestic = ImageTk.PhotoImage(image1)
    image2 = image2.resize((a, b))
    nolic = ImageTk.PhotoImage(image2)
    for label in labelskres:
        label.config(image=krestic)
        label.image=krestic
    for label in labelsnol:
        label.config(image=nolic)
        label.image = nolic

def plus():
    global image1,a,b,krestic, nolic,image2
    if a<500 and b <500:
        a+=10
        b+=10
    image1=image1.resize((a,b))
    krestic = ImageTk.PhotoImage(image1)
    image2 = image2.resize((a, b))
    nolic = ImageTk.PhotoImage(image2)
    for label in labelskres:
        label.config(image=krestic)
        label.image=krestic
    for label in labelsnol:
        label.config(image=nolic)
        label.image = nolic

def button_play_def():
    global button_play
    button_play = ttk.Button(text='Играть',command=game)
    button_play.grid(row=15,column=10,columnspan=9,rowspan=6,sticky='nesw')
    button_plus = Button(text='+', command=plus)
    button_plus.grid(row=0, column=24, rowspan=3, columnspan=3, sticky='nesw')
    button_minus = Button(text='-', command=minus)
    button_minus.grid(row=0, column=27, rowspan=3, columnspan=3,sticky='nesw')
    all_list.append(button_play)

button_play_def()

window.mainloop()