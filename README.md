
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

## Configuração do Projeto

### Instalação

Clone o repositório para sua máquina local usando:

```bash
git clone https://seu-repositorio.com/projeto-hogwarts.git
cd projeto-hogwarts
```

Instale as dependências:

```bash
pip install flask sqlalchemy
```
**no MacOs**

```bash
pip3 install flask sqlalchemy
```

### Configuração do Banco de Dados

Inicialize o banco de dados com o seguinte comando:

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Execução

Para rodar o servidor, execute:

```bash
python run.py
```

Isso iniciará o servidor local no endereço `http://127.0.0.1:5000/`. Acesse o URL em um navegador de sua escolha.

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
```

## Contribuições

Contribuições são o que fazem a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

E não se esqueça "Mal-feito feito!"

## Licença

Não tem licença somos pobres camponeses
