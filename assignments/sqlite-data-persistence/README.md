# 📘 Atividade: Primeiro Banco de Dados com SQLite

## 🎯 Objetivo

Crie um catálogo de livros em Python que armazena os dados em um banco SQLite, mantendo-os disponíveis mesmo depois que o programa for encerrado. Você praticará tabelas, comandos SQL básicos e operações de inserção, consulta e exclusão usando o módulo `sqlite3` da biblioteca padrão.

## 📝 Tarefas

### 🛠️ Crie o banco e a tabela de livros

#### Descrição
Complete a função de inicialização para criar o arquivo `books.db` e a tabela `books` na primeira execução. O programa deve poder iniciar novamente sem falhar se a tabela já existir.

#### Requisitos
O programa concluído deve:

- Criar uma tabela chamada `books` com as colunas `id`, `title` e `author`.
- Configurar `id` como chave primária gerada automaticamente.
- Exigir valores para título e autor.
- Usar `CREATE TABLE IF NOT EXISTS` para permitir inicializações repetidas.

### 🛠️ Adicione e consulte livros

#### Descrição
Implemente as funções para salvar um livro e listar os livros cadastrados. Use os dados solicitados pelo menu do programa e mostre cada registro com seu identificador, título e autor.

#### Requisitos
O programa concluído deve:

- Inserir título e autor na tabela usando parâmetros SQL, sem montar a consulta por concatenação de texto.
- Consultar os livros em ordem crescente de identificador.
- Exibir uma mensagem adequada quando ainda não houver livros cadastrados.
- Permitir adicionar e listar vários livros na mesma execução.

### 🛠️ Remova livros e confira a persistência

#### Descrição
Complete a função de exclusão e teste o catálogo em mais de uma execução. Os registros devem continuar no banco depois que o programa for encerrado.

#### Requisitos
O programa concluído deve:

- Remover um livro pelo identificador informado usando parâmetros SQL.
- Informar quando o identificador não corresponder a nenhum livro.
- Manter os demais registros após uma exclusão.
- Permitir confirmar a persistência encerrando e executando novamente `python starter-code.py`.
