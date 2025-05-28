# Gerenciador de Clientes

Um CRUD de clientes em Python utilizando SQLite3, com validações básicas de dados.

## Funcionalidades

- Criar tabela de clientes (nome, e-mail)
- Inserir cliente com validação de nome e e-mail
- Listar todos os clientes
- Atualizar dados de um cliente
- Remover cliente

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/gerenciador_clientes.git
   cd gerenciador_clientes
(Opcional) crie e ative um ambiente virtual:


python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale dependências (não há pacotes externos; só o Python padrão).

Rode o programa:


python main.py
Estrutura de arquivos
db.py – conexões e criação da tabela SQLite

cliente.py – lógica de CRUD e validações

main.py – menu interativo no terminal

.gitignore recomendado

__pycache__/
*.pyc
clientes.db
venv/
Contribuições
Pull requests são bem-vindos!
Abra uma issue para sugerir melhorias.

