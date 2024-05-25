from tkinter import *

janela = Tk()

meu_menu = Menu(janela)
janela.config(menu=meu_menu)
file_menu = Menu(meu_menu)
meu_menu.add_cascade(label='Arquivo', menu=file_menu)
file_menu.add_command(label='Abrir')
file_menu.add_command(label='Salvar')
file_menu.add_separator()
file_menu.add_command(label='Sair')


janela.mainloop()
