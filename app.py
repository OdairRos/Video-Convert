from moviepy.editor import *
from os import *
import time as tm

"""
É possivel converter videos somente nos formatos abaixo:

.Mkv para .AVI, .MP4, .OGV, .WEBM

todos tendo volta de conversção ou seja

MP4 para AVI  <-->  AVI para MP4

"""

#constantes
EXTENSION_VIDEOS ={
    #'extensão': 'codec'
    '.mkv': 'mpeg4',
    '.avi': 'mpeg4',
    '.mp4': 'mpeg4',
    '.ogv': 'libtheora',
    '.webm': 'libvpx'
    }

class App(object):
    def __init__(self, Local):
        self.Local = Local
        
    def ConvertVideo(self, tipo):
        try:   
            # Para pegar o nome do arquivo
            self.NOME_ARQUIVO = os.path.basename(self.Local).split('.')
            self.VideoClipe = VideoFileClip(self.Local)
            self.AudioClipe = self.VideoClipe.audio
        except:
            print('[ERRO!]Arquivo não encontrado, Verefique se o local esta correto.')

        if tipo in EXTENSION_VIDEOS:
            self.VideoClipe.write_videofile(self.NOME_ARQUIVO[0]+tipo, codec=f'{EXTENSION_VIDEOS[tipo]}' )
            self.VideoClipe.close()
            self.AudioClipe.close()
            print('Conversão concluida com secesso! (Salvo no diretorio do arquivo selecionado)')
        else: print("[ERRO!]Não podemos converter para este tipo de formato de video")

    def ConvertVideoToAudio(self, tipo='.mp3'):
        try:   
            self.NOME_ARQUIVO = os.path.basename(self.Local).split('.')
            self.VideoClipe = VideoFileClip(self.Local)
            self.AudioClipe = self.VideoClipe.audio
        except:
            print('[ERRO!]Arquivo não encontrado, Verefique se o local esta correto.')

        self.AudioClipe.write_audiofile(f'{self.NOME_ARQUIVO[0]}{tipo}')
        self.VideoClipe.close()
        self.AudioClipe.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Conversão concluida com secesso! (Salvo no diretorio do arquivo selecionado)')


Lcl = input("Digite o diretorio em que seu arquivo esta.[EX: C:\Myvideos\Myvdeo.mp4] -> ")
Conversor = App(Lcl)
formato = input('Em qual formato deseja converter seu video?Digite no formato .extensao(EX: .MP4, .AVI, .MKV, .OGV, .WEBM) -> ')
Conversor.ConvertVideo(formato)
        

