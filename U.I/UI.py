# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:35:17 2018

@author: June
"""

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import PIL
from PIL import Image,ImageTk
from tkinter import ttk

class application:
    def __init__(self,master):
        super(application, self).__init__()
        self.master = master
        self.c_size = (700,500)
        
        self.setup_gui(self.c_size)
        self.img=None
        
 
    def setup_gui(self,s):
        
        Label(self.master,text = 'Preview',pady=5,bg='white', font=('Ubuntu',30)).pack()
        self.canvas = Canvas(self.master,height=s[1],width=s[0], bg='black',bd=10,relief='ridge')
        self.canvas.pack()
        txt = '''
                  !
            No Image
        '''
        self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt,font=('',30),fill='white')
        f=Frame(self.master,bg='white',padx=10,pady=10)
        Button(f,text='Open Image',bd=2,fg='white',bg='black',font=('',15),command=lambda: self.make_image(self.canvas)).pack(side=LEFT)
        Button(f,text='Convert',bd=2,fg='white',bg='black',font=('',15),command=lambda: self.make_image(self.canvas)).pack(side=LEFT)
        Button(f,text='Save Text',bd=2,fg='white',bg='black',font=('',15),command=lambda: self.make_image(self.canvas)).pack(side=LEFT)
        Button(f,text='Custom Convert',bd=2,fg='white',bg='black',font=('',15),command=self.create_window).pack(side=LEFT)
        f.pack()
        self.status=Label(self.master,text = 'Current Image: None',bg='gray',font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
        self.status.pack(side=BOTTOM,fill=X)
 
 
    def make_image(self, canvas):
        try:
            File = fd.askopenfilename()
            self.pilImage = Image.open(File)
            re=self.pilImage.resize((350,500),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            canvas.delete(ALL)
            canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,anchor=E,image=self.img)
            self.status['text']='Current Image:'+File
        except:
            ms.showerror('Error!','File type is unsupported.')
            
    def create_window(self):
        newwin = Toplevel()
        #newwin.geometry('700x500')
        Label(newwin, text = 'Preview',pady=5,bg='white', font=('Ubuntu',30)).pack()
        self.canvas1 = Canvas(newwin, height=700,width=500, bg='black',bd=10,relief='ridge')
        self.canvas1.pack()
        txt = '''
                  !
            No Image
        '''
        wt = self.canvas1.create_text(700/2-270,500/2,text=txt,font=('',30),fill='white')
        f=Frame(newwin,bg='white',padx=10,pady=10)
        Button(f,text='Open Image',bd=2,fg='white',bg='black',font=('',15),command=lambda: self.make_image(self.canvas1)).pack(side=LEFT)
        f.pack()
        #display = Label(newwin)
        #display.pack()

root=Tk()
root.configure(bg='white')
root.title('ITT Converter')
application(root)
root.resizable(0,0)
root.mainloop()
        