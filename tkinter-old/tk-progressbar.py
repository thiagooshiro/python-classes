from tkinter import *
from tkinter.ttk import *



janela = Tk()

janela.resizable(True, True) 



progress_bar  = Progressbar(janela, orient='horizontal', length=200, mode='determinate')
progress_bar.pack()
progress_bar.start(50)

size_grip = Sizegrip(janela)

size_grip.pack(anchor=SE, padx='3', expand=True)

janela.mainloop()