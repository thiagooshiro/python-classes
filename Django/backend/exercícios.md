
# 1 - Criar um app "escolas" para gerenciar o cadastro de escolas no sistema.

O comando para isso seria: "python manage.py startapp escolas"

### Passo a passo:

1. **Criar o Model das Escolas:**
   - No arquivo `models.py` do seu novo app, defina a classe do modelo (`Model`) e as informações necessárias para o registro de uma escola no banco de dados.

2. **Criar as Views:**
   - No arquivo `views.py` do seu app "escolas", determine as classes que irão processar as requisições. É importante que seja possível:
     - Cadastrar uma nova escola;
     - Ver as informações de uma escola específica;
     - Editar as informações de uma escola cadastrada;
     - Deletar uma escola cadastrada do registro.

3. **Criar as Rotas:**
   - No arquivo `urls.py` do seu app "escolas", estabeleça quais endpoints acessam quais views.

4. **Consultas:**
   - Em caso de dúvidas, consulte os exemplos correspondentes no app "students".

---

# 2 - Criar um app "professores" para gerenciar o cadastro de professores.

### Passo a passo:

1. **Criar o Model dos Professores:**
   - No arquivo `models.py` do app "professores", defina a classe do modelo (`Model`) e as informações necessárias para o registro de um professor no banco de dados.

2. **Criar as Views:**
   - No arquivo `views.py` do seu app "professores", determine as classes que irão processar as requisições. É importante que seja possível:
     - Cadastrar um novo professor;
     - Ver as informações de um professor específico;
     - Editar as informações de um professor cadastrado;
     - Deletar um professor cadastrado do registro.

3. **Criar as Rotas:**
   - No arquivo `urls.py` do seu app "professores", estabeleça quais endpoints acessam quais views.

---
