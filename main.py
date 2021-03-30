import random


class Card:
    def __init__(self, card_type, card_value):
        self.card_type = card_type
        self.card_value = card_value


def game():
    print('** Bem vindo ao jogo Blackjack! **')
    init = input('Deseja iniciar o jogo? Digite S para Sim, e N para Não iniciar, e sair do jogo: ')

    if init.strip().upper() == 'S':
        deck = get_deck()
        player_one = 0
        player_one_cards = []
        player_two = 0
        player_two_cards = []
        counter = 0

        while init == 'S':
            counter += 1

            if counter == 1:
                secret_card = get_random_card(deck)
                player_one_cards.append(secret_card.card_value)
                player_two_cards.append(secret_card.card_value)

                print('Na primeira rodada é distribuída uma carta secreta! A carta tem o mesmo valor para ambos e '
                      'será revelada no final!')
                player_one += get_card_value(secret_card, 1)
                player_two += player_one
                print(f'\nRodada {counter} - Você = X')
                print(f'Rodada {counter} - Mesa = X\n')

                init = input(
                    'Deseja jogar mais uma rodada, ou quer parar agora? Digite S para Sim, e N para Não: ')
            else:
                player_one_card = get_random_card(deck)
                player_one_cards.append(player_one_card.card_value)
                player_two_card = get_random_card(deck)
                player_two_cards.append(player_two_card.card_value)

                player_one += get_card_value(player_one_card, 0)
                player_two += get_card_value(player_two_card, 1)
                print(f'\nRodada {counter} - Você = {player_one_card.card_value}\n')
                #print(f'Rodada {counter} - Mesa = {player_two_card.card_value}\n')

                if player_two == 21:
                    print('Você perdeu! A mesa fez 21 pontos e ganhou o jogo!')
                    break
                elif player_two > 21:
                    print(f'Parabéns, você ganhou! A mesa passou dos 21 pontos e fez {player_one} pontos.')
                    break

                if player_one == 21:
                    print('Parabéns, você ganhou! Você fez 21 pontos e ganhou o jogo!')
                    break
                elif player_one > 21:
                    print(f'Você perdeu! Você passou dos 21 pontos e fez {player_one} pontos.')
                    break

                init = input(
                    'Nem você nem a mesa completaram os 21 pontos! Deseja jogar mais uma rodada, ou quer parar '
                    'agora? Digite S para Sim, e N para Não: ')

            if init.strip().upper() == 'N':
                if player_one > player_two:
                    print(
                        f'\nParabéns, você ganhou! Você fez {player_one} pontos, '
                        f'enquanto a mesa fez {player_two} pontos.')
                elif player_one == player_two:
                    print(f'\nNem ganhou nem perdeu! Você e a mesa empataram com {player_one} pontos!')
                else:
                    print(f'\nVocê perdeu! Você fez {player_one} pontos, enquanto a mesa fez {player_two} pontos.')

        print(f'Cartas da Mesa: {player_two_cards} = {player_two}')
        print(f'Suas cartas: {player_one_cards} = {player_one}')
    else:
        print('Sem problemas, volte quando quiser!')


def get_random_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def get_card_value(card, type):
    card_value = card.card_value
    if card_value in ['J', 'Q', 'K']:
        return 10
    elif card_value == 'A':
        if type == 0:
            return int(input('Você tirou um Ás! É necessário que escolha um valor para essa carta, sendo 1 ou 11. '
                             'Qual valor escolhe? '))
        else:
            return random.choice([1, 11])
    else:
        return card_value


def get_deck():
    card_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    card_types = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    deck = []

    for card_type in card_types:
        for card_value in card_values:
            deck.append(Card(card_type, card_value))
    return deck


game()
