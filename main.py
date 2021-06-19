from os import *
from moviepy.editor import *
from sys import *
import app as application

EXTENSION_VIDEOS ={
    #   'extensão': 'codec'
    '.mkv': 'mpeg4',
    '.avi': 'mpeg4',
    '.mp4': 'mpeg4',
    '.ogv': 'libtheora',
    '.webm': 'libvpx'
    }

class Main(object):
    def __init__(self):
        try:
            self.LocalArquivo = str(input('Local do arquivo: '))
            self.NOME_ARQUIVO = os.path.basename(self.LocalArquivo).split('.')
            self.VideoClipe = VideoFileClip(self.LocalArquivo)
            self.AudioClipe = self.VideoClipe.audio
        except:
            print('Arquivo não encontrado, Verefique se o local esta correto.')

class Convert(Main):
    def __init__(self):
        super().__init__()
        
        
    def ConvertVideo(self, tipo):
        self.VideoClipe.write_videofile(self.NOME_ARQUIVO[0]+tipo, codec=f'{EXTENSION_VIDEOS[tipo]}')
        self.VideoClipe.close()
        self.AudioClipe.close()

    def ConvertVideoToAudio(self, tipo='.mp3'):
        self.AudioClipe.write_audiofile(f'{self.NOME_ARQUIVO[0]}{tipo}')
        self.VideoClipe.close()
        self.AudioClipe.close()


    
Projeto = Convert()
tipo = str(input('Converter para(1-.MP4/2-.AVI/3-.MKV/4-.OGV/5-.WEBM/6-.MP3)'))

if tipo == '1' or tipo == 'MP4': Projeto.ConvertVideo('.mp4')
elif tipo == '2' or tipo == 'AVI': Projeto.ConvertVideo('.avi')
elif tipo == '3' or tipo == 'MKV': Projeto.ConvertVideo('.mkv')
elif tipo == '4' or tipo == 'OGV': Projeto.ConvertVideo('.ogv')
elif tipo == '5' or tipo == 'WEBM': Projeto.ConvertVideo('.webm')
elif tipo == '6' or tipo == 'MP3': Projeto.ConvertVideoToAudio()

