from cliente import Cliente
from quarto import Quarto
from reserva import Reserva

class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_clientes(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        for c in self.clientes:
            print(c)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def listar_quartos(self):
        for q in self.quartos:
            print(q)

    def criar_reserva(self, cliente_id, numero_quarto, checkin, checkout):
        cliente = next((c for c in self.clientes if c.id_unico == cliente_id), None)
        quarto = next((q for q in self.quartos if q.numero == numero_quarto), None)

        if not cliente:
            print("Cliente não encontrado!")
            return
        
        if not quarto or not quarto.disponivel:
            print("Quarto indisponível!")
            return
        
        reserva = Reserva(cliente, quarto, checkin, checkout)
        self.reservas.append(reserva)
        quarto.disponivel = False

        print("Reserva criada com sucesso!")

    def listar_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva registrada.")
        for r in self.reservas:
            print(r)

    def cancelar_reserva(self, numero_quarto):
        for reserva in self.reservas:
            if reserva.quarto.numero == numero_quarto and reserva.status == "Ativa":
                reserva.status = "Cancelada"
                reserva.quarto.disponivel = True
                print("Reserva cancelada!")
                return
        print("Reserva não encontrada.")
