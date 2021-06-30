from logging import root
import pytube
from tkinter import messagebox, filedialog as fd


class downloader:
    def __init__(self):
        pass

    def verificacao(self, url):
        url = url.get()

        try:
            youtube = pytube.YouTube(url)
            video = youtube.streams.get_highest_resolution()

            titulo = video.title

            msgBox = messagebox.askquestion('Deseja realmente baixar este vídeo?', f'Video: {titulo}')

            if msgBox == 'yes':
                diretorio_selecionado = fd.askdirectory()
                video.download(diretorio_selecionado)

                msgBox = messagebox.showinfo('Download concluído!', 'Parabéns, seu vídeo foi baixado com sucesso! =D')

        except Exception as e:
            msgBox = messagebox.showerror('Erro:', 'Por favor informe um link válido do youtube ou verifique sua conexão com a internet.')
            print(e)
