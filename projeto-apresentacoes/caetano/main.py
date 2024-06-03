from consolemenu import *
from consolemenu.items import *

tarefas = list()

menu = ConsoleMenu("Tarefas Diárias")

categorias = ["Indefinida", "Dom�stica", "Escolar", "Manuten��o", "Criativas", "Aprendizado", "Pesquisa"]

prioridades = ["Indefinida", "Muito Baixa", "Baixa", "M�dia", "Alta", "Muito Alta"]

print(type(prioridades), type(categorias))

def KeySort(e):
    return prioridades.index(e["Prioridade"])

def testar(string):
    try:
        float(string) and bool(string)
        return False
    except:
        return True

def testForAlreadyExist(string):
    if len(tarefas) > 0:
        for i in tarefas:
            if i["Nome"] == string:
                return False
            else:
                return True
    else:
        return True
    

def addTarefa():
    nome = input("Insira um nome para a tarefa: ")
    desc = input("Insira uma descri��o para a tarefa: ")
    prioridade = input(f"Insira a prioridade da tarefa ({prioridades}): ")
    categoria = input(f"Insira a categoria da tarefa ({categorias}): ")

    tarefaNova = {
        "Nome": nome if testar(nome) == True and testForAlreadyExist(nome) == True else "Invalido",
        "Descri��o": desc if testar(desc) == True else "Sem descri��o.",
        "Prioridade": prioridade if prioridade in prioridades else "Indefinida",
        "Categoria": categoria if categoria in categorias else "Indefinida",
        "Comple��o": "Inconclu�do"
    }

    if tarefaNova["Nome"] != "Invalido":
        tarefas.append(tarefaNova)
        Screen.println("Tarefa adicionada.")
    else:
        Screen.println("Nome e/ou descri��o inv�lido(s).")

    
    input("Pressione enter para continuar...")

def listTarefa():
    if len(tarefas) > 0:
        tarefas.sort(key=KeySort, reverse=True)
        for i in tarefas:
            Screen.println("Tarefa", tarefas.index(i))
            for chave, valor in i.items():
                Screen.println(f"{chave}: {valor}")
            Screen.println("---------------------------")
        input("Pressione enter para continuar...")
    else:
        Screen.println("Nenhuma tarefa.")
        input("Pressione enter para continuar...")

def completeTarefa():
    nome = input("Insira o nome da tarefa que deseja concluir: ")

    if len(tarefas) > 0:
        for i in tarefas:
            if i["Nome"] == nome:
                if i["Comple��o"] == "Inconclu�do":
                    i["Comple��o"] = "Conclu�do"
                    i["Prioridade"] = "Indefinida"
                    Screen.println(f'Tarefa de "{nome}" conclu�da.')
                    input("Pressione enter para continuar...")
                    return
                else:
                    Screen.println(f'Tarefa de "{nome}" j� estava conclu�da')
                    input("Pressione enter para continuar...")
                    return
        Screen.println("Nenhuma tarefa com este nome.")
        input("Pressione enter para continuar...")
    else:
        Screen.println("Nenhuma tarefa.")
        input("Pressione enter para continuar...")

def showTarefas():
    escolha = input("Deseja exibir as tarefas por categoria ou prioridade: ")
    filtro = input("Insira a categoria ou prioridade para exibir tarefas contidas na mesma: ")

    if escolha == "categoria":
        if filtro in categorias:
            if len(tarefas) > 0:
                tarefasNew = list()
                for i in tarefas:
                    if i["Categoria"] == filtro:
                        tarefasNew.append(i)
                tarefasNew.sort(key=KeySort, reverse=True)
                for i in tarefasNew:
                    Screen.println("Tarefa", tarefas.index(i))
                    for chave, valor in i.items():
                        Screen.println(f"{chave}: {valor}")
                    Screen.println("---------------------------")
                input("Pressione enter para continuar...")
            else:
                Screen.println("Nenhuma tarefa.")
                input("Pressione enter para continuar...")
        else:
            Screen.println("Categoria inv�lida, listando categorias.")
            for i in categorias:
                Screen.println(i)
            input("Pressione enter para continuar...")
    elif escolha == "prioridade":
        if filtro in prioridades:
            if len(tarefas) > 0:
                tarefasNew = list()
                for i in tarefas:
                    if i["Prioridade"] == filtro:
                        tarefasNew.append(i)
                tarefasNew.sort(key=KeySort)
                for i in tarefasNew:
                    Screen.println("Tarefa", tarefas.index(i))
                    for chave, valor in i.items():
                        Screen.println(f"{chave}: {valor}")
                    Screen.println("---------------------------")
                input("Pressione enter para continuar...")
            else:
                Screen.println("Nenhuma tarefa.")
                input("Pressione enter para continuar...")
        else:
            Screen.println("Prioridade inv�lida, listando prioridades.")
            for i in prioridades:
                Screen.println(i)
            input("Pressione enter para continuar...")
    else:
        Screen.printf("Escolha inv�lida.")
        input("Pressione enter para continuar...")

item1 = FunctionItem(text="Adicionar uma nova tarefa.", function=addTarefa, menu=menu)
item2 = FunctionItem(text="Listar todas as tarefas.", function=listTarefa, menu=menu)
item3 = FunctionItem(text="Concluir uma tarefa.", function=completeTarefa, menu=menu)
item4 = FunctionItem(text="Exibir todas as tarefas de uma categoria ou prioridade.", function=showTarefas, menu=menu)

menu.append_item(item1)
menu.append_item(item2)
menu.append_item(item3)
menu.append_item(item4)

menu.show()