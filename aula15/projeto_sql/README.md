🏫 Sistema de Cadastro de Escolas e Alunos (Python + SQLite)

Este é um projeto simples de terminal feito com Python puro e SQLite que simula o cadastro e a consulta de escolas e alunos.

Ele serve como base para a prática dos conceitos de:

    CRUD (Create, Read, Update, Delete)

    Organização de código com módulos e pastas

    Uso de banco de dados relacional com SQLite

    Interação com terminal

✅ Funcionalidades implementadas

    Criar escola

    Criar aluno

    Listar todas as escolas

    Listar todos os alunos

    Menu de navegação no terminal

📌 Estrutura de pastas

.
├── db.py                  # Criação das tabelas no SQLite
├── main.py                # Interface de terminal (menu)
├── services/
│   ├── alunos.py          # Funções de criação e listagem de alunos
│   └── escolas.py         # Funções de criação e listagem de escolas

🧩 Requisitos de implementação (para os alunos)

Você deve complementar o sistema com as seguintes funcionalidades:

    Read detalhado (por ID):

        Buscar uma escola pelo seu ID

        Buscar um aluno pelo seu ID

    Update:

        Atualizar dados de uma escola existente

        Atualizar dados de um aluno existente

    Delete:

        Deletar uma escola pelo ID

        Deletar um aluno pelo ID

🚀 Como rodar

    Certifique-se de ter Python instalado (versão 3.7+ recomendada)

    Clone este repositório ou baixe os arquivos

    No terminal, vá até a pasta do projeto

    Execute o programa:

python main.py

✍️ Dica para implementação

Para manter a organização do projeto, siga o padrão já existente:

    As funções de manipulação do banco devem ficar nos arquivos services/alunos.py e services/escolas.py.

    A lógica de entrada e interação com o usuário deve ficar no main.py.