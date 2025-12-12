class Cliente:
    def __init__(self, nome, telefone, email, id_unico):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_unico = id_unico

    def __str__(self):
        return f"{self.id_unico} - {self.nome} | tel: {self.telefone} | Email: {self.email}"
    

