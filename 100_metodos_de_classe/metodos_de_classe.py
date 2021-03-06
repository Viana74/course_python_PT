class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Se o método está relacionado a classe então ele não é específico de cad instancia
    # Neste caso, este método está disponível apenas para essa classe e não para outras instancias
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

p1 = Pessoa('Luiz',32)
print(p1.idade)
p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento('Luiz', 1990)
print(f'{p1.nome} tem {p1.idade} anos de idade.')