# BLACK JACK GAME
import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five','Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cardDeck = []
        for i in rank:
            for j in suits:
                createdCard = Card(i,j)
                self.cardDeck.append(createdCard)

    def shuffle_deck(self):
        return random.shuffle(self.cardDeck)

    def deal_one_card(self):
        return self.cardDeck.pop(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.playerDeck = []

    def add_card(self,card):
        return self.playerDeck.append(card)

    def sum_of_cards(self):
        deck_sum = 0
        for i in self.playerDeck:
            deck_sum += i.value
        return deck_sum


class Chips:
    def __init__(self, balance = 100):
        self.balance = balance

    def place_bet(self, amount):
        self.balance -= amount
        return self.balance

    def win_bet(self, amount):
        self.balance += amount * 2
        return self.balance

class Dealer:
    def __init__(self):
        self.dealerDeck = []

    def add_card(self, card):
        return self.dealerDeck.append(card)

    def sum_of_cards(self):
        deck_sum = 0
        for i in self.dealerDeck:
            deck_sum += i.value
        return deck_sum

# GAME LOGIC

def player_busts():
    print(f"Player {player.name} has busted")

def player_wins():
    print(f"Player {player.name} has won!")

def dealer_busts():
    print("Dealer has busted")

def dealer_wins():
    print("Dealer has won!")



def display_player_cards():
    print(f"{player.name}'s Deck: ")
    for card in player.playerDeck:
        print(card)
    print(f"Total Value: {player.sum_of_cards()}")


def display_partial_dealer_cards():
    print("Dealer Card: ")
    print(dealer.dealerDeck[0])
    print(f"Value: {dealer.dealerDeck[0].value}")

def display_all_dealer_cards():
    print("Dealer Deck: ")
    for card in dealer.dealerDeck:
        print(card)
    print(f"Total value: {dealer.sum_of_cards()}")

def play_again():
    answer = input("Would you like to play again? Y or N: ")
    if answer.upper() == "Y" or answer.upper() == "YES":
        return True
    elif answer.upper() == "N" or answer.upper() == "NO":
        return False

# Game Setup

chips = Chips()
line = "____________________"

game_on = True
while game_on:
    # Deals Cards
    player = Player('Sam')
    dealer = Dealer()
    newDeck = Deck()
    newDeck.shuffle_deck()
    for i in range(2):
        dealer.dealerDeck.append(newDeck.deal_one_card())
    for j in range(2):
        player.playerDeck.append(newDeck.deal_one_card())
    display_partial_dealer_cards()
    print(line)
    display_player_cards()
    print(f"Available balance: ${chips.balance}")
    while True:
        bet = int(input("How much would you like to bet? $"))
        if bet <= chips.balance:
            chips.place_bet(bet)
            break
        else:
            print("Insufficient Funds Try Again!")

    # Ask for more cards
    continue_game = True
    while continue_game:
        choice = input("Would you like to add more cards Y or N: ")
        if choice.upper() == "Y":
            player.playerDeck.append(newDeck.deal_one_card())
            if player.sum_of_cards() > 21:
                display_all_dealer_cards()
                print(line)
                display_player_cards()
                player_busts()
                dealer_wins()
                if play_again():
                    game_on = True
                    continue_game = False
                else:
                    game_on = False
                    continue_game = False
            else:
                display_partial_dealer_cards()
                print(line)
                display_player_cards()

        elif choice.upper() == "N":
            while dealer.sum_of_cards() <= 21:
                dealer.dealerDeck.append(newDeck.deal_one_card())
                if dealer.sum_of_cards() > player.sum_of_cards() and dealer.sum_of_cards() <= 21:
                    display_all_dealer_cards()
                    print(line)
                    display_player_cards()
                    dealer_wins()
                    if play_again():
                        game_on = True
                        continue_game = False
                    else:
                        game_on = False
                        continue_game = False
                elif dealer.sum_of_cards() > 21:
                    display_all_dealer_cards()
                    print(line)
                    display_player_cards()
                    dealer_busts()
                    player_wins()
                    chips.win_bet(bet)
                    print(f"Player {player.name} has won ${bet*2}. Available balance: ${chips.balance}")
                    if play_again():
                        game_on = True
                        continue_game = False
                    else:
                        game_on = False
                        continue_game = False
