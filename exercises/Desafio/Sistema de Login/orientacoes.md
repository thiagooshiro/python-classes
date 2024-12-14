### **Exercício 2: Sistema de Login**
#### **Texto Introdutório**:
Neste exercício, você implementará um sistema básico de login para simular o funcionamento de autenticação de usuários. O programa deve permitir que o usuário se cadastre, faça login e veja uma mensagem de boas-vindas. Você usará dicionários para armazenar as informações dos usuários e aplicará estruturas condicionais para validar os acessos.

#### **Requisitos**:
1. **Inicialização**:
   - O programa deve começar com um dicionário vazio, onde cada chave será um nome de usuário e o valor será a senha correspondente.
2. **Menu Principal**:
   - O programa deve exibir as seguintes opções:
     1. Cadastrar um novo usuário.
     2. Fazer login.
     3. Listar usuários cadastrados.
     4. Sair.
3. **Lógica de Funcionamento**:
   - O programa deve funcionar em um loop contínuo até que o usuário escolha sair.
   - Cada opção deve ser validada para evitar erros.
4. **Detalhes das Opções**:
   - **Cadastrar Novo Usuário**:
     - Solicitar um nome de usuário e uma senha.
     - Verificar se o nome de usuário já existe antes de cadastrar.
     - Informar o sucesso ou falha do cadastro.
   - **Fazer Login**:
     - Solicitar o nome de usuário e a senha.
     - Verificar se o nome de usuário existe no dicionário.
     - Verificar se a senha está correta.
     - Mostrar mensagens adequadas (login bem-sucedido ou erro).
   - **Listar Usuários Cadastrados**:
     - Exibir todos os nomes de usuários cadastrados (sem as senhas).
     - Mostrar uma mensagem caso não haja usuários cadastrados.
   - **Sair**:
     - Encerrar o programa com uma mensagem de despedida.
5. **Extras (Opcional)**:
   - Limitar tentativas de login antes de bloquear o usuário temporariamente.
   - Permitir a exclusão de usuários cadastrados.

