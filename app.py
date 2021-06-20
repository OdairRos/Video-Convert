#import main


import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, FLAT, LAST, LEFT, RAISED, RIGHT
import tkinter.ttk as ttk

LOGOIMG = 'C:IMG\Menu-imageLogoCropped.ppm'
BUTTON_CONFIG = {'border': '5', 'relief': 'raised','fg': 'black','bg': '#ffffff', 'font': ('sans serif','13', 'bold' )}
LABEL_CONFIG = {'fg': 'black','bg': '#ffffff', 'font': ('sans serif','13', 'bold' )}

class App(object):
    def __init__(self):
        self.Aplicativo = tk.Tk()
        self.Aplicativo.title('PyConvert')
        self.Aplicativo.geometry("700x400")
        self.LOGO = tk.PhotoImage(file = LOGOIMG)

        self.frames = [tk.Frame(self.Aplicativo).pack() for i in range(0,5)]# Criando os Frames(locais para cada widget) e "adcionando" eles na tela com o metodo pack()
        
        self.LG = tk.Label(self.frames[0], image=self.LOGO, bg='#ffffff').pack()

        self.Entry = tk.Entry(self.frames[2], textvariable='odair').pack()

        self.btnMP4 = tk.Button(self.frames[3], BUTTON_CONFIG, text='To MP4', command=None, padx=20).pack(side=LEFT,padx=5) 
        self.btnAVI = tk.Button(self.frames[3], BUTTON_CONFIG, text='To AVI', command=None, padx=20).pack(side=LEFT,padx=5)

        self.Aplicativo.configure(background='#ffffff')#385ce0

        self.Aplicativo.mainloop()

app = App()
