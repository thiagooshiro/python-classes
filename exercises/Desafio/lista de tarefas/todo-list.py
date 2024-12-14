# Estrutura inicial do programa

# Este programa será uma lista de tarefas que funciona no terminal.

# 1. **Estrutura de Dados**:
#    - Utilize uma **lista** para armazenar as tarefas.
#    - Cada tarefa será uma **string** representando o texto da tarefa (ex.: "Comprar pão").

# 2. **Funcionalidades**:
#    - O programa deve exibir um **menu principal** com as seguintes opções:
#        1. Adicionar uma nova tarefa.
#        2. Listar todas as tarefas.
#        3. Remover uma tarefa.
#        4. Sair.
#    - O menu deve ser mostrado continuamente até que o usuário escolha "Sair".
#    - Cada opção do menu deve executar uma ação específica:
#        - **Adicionar uma nova tarefa**:
#            - Peça ao usuário para digitar o texto da tarefa.
#            - Adicione o texto na lista de tarefas.
#        - **Listar todas as tarefas**:
#            - Exiba todas as tarefas atualmente armazenadas na lista.
#            - Cada tarefa deve ser exibida com um número correspondente ao índice na lista (começando em 1).
#        - **Remover uma tarefa**:
#            - Peça ao usuário para inserir o **número** da tarefa que deseja remover.
#            - Verifique se o número é válido (ou seja, se existe uma tarefa correspondente).
#            - Remova a tarefa da lista se for válida.
#        - **Sair**:
#            - Encerre o programa.

# 3. **Requisitos Técnicos**:
#    - Use um loop `while` para manter o programa rodando até que o usuário escolha "Sair".
#    - Use estruturas condicionais (`if`, `elif`, `else`) para tratar as diferentes opções do menu.
#    - Verifique entradas inválidas:
#        - Se o usuário tentar remover uma tarefa inexistente (número fora do intervalo), mostre uma mensagem de erro.
#        - Se o usuário escolher uma opção inválida no menu, informe e peça outra escolha.
#    - Certifique-se de que a lista inicial esteja vazia ao iniciar o programa.

# 4. **Dicas Adicionais**:
#    - Teste cada funcionalidade separadamente para garantir que o programa funcione corretamente.
#    - Pense na experiência do usuário: as mensagens devem ser claras e amigáveis.
#    - Use a função `input()` para capturar as escolhas do usuário.
#    - Para converter o número da tarefa em índice da lista, lembre-se que os índices de listas começam em 0.

# Seu código começa aqui:
