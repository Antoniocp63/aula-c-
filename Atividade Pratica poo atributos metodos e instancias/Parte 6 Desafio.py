def pode_ser_alugado(self):
    return self.disponivel

if veiculo1.pode_ser_alugado():
    print("Veículo disponível para aluguel.")
else:
    print("Veículo indisponível.")
