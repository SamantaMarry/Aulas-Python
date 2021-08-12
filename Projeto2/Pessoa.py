import random

from Pokemon import *


NOMES = [ 'Ash', 'Misty', 'Brock', 'Jessie', 'Gary', 'James', 'Professor Carvalho',
          'Iris', 'Enfermeira Joy', 'Max', 'Lilie', 'Bonnie',

]

POKEMONS = [ PokemonFogo('Charmander'),
             PokemonFogo('Arcanine'),
             PokemonFogo('Charmeleon'),
             PokemonEletrico('Pikachu'),
             PokemonEletrico('Raichu'),
             PokemonAgua('Squirtle'),
             PokemonAgua('Magicarp'),
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome

        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Pokemons de {}'.format(self))
            for index, pokemon in enumerate(self.pokemons):
                print('{} - {}:'.format(index, pokemon))

        else:
            print('{} não possui nenhum pokemon'.format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_selecionado = random.choice(self.pokemons)
            print('{} selecionou {}'.format(self, pokemon_selecionado))
            return pokemon_selecionado
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon a ser selecionado!!')

    def mostrar_dinheiro(self):
        print('Você possui ${} em sua conta.'.format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('Você ganhou ${}'.format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print('{} iniciou uma batalha com {}'.format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitória = pokemon.atacar(pokemon_inimigo)
                if vitória:
                    print('{} ganhou a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha'.format(pessoa))
                    break
        else:
            print('Não foi possível realizar a batalha')

class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}!'.format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                selecione = input('Selecione seu Pokemon: ')
                try:
                    selecione = int(selecione)
                    pokemon_selecionado = self.pokemons[selecione]
                    print('{} eu escolho você!!'.format(pokemon_selecionado))
                    return pokemon_selecionado
                except:
                    print('Inválido')
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon a ser selecionado!!')

    def explorar(self):
        if random.random() <= 0.3:
           pokemon = random.choice(POKEMONS)
           print('Um pokemon selvagem apareceu: {}'.format(pokemon))

           escolha = input('Deseja capturar o pokemon encontrado? (s/n): ')
           if escolha == 's':
               if random.random() >= 0.5:
                   self.capturar(pokemon)
               else:
                   print('{} fugiu!! Que pena!!'.format(pokemon))
           else:
                print('OK, boa viagem')
        else:
            print('Sua exploração não deu em nada!')

class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)



