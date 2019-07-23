import datetime 

#Estou tentando retornar a idade com base na data de nascimento usando o datetime mas ainda não consegui, estarei enviando assim mesmo e caso consiga com datetime antes das 23:59 eu envio novamente. 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return self.nome
        return self.idade

class Animal:
    def __init__(self,nome_pet ,dono, data_nascimento):
        self.nome_pet = nome_pet
        self.dono = dono
        self.data_nascimento = data_nascimento

    def __str__(self):
        return self.nome_pet
        return self.dono
        return self.data_nascimento


pessoa = Pessoa('Fabio', '25')
animal = Animal('Poty','Fabio','05/08/2004')

print(f'O nome da pessoa é {pessoa.nome}, sua idade é {pessoa.idade}')
print(f'O nome do pet é {animal.nome_pet}, seu dono é {animal.dono}, e sua data de nascimento é {animal.data_nascimento}')