class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzina(self):
        print("Plim Plim...")
        
    def parar(self):
        print("Bicicleta parada")
        
    def correr(self):
        print("Correndo Vrummm")
        
    def get_cor(self):
        return self.cor
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("Preta", "BMX", 2005, 150)

b1.correr() # Bucicleta.correr(b1) e a mesma coisa
b1.buzina()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1.cor)  # print(b1.get_cor()) mesma coisa
print(b1)