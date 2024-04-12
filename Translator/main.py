from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES 


def translate(text="type",src= "English",dest= "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1 ,dest=dest1)
    return trans1.text


def data():
    s = combo_source.get()
    d = combo_Desti.get()
    message = sorce_box.get(1.0,END)
    textget = translate(text= message,src=s,dest=d)
    Desti_box.delete(1.0,END)
    Desti_box.insert(END,textget)






window = Tk()
# Logic Design
window.title("Translator")
window.geometry("500x700")
window.config(bg="red")

Label1 = Label(window,text="Translator",font=("Time New Roman", 40,"bold"))
Label1.place(x=100,y=40,height=50,width=300)

frame = Frame(window,bg="green").pack(side=BOTTOM)

sorce = Label(window,text="Source",font=("Time New Roman", 20,"bold"),bg="red")
sorce .place(x=0,y=100,height=30,width=300)

sorce_box = Text(frame,font=("Time New Roman", 20,"bold"),wrap=WORD,bg="black",fg="#00ff00",insertbackground="white")
sorce_box.place(x=10,y=130,height=150,width=480)

lang_list = list(LANGUAGES.values())

combo_source = ttk.Combobox(frame,value=lang_list)
combo_source.place(x=10,y=300,height=40,width=150)
combo_source.set("ENGLISH")

Translate_Button = Button(frame,text= "Translate",relief=RAISED,command=data)
Translate_Button.place(x=170,y=300,height=40,width=150)

combo_Desti = ttk.Combobox(frame,value=lang_list)
combo_Desti .place(x=330,y=300,height=40,width=150)
combo_Desti .set("HINDI")

Desti_box = Text(frame,font=("Time New Roman", 20,"bold"),wrap=WORD,bg="black",fg="#00ff00",insertbackground="white")
Desti_box.place(x=10,y=400,height=150,width=480)

destination = Label(window,text="Destination",font=("Time New Roman", 20,"bold"),bg="red")
destination.place(x=60,y=360,height=30,width=300)


window.mainloop()