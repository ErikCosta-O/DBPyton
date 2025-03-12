# Projeto Banco de Dados com Python

## Descrição
O arquivo `sgcontatos.py` é um script em Python que gerencia um banco de dados SQLite para armazenar informações de contatos. Ele permite ao usuário realizar operações básicas de CRUD (Create, Read, Update, Delete) em uma tabela de contatos.

## Funcionalidades
- **Criação do Banco de Dados**: O script verifica se o arquivo do banco de dados `ex: C:\\Users\\SeuUsuario\\Documents\\DBPyton\\contatos.db)` já existe. Se existir, pergunta ao usuário se deseja excluí-lo e criar um novo.
- **Criação da Tabela**: Cria a tabela `tb_contatos` no banco de dados, se ela não existir.
- **Inserção de Registros**: Permite ao usuário inserir novos contatos no banco de dados.
- **Deletar Registros**: Permite ao usuário deletar contatos existentes no banco de dados.
- **Atualizar Registros**: Permite ao usuário atualizar informações de contatos existentes.
- **Consulta de Registros**: Permite ao usuário consultar todos os contatos ou buscar contatos pelo nome.

## Como Usar
1. Execute o script `sgcontatos.py`.
2. Digite o caminho completo do diretório onde o banco de dados será armazenado (ex: `C:\\Users\\SeuUsuario\\Documents\\DBPyton`).
3. Digite o nome do banco de dados (ex: `contatos.db`).
4. Siga as instruções no menu principal para realizar as operações desejadas.

## Autor
**Erik Costa Oliveira**  
**Data**: 11/03/2025  
**Versão**: 1.0