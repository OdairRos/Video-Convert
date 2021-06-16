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

try:
    Arquivo = input('Local do arquivo: ')
    Video = VideoFileClip(Arquivo)
    NOME_ARQUIVO = os.path.basename(Arquivo).split('.')
except:
    print('Arquivo não encontrado, verefique se digitou o local correto\n')

tipo = str(input('Converter para(1-.MP4/2-.AVI/3-.MKV/4-.OGV/5-.WEBM/6-.MP3)'))

if tipo == '1' or tipo.upper() == 'MP4':
    Video.write_videofile(NOME_ARQUIVO[0]+'.mp4', codec=EXTENSION_VIDEOS['.mp4']) # Esta linha esta convertendo o arquivo para o formato desejado, usando o codec correto.
elif tipo == '2' or tipo.upper() == 'AVI':
    Video.write_videofile(NOME_ARQUIVO[0]+'.avi', codec=EXTENSION_VIDEOS['.avi'])
elif tipo == '3' or tipo.upper() == 'MKV':
    Video.write_videofile(NOME_ARQUIVO[0]+'.mkv', codec = EXTENSION_VIDEOS['.mkv'])
elif tipo == '4' or tipo.upper( ) == 'OGV':
    Video.write_videofile(NOME_ARQUIVO[0]+'.ogv', codec=EXTENSION_VIDEOS['.mkv'])
elif tipo == '5' or tipo.upper() == 'WEBM':
    Video.write_videofile(NOME_ARQUIVO[0]+'.webm', codec=EXTENSION_VIDEOS['.wemb'])
elif  tipo == '6' or tipo.upper() == 'MP3':
    print('modificar')
    """
    mp3audio = 'resultado.mp3'
    VideoClip = VideoFileClip(Arquivo)
    AudioClip = VideoClip.audio
    AudioClip.write_audiofile()
    VideoClip.close()
    AudioClip.close()
    """

Video.close()





