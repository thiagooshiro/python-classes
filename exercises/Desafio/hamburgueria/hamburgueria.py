# Estrutura inicial do programa

# Este programa será um sistema para gerenciar uma hamburgueria com funções administrativas e de cliente.

# 1. **Estrutura de Dados**:
#    - Crie um **dicionário** para armazenar os usuários cadastrados:
#        - Cada chave será o nome do usuário (uma string).
#        - O valor será uma tupla contendo a senha (string) e o tipo de usuário (string: "admin" ou "cliente").
#    - Crie uma **lista** para armazenar os hambúrgueres disponíveis no cardápio.
#        - Cada hambúrguer será um dicionário com "nome" (string) e "preço" (float).

# 2. **Funcionalidades**:
#    - O programa deve começar solicitando um **login**.
#        - Verifique se o nome e a senha fornecidos correspondem ao cadastro.
#        - Identifique o tipo de usuário: "admin" ou "cliente".
#    - Após o login:
#        - Para administradores:
#            1. Adicionar um novo hambúrguer ao cardápio.
#            2. Remover hambúrgueres do cardápio.
#            3. Listar todos os hambúrgueres cadastrados.
#            4. Sair do sistema.
#        - Para clientes:
#            1. Visualizar o cardápio.
#            2. Fazer um pedido.
#            3. Sair do sistema.
#    - O menu deve ser mostrado continuamente até que o usuário escolha "Sair".
#    - Cada ação deve ter uma lógica específica:
#        - **Adicionar hambúrguer (admin)**:
#            - Peça o nome e o preço do hambúrguer.
#            - Adicione-o à lista de cardápio.
#        - **Remover hambúrguer (admin)**:
#            - Mostre o cardápio com números para escolha.
#            - Peça o número do hambúrguer a ser removido.
#            - Verifique se o número é válido antes de remover.
#        - **Fazer pedido (cliente)**:
#            - Mostre o cardápio com preços.
#            - Peça ao cliente para escolher um ou mais hambúrgueres.
#            - Mostre o valor total do pedido.

# 3. **Requisitos Técnicos**:
#    - Use um loop `while` para manter o programa rodando até que o usuário escolha "Sair".
#    - Use estruturas condicionais (`if`, `elif`, `else`) para tratar as diferentes opções dos menus.
#    - Verifique entradas inválidas:
#        - No login, mostre uma mensagem apropriada se o nome ou senha estiverem incorretos.
#        - Nas escolhas de cardápio, mostre um erro se o número escolhido não for válido.
#    - Certifique-se de que o dicionário de usuários e a lista de cardápio tenham pelo menos:
#        - Um administrador padrão cadastrado para testar.
#        - Alguns hambúrgueres iniciais cadastrados.

# 4. **Dicas Adicionais**:
#    - Mantenha o programa organizado em blocos de funcionalidades.
#    - Lembre-se de que a lista de hambúrgueres é compartilhada entre administradores e clientes.
#    - Use `input()` para capturar as escolhas dos usuários e mensagens claras para orientar suas ações.

# Seu código começa aqui:
