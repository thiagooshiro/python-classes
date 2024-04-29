from tkinter import *
from tkinter.ttk import *

janela = Tk()

janela.title('Exemplo combo-box')


dias_da_semana = ['Segunda', 'Terça', 'Quarta']

combo_box = Combobox(janela, values=dias_da_semana)
combo_box.pack(padx=75, pady=20)

janela.mainloop()