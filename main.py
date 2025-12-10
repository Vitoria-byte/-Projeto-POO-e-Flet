from gerenciador import GerenciadorDeReservas
from cliente import Cliente
from quarto import Quarto

def menu():
    system = GerenciadorDeReservas()

    # Criar alguns quartos iniciais
    system.adicionar_quarto(Quarto(101, "single", 180))
    system.adicionar_quarto(Quarto(102, "double", 250))
    system.adicionar_quarto(Quarto(201, "suite", 400))

    while True:
        print("\n===== SISTEMA DE RESERVAS DO HOTEL =====")
        print("1 - Adicionar Cliente")
        print("2 - Lista Clientes")
        print("3 - Lista Quartos")
        print("4 - Criar Reserva")
        print("5 - Lista Reservas")
        print("6 - Cancelar Reserva")
        print("0 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            id_unico = input("ID único: ")
            system.adicionar_clientes(Cliente(nome, telefone, email, id_unico))

        elif op == "2":
            system.listar_clientes()

        elif op == "3":
            system.listar_quartos()

        elif op == "4": 
            cliente_id = input("ID do cliente: ")
            quarto = int(input("Número do quarto: "))
            checkin = input("Data de check-in: ")
            checkout = input("Data de check-out ")
            system.criar_reserva(cliente_id, quarto, checkin, checkout)

        elif op == "5":
            system.listar_reservas()

        elif op == "6":
            quarto = int(input("Número do quarto da reserva a cancelar: "))
            system.cancelar_reserva(quarto)

        elif op == "0":
            break

        else:
            print("Opção inválida!")

menu()

    

     