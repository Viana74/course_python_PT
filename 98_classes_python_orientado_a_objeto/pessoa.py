from datetime import datetime

class Pessoa: #Conveciona a primeira letra maiuscula
    ano_atual = int(datetime.strftime(datetime.now(),'%Y')) #variavel (atributo) da classe. Esta disponível para todos os objetos (instancias) inclusive a propria classe
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        variavel = 'Valor'
        print(variavel)

    #def falar(self):
    #   print('Pessoa está falando')

# metodo é uma função pertencente a uma classe
#self é obrigatorio e não deve ser passado e é refente a p1 e p2

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} ja esta falando.')
            return

        print(f'{self.nome} começou a falar sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao esta falando.')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} está falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade