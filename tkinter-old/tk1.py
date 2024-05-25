from tkinter import *

janela = Tk()


label = Label(janela, text="Isso é uma janela", font=('Arial', 32))
label.pack()

texto_nome = StringVar()
texto_idade = StringVar()
texto_nota = StringVar()

input_nome = Entry(janela, textvariable=texto_nome, bg='lightgrey', width=200)
input_nome.pack()

input_idade = Entry(janela)
input_idade.pack()

input_nota = Entry(janela, textvariable=texto_nota, bg='lightgrey', width=200)
input_nota.pack()


# text_box = Text(janela, height=50, width=70 )
# text_box.pack()

# text_box.insert(END, 'Esse é um exemplo de caixa de texto')





def click_button():
    label.config(text=input_idade.get())


button =  Button(janela, width=100, text='Clique em mim', command=click_button)
button.pack()

janela.mainloop()
