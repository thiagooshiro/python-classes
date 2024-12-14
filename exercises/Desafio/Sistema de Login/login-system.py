# Estrutura inicial do programa

# Este programa será um sistema simples de login e cadastro de usuários para ser executado no terminal.

# 1. **Estrutura de Dados**:
#    - Utilize um **dicionário** para armazenar os usuários cadastrados.
#    - Cada chave do dicionário será o nome do usuário (uma string).
#    - Cada valor será a senha correspondente (também uma string).

# 2. **Funcionalidades**:
#    - O programa deve exibir um **menu principal** com as seguintes opções:
#        1. Cadastrar um novo usuário.
#        2. Fazer login.
#        3. Listar todos os usuários cadastrados.
#        4. Sair.
#    - O menu deve ser mostrado continuamente até que o usuário escolha "Sair".
#    - Cada opção do menu deve executar uma ação específica:
#        - **Cadastrar um novo usuário**:
#            - Peça ao usuário para digitar um nome de usuário.
#            - Verifique se o nome já está cadastrado no dicionário:
#                - Se já existir, mostre uma mensagem de erro e peça outro nome.
#                - Se não existir, peça uma senha e salve o novo usuário no dicionário.
#        - **Fazer login**:
#            - Peça ao usuário para digitar seu nome e senha.
#            - Verifique se o nome e a senha coincidem com os armazenados no dicionário.
#                - Se forem válidos, mostre uma mensagem de "Login bem-sucedido".
#                - Caso contrário, informe "Nome ou senha incorretos".
#        - **Listar todos os usuários cadastrados**:
#            - Mostre uma lista de todos os nomes de usuários cadastrados.
#            - **Atenção:** Não exiba as senhas.
#        - **Sair**:
#            - Encerre o programa.

# 3. **Requisitos Técnicos**:
#    - Use um loop `while` para manter o programa rodando até que o usuário escolha "Sair".
#    - Use estruturas condicionais (`if`, `elif`, `else`) para tratar as diferentes opções do menu.
#    - Verifique entradas inválidas:
#        - Se o nome de usuário já existir no cadastro, mostre um aviso e não sobrescreva os dados.
#        - Se o nome ou a senha estiverem errados no login, mostre uma mensagem apropriada.
#    - Certifique-se de que o dicionário inicial esteja vazio ao iniciar o programa.

# 4. **Dicas Adicionais**:
#    - Pense na experiência do usuário: mensagens claras ajudam a entender erros.
#    - Use a função `input()` para capturar as entradas do usuário.
#    - Para fins de teste, você pode começar com um usuário pré-cadastrado, mas remova antes de entregar.

# Seu código começa aqui:
