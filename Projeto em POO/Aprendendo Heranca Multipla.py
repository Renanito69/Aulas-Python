class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelos, **kw):
        self.cor_pelos = cor_pelos
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass


gato = Gato(nro_patas=4, cor_pelos="Preto")
print(gato)

onitorrinco = Onitorrinco(nro_patas=2, cor_pelos="Vermelho", cor_bico="Laranja")
print(onitorrinco)