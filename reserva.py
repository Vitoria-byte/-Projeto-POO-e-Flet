class Reserva: 
    def __init__(self, cliente, quarto, checkin, checkout, status = "Ativa"):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = status
    
    def __str__(self):
        return (f"Reserva - Cliente: {self.cliente.nome}, Quarto: {self.quarto.numero},"
                f"Check-in: {self.checkin}, Check-out: {self.checkout}, Status: {self.status}")
