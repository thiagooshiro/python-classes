from tkinter import *

janela = Tk()


label = Label(janela, text="Isso é uma janela", font=('Arial', 12), fg='#6A5ACD')
label.pack()

def click_button():
    label.config(text='Botão clicado')

button =  Button(janela, text='Clique em mim', command=click_button)
button.pack()

janela.mainloop()