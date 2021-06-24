import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from moviepy.editor import *
from os import *




#constantes
EXTENSION_VIDEOS ={
    #   'extensão': 'codec'
    '.mkv': 'mpeg4',
    '.avi': 'mpeg4',
    '.mp4': 'mpeg4',
    '.ogv': 'libtheora',
    '.webm': 'libvpx'
    }
LOGOIMG = 'C:IMG\Menu-imageLogoCropped.ppm'
BUTTON_CONFIG = {'border': '5', 'relief': 'raised','fg': 'black','bg': '#ffffff', 'font': ('sans serif','13', 'bold' )}
LABEL_CONFIG = {'fg': 'black','bg': '#ffffff', 'font': ('sans serif','12', 'italic' )}

#variaveis globais
Local = str('None')


#funções
def GetLocal():
    global Local
    Local = fd.askopenfilename()




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

        self.btnLocal = tk.Button(self.root, fg='black', bg='#ffffff',text='Escolher local do arquivo', command=GetLocal).place(x=340, y=150)


        self.btnMP4 = tk.Button(self.root, BUTTON_CONFIG, text='To MP4 ', command=lambda : self.ConvertVideo('.mp4'), padx=20).place(x=50,y=250)
        self.btnAVI = tk.Button(self.root, BUTTON_CONFIG, text='To AVI ', command=lambda: self.ConvertVideo('.avi'), padx=20).place(x=183,y=250)
        self.btnMKV = tk.Button(self.root, BUTTON_CONFIG, text='To MKV ', command=lambda: self.ConvertVideo('.mkv'), padx=20).place(x=310,y=250)
        self.btnOGV = tk.Button(self.root, BUTTON_CONFIG, text='To OGV ', command=lambda: self.ConvertVideo('.ogv'), padx=20).place(x=450, y=250)
        self.bntWEBM = tk.Button(self.root, BUTTON_CONFIG, text='To WEBM', command=lambda: self.ConvertVideo('.webm'), padx=20).place(x=592, y=250)
        
        #self.progress = ttk.Progressbar(self.root, orient = HORIZONTAL,length = 500, mode = 'determinate').place(x=140,y=370)
        self.root.mainloop()
        
    def ConvertVideo(self, tipo):
        global Local
        try:   
            self.NOME_ARQUIVO = os.path.basename(Local).split('.')
            self.VideoClipe = VideoFileClip(Local)
            self.AudioClipe = self.VideoClipe.audio
        except:
            print('Arquivo não encontrado, Verefique se o local esta correto.')

        print(Local)
        self.VideoClipe.write_videofile(self.NOME_ARQUIVO[0]+tipo, codec=f'{EXTENSION_VIDEOS[tipo]}')
        self.VideoClipe.close()
        self.AudioClipe.close()

    def ConvertVideoToAudio(self, tipo='.mp3'):
        global Local
        try:   
            self.NOME_ARQUIVO = os.path.basename(Local).split('.')
            self.VideoClipe = VideoFileClip(Local)
            self.AudioClipe = self.VideoClipe.audio
        except:
            print('Arquivo não encontrado, Verefique se o local esta correto.')

        self.AudioClipe.write_audiofile(f'{self.NOME_ARQUIVO[0]}{tipo}')
        self.VideoClipe.close()
        self.AudioClipe.close()

if __name__ == '__main__':
        pass

