### **Exercício 3: Sistema de Funcionamento de uma Hamburgueria**
#### **Texto Introdutório**:
Você foi contratado para criar o sistema de funcionamento de uma hamburgueria! Este sistema terá dois tipos de login: **administrativo** e **usuário comum**. O administrador poderá gerenciar o cardápio (adicionar, listar, e remover hambúrgueres). Já o usuário poderá visualizar o cardápio e fazer pedidos. É uma oportunidade perfeita para praticar o uso de listas, dicionários, loops e condicionais.

#### **Requisitos**:

##### **1. Inicialização**
- O programa deve começar com:
  - Um cardápio vazio (uma lista de hambúrgueres).
  - Um dicionário de usuários, contendo pelo menos um administrador cadastrado:
    ```python
    usuarios = {"admin": {"senha": "1234", "tipo": "admin"}}
    ```

##### **2. Lógica de Login**
- **Ao iniciar**, o sistema deve solicitar que o usuário faça login.
- O login deve ser validado:
  - Nome de usuário e senha corretos.
  - Exibir mensagens apropriadas caso o login falhe.
- Após o login:
  - **Administrador** terá acesso ao menu administrativo.
  - **Usuário comum** verá opções para fazer pedidos e visualizar o cardápio.

##### **3. Funções do Administrador**
O menu administrativo deve oferecer as seguintes opções:
1. **Adicionar Hambúrguer**:
   - Solicitar o nome e preço do hambúrguer.
   - Adicionar o hambúrguer ao cardápio como um dicionário, por exemplo:
     ```python
     {"nome": "Cheeseburger", "preco": 15.00}
     ```
   - Validar se o hambúrguer já existe antes de adicionar.
2. **Listar Hambúrgueres**:
   - Exibir todos os hambúrgueres do cardápio com preços.
   - Mostrar uma mensagem caso o cardápio esteja vazio.
3. **Remover Hambúrguer**:
   - Solicitar o nome do hambúrguer a ser removido.
   - Validar se o nome existe antes de remover.
4. **Sair**:
   - Encerrar o menu administrativo.

##### **4. Funções do Usuário Comum**
O menu do usuário deve oferecer as seguintes opções:
1. **Visualizar Cardápio**:
   - Exibir todos os hambúrgueres do cardápio com preços.
   - Mostrar uma mensagem caso o cardápio esteja vazio.
2. **Fazer Pedido**:
   - Solicitar que o usuário escolha hambúrgueres pelo nome (permitir múltiplos pedidos).
   - Exibir o total do pedido ao final.
   - Informar caso algum hambúrguer não exista.
3. **Sair**:
   - Encerrar o menu do usuário.

##### **5. Lógica de Funcionamento**
- O programa deve funcionar em um loop contínuo, alternando entre login e menus, até que o administrador ou o usuário escolha sair.
- O sistema deve sempre verificar permissões para garantir que apenas administradores possam alterar o cardápio.

---

#### **Extras (Opcional)**
- Adicionar a opção de **cadastrar novos usuários** (somente administradores).
- Incluir categorias no cardápio, como "Hambúrgueres Clássicos" e "Especiais."
- Implementar um sistema de estoque para limitar a quantidade de hambúrgueres disponíveis.
- Salvar os dados (usuários e cardápio) em arquivos para que o sistema não reinicie vazio.
