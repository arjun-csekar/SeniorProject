# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:35:19 2018

@author: June
"""
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Handwritting Recognition")

def openFile():
    global panel
    window.fileName = filedialog.askopenfilename(filetypes = [('Image Files', '.png .jpg')])
    if window.fileName != "":
        print(window.fileName)
        img = ImageTk.PhotoImage(Image.open(window.fileName))
        window2 = tk.Toplevel()
        window2.geometry('700x700')
        panel = tk.Label(window2, image = img)
        
        panel.image = img
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window2.mainloop()

def saveFile():
    fout = filedialog.asksaveasfile(mode='w', filetypes = [('text files', '.png')])
    text = input("Input text to save: ")
    print("Text Saved")
    fout.write(text)
    fout.close()
    #panel.image.save(fout, 'PNG')
    
B = tk.Button(window, text = "Open", command = lambda: openFile())
B.place(x = 50,y = 50)

B2 = tk.Button(window, text = "Save", command = lambda: saveFile())
B2.place(x = 50,y = 100)
    
window.mainloop()

