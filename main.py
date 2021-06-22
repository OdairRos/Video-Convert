from os import *
from moviepy.editor import *
from sys import *

EXTENSION_VIDEOS ={
    #   'extensão': 'codec'
    '.mkv': 'mpeg4',
    '.avi': 'mpeg4',
    '.mp4': 'mpeg4',
    '.ogv': 'libtheora',
    '.webm': 'libvpx'
    }

class main(object):
    def __init__(self):
    
        try:
            self.LocalArquivo = input('Local: ')
            self.NOME_ARQUIVO = os.path.basename(self.LocalArquivo).split('.')
            self.VideoClipe = VideoFileClip(self.LocalArquivo)
            self.AudioClipe = self.VideoClipe.audio
        except:
         print('Arquivo não encontrado, Verefique se o local esta correto.')

class Convert(main):
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


if __name__ == '__main__':
    projeto = Convert()

