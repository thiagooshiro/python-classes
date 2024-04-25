from tkinter import *
from tkinter.ttk import *



janela = Tk()

valores = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')

combo_box = Combobox(janela, values=valores, state='readonly')
combo_box.pack(padx=20, pady=10)

size_grip = Sizegrip(janela)
size_grip.pack(anchor=SE, padx=3, pady=3, expand=True)

progress_bar = Progressbar(janela, orient='horizontal', length=500, mode='determinate')
progress_bar.pack(padx=10, pady=10)
progress_bar.start(100)



janela.mainloop()