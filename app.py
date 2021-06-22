#from Main import *

import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, FALSE, FLAT, LAST, LEFT, RAISED, RIGHT, HORIZONTAL
import tkinter.ttk as ttk
from tkinter import filedialog as fd


#constantes
LOGOIMG = 'C:IMG\Menu-imageLogoCropped.ppm'
BUTTON_CONFIG = {'border': '5', 'relief': 'raised','fg': 'black','bg': '#ffffff', 'font': ('sans serif','13', 'bold' )}
LABEL_CONFIG = {'fg': 'black','bg': '#ffffff', 'font': ('sans serif','12', 'italic' )}



class App(object):
    def __init__(self):
        #Tkinter Contruindo tela
        self.root = tk.Tk()
        self.root.title('PyConvert')
        self.root.geometry("800x500")
        self.root.resizable(FALSE,FALSE)
        self.root.configure(background='#ffffff')#385ce0
        self.IMG = tk.PhotoImage(file = LOGOIMG)

        self.LOGO = tk.Label(self.root, image=self.IMG, bg='#ffffff').place(x=250, y=0)

        self.btnLocal = tk.Button(self.root, fg='black', bg='#ffffff',text='Escolher local do arquivo', command=fd.askopenfilename).place(x=340, y=150)


        self.btnMP4 = tk.Button(self.root, BUTTON_CONFIG, text='To MP4 ', command=None, padx=20).place(x=50,y=250)
        self.btnAVI = tk.Button(self.root, BUTTON_CONFIG, text='To AVI ', command=None, padx=20).place(x=183,y=250)
        self.btnMKV = tk.Button(self.root, BUTTON_CONFIG, text='To MKV ', command=None, padx=20).place(x=310,y=250)
        self.btnOGV = tk.Button(self.root, BUTTON_CONFIG, text='To OGV ', command=None, padx=20).place(x=450, y=250)
        self.bntWEBM = tk.Button(self.root, BUTTON_CONFIG, text='To WEBM', command=None, padx=20).place(x=592, y=250)

        #self.progress = ttk.Progressbar(self.root, orient = HORIZONTAL,length = 500, mode = 'determinate').place(x=140,y=370)
        self.root.mainloop()

    
app = App()
