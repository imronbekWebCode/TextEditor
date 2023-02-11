from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkinter import dialog
from tkinter import simpledialog
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from tkinter import filedialog as fd 

root = Tk()
root.title("TextEditor")
root.resizable(0,0)
root.iconbitmap("D:/Mixhost/navruz/new.png")
canvas = Canvas(root, width=700, height=500, bg="white")
canvas.pack()
#******************************
 
mainmenu = Menu(root) 
root.config(menu=mainmenu) 

  
filemenu = Menu(mainmenu, tearoff=0)
def create_text():
   new_root = Tk()
   new_root.title("TextEditor")
   new_root.resizable(0,0)
   new_root.geometry("700x500")
   nb = ttk.Notebook(new_root)
   nb.pack(fill='both', expand='yes')
   f1 = ttk.Frame(nb)
   nb.pack(fill='both', expand='yes')
   f1 = ttk.Frame(nb)
   nb.add(f1, text='Doc1')
   # combobox = ttk.Combobox(new_root2, values=languages)
   #combobox.pack(anchor=NW, padx=7, pady=8)      
   #Name = ttk.Entry(new_root2, width=20).pack(anchor=NW, padx=7, pady=8)
   def save():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = f1.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
   Button(new_root, width=20, height=2,text="Save the Document", command=save).place(x=550, y=460)
   # combobox = ttk.Combobox(new_root2, values=languages)
   #combobox.pack(anchor=NW, padx=7, pady=8)      
   #Name = ttk.Entry(new_root2, width=20).pack(anchor=NW, padx=7, pady=8)
   def save():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = f1.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
   Button(new_root, width=20, height=2,text="Save the Document", command=save).place(x=550, y=460)

def close():
      root.quit()
def callback():
      filepath = filedialog.askopenfilename()
      fh = open(filepath, 'r')
      read = fh.read()
      open_text = Text(f1)
      open_text.pack(padx=6, pady=6)
      open_text.insert(END, read)
      def close_2():
            f1.quit()
      def save():
            filepath = filedialog.asksaveasfilename()
            if filepath != "":
                  text = f1.get("1.0", END)
                  with open(filepath, "w") as file:
                        file.write(text)
      Button(f1, width=20, height=2,text="Save the Document", command=save).pack()
      Button(f1, text="Close", state="active", command=close_2).pack()
filemenu.add_command(label="Открыть...", command=callback)
filemenu.add_command(label="Новый", command=create_text)
filemenu.add_command(label="Выход", command=close)

window = Menu(mainmenu, tearoff=0)
def settings():
         new_root = Tk()
         new_root.title("TextEditor")
         new_root.resizable(0,0)
         new_root.geometry("700x500")
         fonts = [
            "Arial",
            "Bold",
            "Italianic",
            "Times",
            "sans-serifs"
         ]
         font_fam = ttk.Combobox(new_root, values=fonts, width=40).place(x=10, y=0)
         font_kode = ttk.Combobox(new_root, values="utf-8", width=40).place(x=10, y=40)
         font_size_f = [
            10,20,30,40,50,60,70,80,90
         ]
         font_size = ttk.Combobox(new_root, values=font_size_f, width=100).place(x=10, y=67)
         def color_ch():
            colot_ch = colorchooser.askcolor(color="red")
         color = Button(new_root, width=40, text="Color", command=color_ch).place(x=400, y=20)
         Button(new_root, width=40, text="Ok", command=close).place(x=450, y=480)
window.add_command(label="Настройки", command=settings)
 
mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
mainmenu.add_cascade(label="Окно",
                     menu=window)
#*******************************
nb = ttk.Notebook(canvas)
nb.pack(fill='both', expand='yes')
f1 = Label(text="You can create a new file")
def create_text():
   new_root = Tk()
   new_root.title("TextEditor")
   new_root.resizable(0,0)
   new_root.geometry("700x500")
   nb = ttk.Notebook(new_root)
   nb.pack(fill='both', expand='yes')
   f1 = Text(new_root)
   nb.add(f1, text='Doc1')
   # combobox = ttk.Combobox(new_root2, values=languages)
   #combobox.pack(anchor=NW, padx=7, pady=8)      
   #Name = ttk.Entry(new_root2, width=20).pack(anchor=NW, padx=7, pady=8)
   def save():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = f1.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
   Button(new_root, width=20, height=2,text="Save the Document", command=save).place(x=550, y=460)
Button(f1,width=20, height=2, text="Create a new file", command=create_text).place(x=490, y=340)
#********************************************
f2 = Text(root, background="#333", fg="green")
Button(f2,width=20, height=2, text="Send", bg="blue").place(x=490, y=340)
nb.add(f1, text='Myfiles', image="D:/Mixhost/navruz/new.png")
nb.add(f2, text='Post a review')
root.mainloop()

