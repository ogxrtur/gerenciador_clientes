from db import criar_tabela
from cliente import adicionar_cliente, listar_clientes, atualizar_cliente, deletar_cliente

def menu():
    print("\n--- Gerenciador de Clientes ---")
    print("1. Adicionar cliente")
    print("2. Listar clientes")
    print("3. Atualizar cliente")
    print("4. Remover cliente")
    print("5. Sair")

def executar():
    criar_tabela()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionar_cliente(nome, email)
        
        elif opcao == "2":
            for c in listar_clientes():
                print(f"ID: {c[0]} | Nome {c[1]} | Email: {c[2]}")

        elif opcao == "3":
            id = int(input("ID do cliente a atualizar: "))
            nome = input("Novo Nome: ")
            email = input("Novo email: ")
            atualizar_cliente(id, nome, email)

        elif opcao == "4":
            id = int (input("ID do cliente a remover: "))
            deletar_cliente(id)

        elif opcao == "5":
           break

        else:
            print("Opção invalída!")


if __name__ == "__main":
    executar()
