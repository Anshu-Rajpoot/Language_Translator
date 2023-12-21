from tkinter import *
from googletrans import Translator
from gtts import gTTS

def a():
    n1=entrywindow.get()
    n2=Translator()
    n3=dropdown.get()

    if n3=="Hindi":
        cnvrt="hi"
    elif n3=="English":
        cnvrt="en"
    elif n3=="Spanish":
        cnvrt="es"
    elif n3=="German":
        cnvrt="de"
    elif n3=="French":  
        cnvrt="fr"

    txt=n2.translate(n1,dest=cnvrt)
    txt=txt.text
    n4=gTTS(text=txt,slow=False,lang=cnvrt)
    label.config(text=txt)
    
opt=["Hindi","English","Spanish","German","French"]

#for window
window=Tk()
window.geometry("600x300")#it's "x" not multiplication sign
window.config(bg="light gray")

#gui for input of first entry window
entrywindow=Entry(window, bg="white", fg="dark gray",
                  font=("arial",20,"bold"))#write text to convert
entrywindow.place(x=20,y=60)

dropdown=StringVar()#datatype for input of drop down window
dropdown.set("Select Language")

dropcontent=OptionMenu(window,dropdown,*opt)#list of language using this function
dropcontent.configure(bg="light blue", fg="black", font=("arial",12,"bold"))
dropcontent.place(x=350,y=60)#helps in giving dimensions using coordinates

label=Label(window,text="\t\t\t\t\t\t",bg="light blue",fg="white",font=("arial",16,"bold"))#to write anything
label.place(x=20,y=120)
label=Label(window,text="Translated Language",bg="light blue",fg="black",font=("arial",16,"bold"))
label.place(x=180,y=120)

translateb=Button(window,text="Translate !!", bg="deep sky blue",fg="white",font=("arial",16,"bold"),command=a)
translateb.place(x=220,y=220)
window.mainloop()#indicates the program completion and if it is not used then o/p will not be shown whether it has error or not
