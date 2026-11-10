# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para administrar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com Pydantic, respostas de erro e operações CRUD; os dados ficarão em memória durante a execução.

## 📝 Tarefas

### 🛠️ Configure a aplicação e consulte livros

#### Descrição
Instale FastAPI e Uvicorn, complete as rotas de consulta no código inicial e execute a aplicação. Use a documentação interativa do FastAPI em `/docs` para testar os endpoints.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI executável com `python starter-code.py`.
- Implementar `GET /books` para retornar a lista de livros.
- Implementar `GET /books/{book_id}` para retornar um livro pelo identificador.
- Responder com erro HTTP 404 quando o identificador solicitado não existir.

### 🛠️ Crie livros com validação

#### Descrição
Defina um modelo Pydantic para os dados recebidos e implemente a criação de livros no catálogo. Cada livro deve receber um identificador único gerado pela aplicação.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` recebendo título e autor no corpo da requisição.
- Validar o corpo da requisição usando um modelo Pydantic e rejeitar campos obrigatórios ausentes.
- Gerar um identificador para o novo livro e adicioná-lo ao catálogo em memória.
- Retornar o livro criado com status HTTP 201.

### 🛠️ Atualize e remova livros

#### Descrição
Complete as operações de atualização e remoção, mantendo as respostas consistentes quando um livro não for encontrado.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar título e autor do livro informado.
- Implementar `DELETE /books/{book_id}` para remover e retornar o livro removido.
- Responder com erro HTTP 404 ao tentar atualizar ou remover um identificador inexistente.
- Permitir testar todas as rotas pela documentação interativa em `/docs`.
