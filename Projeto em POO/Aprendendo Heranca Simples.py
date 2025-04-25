class Veiculo:
    def __init__(self, cor, placa, numeros_rodas,):
        self.cor = cor
        self.placa = placa
        self.numeros_rodas = numeros_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):

    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):

    def __init__(self, cor, placa, numeros_rodas, carregado):
        super().__init__(cor, placa, numeros_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao'} Estou carregado")


moto = Motocicleta('preta', 'abc-1213', 2)

moto.ligar_motor()

carro = Carro('branco', "ren-8468", 4)
carro.ligar_motor()

caminhao = Caminhao("Cinza", "gtd-3895", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
