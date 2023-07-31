import random

#classes
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Player:
    def __init__(self, turns, cards):
        self.turns = turns
        self.cards = cards

#objects
user = Player(0, [])
dealer = Player(0, [])
colors = ['heart', 'diamonds', 'spades', 'clubs']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace']
deck = [Card(value, color) for value in values for color in colors]

#functions
def draw(role):
    rand_card = (random.choice(deck))
    role.cards.append(rand_card)
    
    deck.remove(rand_card)


def card_sum_user(role):
    global sum_val_user
    val_list_user = []
    for i in role.cards:
        if i.value == 'king' or i.value == 'queen' or i.value == 'jack':
            val_list_user.append(10)
        elif i.value == 'ace':
            val_list_user.append(11)
        else:
            val_list_user.append(int(i.value))
    sum_val_user = sum(val_list_user)
    for i in val_list_user:
        val_list_user.remove(i)

def card_sum_dealer(role):
    global sum_val_dealer
    val_list_dealer = []
    for i in role.cards:
        if i.value == 'king' or i.value == 'queen' or i.value == 'jack':
            val_list_dealer.append(10)
        elif i.value == 'ace':
            val_list_dealer.append(11)
        else:
            val_list_dealer.append(int(i.value))
    sum_val_dealer = sum(val_list_dealer)
    for i in val_list_dealer:
        val_list_dealer.remove(i)
        
#initial drawing of cards
while user.turns < 2 and dealer.turns < 2:
    draw(user)
    draw(dealer)
    user.turns += 1
    dealer.turns += 1

#dealer third draw
card_sum_dealer(dealer)
while sum_val_dealer < 16:
    draw(dealer)
    card_sum_dealer(dealer)

#deal or stand choice
while True:
    card_sum_user(user)
    if sum_val_user > 21:
        break
    deal_choice = input("the sum total of your cards is " + str(sum_val_user) + " do you wish to [D]eal or [S]tand? ")
    if deal_choice == "d":
        draw(user)
    elif deal_choice == "s":
        break
    else:
        print("invalid input")

#outcomes

if sum_val_user >= 22 and sum_val_dealer < 22:
    print("you lost, "+ "user card sum: " + str(sum_val_user) + " dealer card sum: "+ str(sum_val_dealer))
if sum_val_user >= 22 and sum_val_dealer >= 22:
    print("you lost, "+ "user card sum: " + str(sum_val_user) + " dealer card sum: "+ str(sum_val_dealer))
if sum_val_user < 22 and sum_val_dealer < 22 and sum_val_user < sum_val_dealer:
    print("you lost, "+ "user card sum: " + str(sum_val_user) + " dealer card sum: "+ str(sum_val_dealer))   
if sum_val_user < 22 and sum_val_dealer < 22 and sum_val_user > sum_val_dealer:
    print("you won, "+ "user card sum: " + str(sum_val_user) + " dealer card sum: "+ str(sum_val_dealer))
if sum_val_user < 22 and sum_val_dealer >= 22:
    print("you won, "+ "user card sum: " + str(sum_val_user) + " dealer card sum: "+ str(sum_val_dealer))
if sum_val_user == sum_val_dealer:
    print("stalemate, drawing cards...")
    draw(user), draw(dealer)
    while True:
        card_sum_dealer(dealer), card_sum_user(user)
        if sum_val_user > sum_val_dealer:
            print("you won, "+ "user card sum: " + str(sum_val_user)+ " dealer card sum: "+ str(sum_val_dealer))
            break
        elif sum_val_user == sum_val_dealer:
            continue
        else:
            print("you lost, "+ "user card sum: " + str(sum_val_user) + " dealer card sum: "+ str(sum_val_dealer))
            break
