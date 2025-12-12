class Quarto:
    def __init__(self, numero, tipo, preco, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} ({self.tipo}) - R$ {self.preco}/dia - {status}"

        
