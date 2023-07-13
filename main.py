from random import choice

print('Hello, player!')
print("This is a card game. There will be five rounds")

CARD_NUMBER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["H", "D", "S", "C"]
rounds = 5
wins = 0
loses = 0


def check_game_level():
    while True:
        answer = input()
        if answer in ['1', '2', '3']:
            return answer
        else:
            print('The answer is invalid! Try again')


def check_color():
    while True:
        answer = input("Choose between red or black card: ").lower()
        if answer in ['red', 'black']:
            return answer
        else:
            print('The answer is invalid! Try again')


def check_suit():
    while True:
        answer = input("Choose the suit between H, D, S, C: ").upper()
        if answer in ['H', 'D', 'S', 'C']:
            return answer
        else:
            print('The answer is invalid! Try again')


def check_card():
    while True:
        suit_guess = input("Choose the suit between H, D, S, C: ").upper()
        number_guess = input("Choose the number between 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A: ").upper()
        if suit_guess in ['H', 'D', 'S', 'C'] and number_guess in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            answer = number_guess + ' ' + suit_guess
            return answer
        else:
            print('The answer is invalid! Try again')


print('Choose the game level:')
print("If you want to guess the card's color, press 1\nIf you want to guess the suit, press 2\nIf you want to guess the card, press 3")
game_level = check_game_level()
if game_level == '1':
    while rounds > 0:
        chosen_card_number = choice(CARD_NUMBER)
        chosen_card_suit = choice(CARD_SUIT)
        player_answer = check_color()
        if player_answer == 'red' and chosen_card_suit in ['H', 'D']:
            wins += 1
            rounds -= 1
            print('Congratulations! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)
        elif player_answer == 'black' and chosen_card_suit in ['S', 'C']:
            wins += 1
            rounds -= 1
            print('Congratulations! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)
        else:
            loses += 1
            rounds -= 1
            print('Incorrect! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)
elif game_level == '2':
    while rounds > 0:
        chosen_card_number = choice(CARD_NUMBER)
        chosen_card_suit = choice(CARD_SUIT)
        player_answer = check_suit()
        if player_answer == chosen_card_suit:
            wins += 1
            rounds -= 1
            print('Congratulations! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)
        else:
            loses += 1
            rounds -= 1
            print('Incorrect! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)
elif game_level == '3':
    while rounds > 0:
        chosen_card_number = choice(CARD_NUMBER)
        chosen_card_suit = choice(CARD_SUIT)
        chosen_card = chosen_card_number + ' ' + chosen_card_suit
        player_answer = check_card()
        if player_answer == chosen_card:
            wins += 1
            rounds -= 1
            print('Congratulations! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)
        else:
            loses += 1
            rounds -= 1
            print('Incorrect! The card was: ' + chosen_card_number + ' ' + chosen_card_suit)


print('Number of your wins: ', wins)
print('Number of your loses: ', loses)
