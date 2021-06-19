#import main

import tkinter as tk
import tkinter.ttk as ttk
class Main(object):
    def __init__(self):
        
        self.Aplicativo = tk.Tk()
        self.Aplicativo.title('PyConvert')
        self.Aplicativo.geometry("700x400")
        self.a = tk.Frame()
        self.a.pack()
        self.b = tk.Label(self.a,text = 'PyConvert!',bg = 'blueviolet',font = 'Corbel, 12', pady='350px')
        self.b.pack()
        
        self.Aplicativo.configure(background='blueviolet')#385ce0
        self.Aplicativo.mainloop()
class App(Main):
    def __init__(self):
        super().__init__()

app = App()
