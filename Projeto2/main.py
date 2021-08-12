import pickle

from Pokemon import *
from Pessoa import *


def escolher_pokemon_inicial(player):
    print('Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada'.format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas')
    print('1 -', pikachu)
    print('2 -', charmander)
    print('3', squirtle)

    while True:
        escolha = input('Escolha um Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')


def salvar_jogo (player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('Jogo salvo com sucesso!')
    except Exception as error:
        print('Erro ao salvar o jogo')
        print(error)

def carregar_jogo ():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso!")
            return player
    except Exception as error:
        print('Save não encontrado')


if __name__ == '__main__':
    print('--------------------------------')
    print('Bem-vindo ao Game Pokemon RPG de terminal')
    print('-----------------------------------------')

    player = carregar_jogo()

    if not player:
        nome = input('Olá, qual seu nome? ')
        player = Player(nome)
        print('Olá {}, esse é um mundo habitado por Pokemons,'
              ' a partir de agora sua missão é se tornar um mestre dos Pokemons!'.format(player))
        print('Capture o máximo de Pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
           print('Já vi que você tem alguns pokemons. Vamos ver?')
           player.mostrar_pokemons()
        else:
            print('Você não tem nenhum Pokemon, vamos escolher um? ')
            escolher_pokemon_inicial(player)

        print('Pronto, agora você já possui um Pokemon, enfrente seu primeiro inimigo.... Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print('-------------------------------------')
        print('O que deseja fazer?')
        print('0 - Explorar o mundo?')
        print('1 - Batalhar com um inimigo?')
        print('2 - Mostrar sua pokeagenda?')
        print('3 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '1':
              inimigo_aleatorio = Inimigo()
              player.batalhar(inimigo_aleatorio)
              salvar_jogo(player)
        elif escolha == '2':
             player.mostrar_pokemons()
        elif escolha == '3':
            print('Saindo.... Até mais :D')
            break
        else:
            print('Escolha inválida')






