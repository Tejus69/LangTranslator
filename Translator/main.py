from tkinter import *
import customtkinter
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





customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 

window = customtkinter.CTk()
# Logic Design
window.title("Language Translator")
window.geometry("500x700")


frame = customtkinter.CTkFrame(window).pack(side=BOTTOM)

mode = "dark"

def change_colors(choice):
	customtkinter.set_default_color_theme(choice)

def change():
	global mode
	if mode == "dark":
		customtkinter.set_appearance_mode("light")
		mode = "light"
	
	else:
		customtkinter.set_appearance_mode("dark")
		mode = "dark"



my_button = customtkinter.CTkButton(frame, text="Change Light/Dark", command=change)
my_button.pack(pady=20)
my_button.place(x=180,y=650)


Label1 = customtkinter.CTkLabel(master=window,text ="Translator"  ,font=("Segoe Print", 50, "bold"),height=60,width=320,text_color="DodgerBlue2")
Label1.pack(padx=100, pady=20)




sorce = customtkinter.CTkLabel(window,text="Source",font=("Time New Roman", 20,"bold"),height=30,width=100,text_color="magenta2")
sorce .pack(padx=30,pady=1)
sorce .place(x=20,y=100)

sorce_box = customtkinter.CTkTextbox(frame,border_width=2,fg_color="black",font=("Time New Roman", 20,"bold"),text_color="green1",height=150,width=480,wrap=WORD)
sorce_box.place(x=10,y=130)

lang_list = list(LANGUAGES.values())

combo_source = customtkinter.CTkComboBox(frame,values=lang_list)
combo_source.place(x=27,y=310)
combo_source.set("ENGLISH")

Translate_Button = customtkinter.CTkButton(frame,text= "Translate",hover_color="pink",font=("Time New Roman", 20, "bold"),height=40,width=150,command=data,border_width=3,border_color="green")
Translate_Button.place(x=185,y=310)

combo_Desti = customtkinter.CTkComboBox(frame,values=lang_list)
combo_Desti .place(x=350,y=310)
combo_Desti .set("HINDI")

Desti_box =  customtkinter.CTkTextbox(frame,fg_color="black",text_color="green1",font=("Time New Roman", 20,"bold"),border_width=2,height=150,width=480,wrap=WORD)
Desti_box.place(x=10,y=420)


destination = customtkinter.CTkLabel(window,text="Destination",font=("Time New Roman", 20,"bold"),height=20,width=30,text_color="magenta2")

destination.place(x=25,y=380)




window.mainloop()
