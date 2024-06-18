
# Sistema de Matrículas de Hogwarts

O Sistema de Matrículas de Hogwarts é uma aplicação web desenvolvida para gerenciar os alunos da Escola de Magia e Bruxaria de Hogwarts. Com este sistema, é possível adicionar, visualizar, editar e deletar registros de alunos, além de visualizar detalhes específicos como casa, ano e especialidades mágicas de cada aluno.

## Tecnologias Utilizadas

- **Front-end**: HTML, CSS
- **Back-end**: Python, Flask
- **Database**: SQLite
- **Outras**: SQLAlchemy para ORM

## Pré-requisitos

Antes de iniciar, você precisará ter instalado em sua máquina as seguintes ferramentas:
- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- Um editor de código, eu indico [VSCode](https://code.visualstudio.com/)


### Execução

Clone o repositório para sua máquina local usando:

```bash
git clone https://seu-repositorio.com/projeto-hogwarts.git
cd projeto-hogwarts
```

### Configuração da imagem docker

**Caso não tenha o docker**

Download do Docker Desktop [Docker](https://www.docker.com/)

**Depois de instalado rode os seguintes comandos no terminal**

```bash
docker-compose up --build -d
```


**Depois da build da imagem rode o seguinte comando no terminal**

```bash
docker-compose logs web
```

Segurando a tecla Ctrl no seu teclado clique em "Running on http://127.0.0.1:5000"

Pront, a aplicação estará rodando

### Parando a aplicação

Para parar a aplicação digite o seguinte comando no terminal

```bash
docker-compose down
```


## Funcionalidades

- **Cadastrar Alunos**: Acesse `/cadastrar` para abrir o formulário de cadastro de alunos.
- **Listar Alunos**: Todos os alunos cadastrados podem ser vistos em `/alunos`, onde também é possível editar ou deletar um aluno.
- **Editar Alunos**: Clique em "Editar" ao lado de qualquer aluno na lista para modificar seus dados.
- **Deletar Alunos**: Clique em "Delete" para remover um aluno do sistema.

## Estrutura de Diretórios

```
|-- /app
|   |-- __init__.py
|   |-- models.py
|   |-- routes.py
|   |-- /templates
|   |   |-- home.html
|   |   |-- alunos.html
|   |   |-- cadastrar.html
|   |   |-- edit_aluno.html
|   |-- /static
|       |-- /images
|       |-- /css
|           |-- style.css
|-- run.py
|-- .dockerignore
|-- docker-compose.yml
|-- Dockerfile
```

## Contribuições

Contribuições são o que fazem a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

E não se esqueça "Mal-feito feito!"

## Licença

Não tem licença somos pobres camponeses
