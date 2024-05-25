from tkinter import *

janela = Tk()


label = Label(janela, text="Isso é uma janela", font=('Arial', 32))
label.pack()

frame = Frame(janela, width=40, height=40, relief=SUNKEN, bd=50, bg='lightgrey')
frame.pack()

# canvas = Canvas(janela, width=600, height=500)
# canvas.pack()

# canvas.create_rectangle(100, 100, 1000, 600, fill='blue')

check_var = BooleanVar()

check_button = Checkbutton(janela, text='Aceitar os termos!', variable=check_var)
check_button.pack()


radio_var = StringVar()

radio1 = Radiobutton(janela, text='Opção 1', variable=radio_var, value='opção1')
radio2 = Radiobutton(janela, text='Opção 2', variable=radio_var, value='opção?', state='normal' )
radio1.pack()
radio1.invoke()
radio2.pack()

scale_var = DoubleVar()
scale = Scale(janela, width=200, from_=0, to=100, orient='horizontal',variable=scale_var)
scale.pack()


def click_button():
    label.config(text=radio_var.get())


button =  Button(janela, width=100, text='Clique em mim', command=click_button)
button.pack()

janela.mainloop()
