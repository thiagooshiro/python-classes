### Guia Projeto CRUD em DJANGO
CRUD significa "Create, Retrieve, Update and Delete".
Diz respeito às funcionalidades de:
Recuperar dados de um banco de dados, seja de todos os dados ou dados específcos.
Por exemplo, todos os estudantes da escola, ou os detalhes de um estudante em específico.
Criar novas informações - no nosso caso a possibilidade de registrar novos estudantes.
Atualizar informações - alterar registros já existentes.
Deletar informações - remover registros já existentes.

### Estrutura do projeto em Django... 

O Django lida com isso de uma forma muito elegante. 
Nós temos um app principal, nesse caso chamado de "schoolmanager".
Nos quais as configurações de rotas e o gerenciamento de acesso e configurações é realizado.
E cada "conjunto" de informações ou conjunto que precisamos criar o CRUD pode ser um app diferente,
no nosso exemplo, temos o app "students" que lida com o CRUD dos estudantes:
- Cadastro de novos estudantes;
- Ver todos os estudantes cadastrados ou retornar um cadastro específico
- Atualizar um cadastro
- Deletar um cadastro;

### Ferramentas do Django: 
Para isso o Django utiliza o que chamamos de "views", no arquivos views.py do app students teremos a implementaçãod a lógica de cada um das funcionalidades listadas acima.

Essas views serão acessadas via um arquivo "urls.py" no app students, que também terá uma referência no app principal "schoolmanager";


### Para fins de simplicidade, usaremos o banco de dados SQlite que é o padrão do Django.
Abaixo vocês encontrarão um passo a passo para a criação dos comandos utilziados para criar a base desse projeto.

### O arquivo "requirements.txt"
Normalmente, e é o caso desse projeto, sempre temos um arquivo .gitignore no quais arquivos sensíveis serão ignorados caso esse projeto seja enviado para um repositório, isso é necessário para evitar que informações sensíveis sejam enviadas para o repositório, ou para que arquivos muito grandes, como bibliotecas e frameworks tbm. 

No arquivo requirements.txt teremos todas as bibliotecas e frameworks utilizados pelo projeto, é comum se refereir a esses elementos como "dependências" do projeto.

### Passo 1: Criação do Ambiente Virtual

1. **Criar o Ambiente Virtual:**
   ```bash
   python -m venv .venv
   ```

2. **Ativar o Ambiente Virtual:**
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No MacOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

### Passo 2: Instalar o Django

1. **Instalar o Django:**
   ```bash
   pip install django
   ```

### Passo 3: Criar o Projeto Django

1. **Criar o Projeto Django:**
   ```bash
   django-admin startproject schoolmanager
   ```

2. **Navegar para o Diretório do Projeto:**
   ```bash
   cd schoolmanager
   ```

### Passo 4: Criar o Aplicativo "students"

1. **Criar o Aplicativo:**
   ```bash
   python manage.py startapp students
   ```

### Passo 5: Configurar o Projeto Django

1. **Adicionar o Aplicativo `students` ao `INSTALLED_APPS` no `settings.py`:**
   - Abra o arquivo `school/settings.py` e adicione `'students'` à lista `INSTALLED_APPS`.

### Passo 6: Criar Migrações e Aplicá-las

1. **Criar Migrações:**
   ```bash
   python manage.py makemigrations
   ```

2. **Aplicar Migrações:**
   ```bash
   python manage.py migrate
   ```

### Passo 7: Iniciar o Servidor de Desenvolvimento

1. **Iniciar o Servidor:**
   ```bash
   python manage.py runserver
   ```

Seguindo esses comandos, você terá configurado um ambiente virtual, instalado o Django, criado um projeto Django chamado "schoolmanager", criado um aplicativo chamado "students" e iniciado o servidor de desenvolvimento. A partir daí, você pode continuar com a implementação específica do modelo, views, templates e URLs conforme necessário para sua aplicação.