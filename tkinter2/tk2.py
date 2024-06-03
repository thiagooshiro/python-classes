from tkinter import *
from tkinter.ttk import * 

janela = Tk()
janela.title('Tree View app')

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]

emails = ["alice@example.com", "bob@example.com", "charlie@example.com", "david@example.com", "emma@example.com", "frank@example.com", "grace@example.com", "henry@example.com", "ivy@example.com", "jack@example.com"]

phone_numbers = ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234", "678-901-2345", "789-012-3456", "890-123-4567", "901-234-5678", "012-345-6789"]



tree_view = Treeview(janela)

tree_view['columns'] = ('nome', 'email', 'telefone')

tree_view.column('#0', width=100, minwidth=100, anchor='center')
tree_view.column('nome', width=150, minwidth=150, anchor='center')
tree_view.column('email', width=150, minwidth=150, anchor='center')
tree_view.column('telefone', width=150, minwidth=150, anchor='center')


tree_view.heading('#0', text='ID')
tree_view.heading('nome', text='NOME')
tree_view.heading('email', text='EMAIL')
tree_view.heading('telefone', text='TEL')

label_name = Label(janela, text='Digite seu nome')
entry_name = Entry(janela, width=100)
label_name.pack()
entry_name.pack()

label_email = Label(janela, text='Digite seu email')
entry_email = Entry(janela, width=100)
label_email.pack()
entry_email.pack()

def add_people():
    name = entry_name.get()
    email = entry_email.get()
    id = len(tree_view.get_children())
    # last_id = (tree_view.get_children()[-1])
    tree_view.insert('', END, text=id+1, values=(name, email, '123'))
    # last_value = tree_view.index(last_id)
    # item2 = tree_view.item(last_id)
    # tree_view.move(item, "", last_value) # troca a ordem do penultimo valor com o último valor adicionado na lista.



button = Button(janela, text='Adicionar', command=add_people)
button.pack()


i = 0
for name in names:
    tree_view.insert("", END, text=i+1, values=(name, emails[i], phone_numbers[i]))
    i += 1

tree_view.pack()

janela.mainloop()