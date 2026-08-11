# Projeto Final - API de Biblioteca

## Tema

Biblioteca.

O sistema permite cadastrar autores e livros, além de consultar, alterar,
excluir e pesquisar os dados.

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- SQL
- REST API

## Banco de dados

O projeto possui duas tabelas.

### Tabela autores

Possui:

- id
- nome

### Tabela livros

Possui:

- id
- titulo
- ano
- autor_id

O campo autor_id é uma chave estrangeira que relaciona os livros com os autores.

Um autor pode possuir vários livros.

## Relacionamento

A relação entre as tabelas é:

autores
    |
    |
    v
livros

O campo livros.autor_id aponta para autores.id.

Também foi utilizado ON DELETE CASCADE. Assim, quando um autor é excluído,
os livros relacionados a ele também são excluídos.

## Como executar

Primeiro instale o Flask:

    pip install flask

Depois execute o arquivo:

    python app.py

A API será iniciada no endereço:

    http://127.0.0.1:5000

O banco de dados biblioteca.db será criado automaticamente.

## Rotas dos autores

### Listar autores

GET /autores

### Criar autor

POST /autores

Exemplo:

{
    "nome": "Machado de Assis"
}

### Alterar autor

PUT /autores/<id>

### Excluir autor

DELETE /autores/<id>

## Rotas dos livros

### Listar livros

GET /livros

### Criar livro

POST /livros

Exemplo:

{
    "titulo": "Dom Casmurro",
    "ano": 1899,
    "autor_id": 1
}

### Alterar livro

PUT /livros/<id>

### Excluir livro

DELETE /livros/<id>

## JOIN

A rota:

GET /livros/detalhes

utiliza INNER JOIN para mostrar os dados do livro junto com o nome do autor.

## Filtros

### Filtro por caminho

GET /autores/<id>/livros

Mostra somente os livros de determinado autor.

### Busca por query string

GET /livros/buscar?titulo=Dom

Procura livros pelo título utilizando LIKE.

## Códigos HTTP

O projeto utiliza:

- 200 para operações realizadas com sucesso
- 201 quando um registro é criado
- 400 quando os dados enviados são inválidos
- 404 quando o registro não existe

## Testes

O arquivo testes.http contém exemplos para testar as rotas da API.

Os testes incluem:

- criação de autores;
- consulta de autores;
- alteração de autores;
- exclusão de autores;
- criação de livros;
- consulta de livros;
- alteração de livros;
- exclusão de livros;
- JOIN;
- filtro por autor;
- busca utilizando LIKE;
- testes de registros inexistentes;
- testes de dados inválidos.