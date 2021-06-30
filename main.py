from tkinter import *
import downloader

downloader = downloader.downloader()

window = Tk()

w = 800
h = 30

w_screen = window.winfo_screenwidth()
h_screen = window.winfo_screenheight()

position_x = (w_screen/2) - (w/2)
position_y = (h_screen/2) - (h/2)

window.geometry(f'{w}x{h}+{int(position_x)}+{int(position_y)}')
window.resizable(False, False)
window['bg'] = '#808080'

youtube_link = Entry(
    window,
    width=70,
    font='Arial 12'
)

youtube_link.place(x=5, y=3)

download_button = Button(
    window,
    text='Baixar',
    width=20,
    command=lambda:downloader.verificacao(youtube_link)
).place(x=645, y=3)

window.mainloop()