import time 
import random 


def create_deck(): 
    deck = []
    for i in ("Heart", "¨Spade", "Club", "Diamond"):
        for j in range(2,15):
            deck.append([j,i])
    random.shuffle(deck)
    return deck


def replay():
    re = input("Do you want to replay ? (Y/N)")
    re.lower()
    if re == "y":
        clearConsole()
        blackJack()
    else:
        print("Thank's for playing, Good bye.")
        return exit()


def deal(deck,hand):
    card = deck.pop()
    if card[0] == 11:
        card[0] = "Jack"
    if card[0] == 12:
        card[0] = "Queen"
    if card[0] == 13:
        card[0] = "King"
    if card[0] == 14:
        card[0] = "Ace"
    hand.append(card)
    return hand

def bet():
    f = open("bank.txt", "r")
    total_money = f.read()
    f.close()
    total_money = int(total_money)
    if total_money < 0:
        print("You don't have any money left, you can't bet")
        return exit()
    print("You have ", total_money,"$ on your account, how much do you want to bet ?")
    bet = int(input("réponse:"))
    while bet > total_money:
        print("Incorrect bet, you don't have enough money on your account, choose a valid bet...")
        bet = int(input("answer :"))
    if total_money < bet:
        print("Incorrect bet, you don't have enough money on your account, choose a valid bet...")
    f = open("bank.txt", "w")
    total_money = int(total_money) - bet
    f.write(str(total_money))
    f.close()
    clearConsole()
    return bet


def betUpdate(bet):
    f = open("bank.txt", "r")
    total_money = f.read()
    f.close()
    f = open("bank.txt", "w")
    total_money = int(int(total_money) + bet)
    f.write(str(total_money))
    f.close()
    return bet


def checkBlackJack(player_hand, dealer_hand,bet):
    if handValue(player_hand) == handValue(dealer_hand) and handValue(player_hand) == 21:
        print("Both of you and the dealer had a BLACKJACK, tied game..")
        replay()
    elif handValue(player_hand) == 21:
        print(" Congrats ! you got a BLACKJACK ! , you won ")
        betUpdate(bet)
        replay()
    elif handValue(dealer_hand) == 21:
        print(" Sorry, the dealer got a BLACKJACK, you loose...")
        replay()
    return 

def tirer(deck):
    card = deck.pop()
    if card[0] == 11:
        card[0] = "Jack"
    if card[0] == 12:
        card[0] = "Queen"
    if card[0] == 13:
        card[0] = "King"
    if card[0] == 14:
        card[0] = "Ace"
    return card


def clearConsole():
    print("Clear console :")
    for _ in range(15):
        print("\n")

def handValue(hand):
    valeur = 0
    for i in hand:
        if i[0] == "Jack" or i[0] == "Queen" or i[0] == "King":
            valeur += 10
        elif i[0] == "Ace":
            if valeur > 10:
                valeur += 1
            else:
                valeur += 11
        else:
            valeur += i[0]
    return valeur

def afficherhands(handplayer,handdealer):
    print("Here are the hands : \n")
    print("hand player : ", handplayer, "Valeur : ", handValue(handplayer))
    print("hand dealer : ", handdealer, "Valeur :", handValue(handdealer))


def finalScores(handplayer, handdealer, bet):
    afficherhands(handplayer,handdealer)
    if handValue(handplayer) > 21:
        print("your score exceeds 21 ,you lose...")
    elif handValue(handdealer) > 21:
        print("The dealer exceeds 21, you won !")
        betUpdate(bet*1.5)
    elif handValue(handplayer) == 21:
        print(" You got a BLACKJACK !, you won !")
        betUpdate(bet*1.5)
    elif handValue(handdealer) == 21:
        print("The dealer made a BLACKJACK, you lose...")
    elif handValue(handplayer) == handValue(handdealer) <= 21:
        print("both of you and the dealer had the same score, it's a tied game nobody won")
        betUpdate(bet)
    elif handValue(handplayer) > handValue(handdealer):
        print("Congratulations, you have a better score than the dealer, you won !")
        betUpdate(bet*1.5)
    elif handValue(handplayer) < handValue(handdealer):
        print("Too bad, the dealer got a better hand than yours")
    
    
def blackJack():

    print("| WELCOME TO THE BLACKJACK | ")

    answ = ""
    deck = [] 
    deck = create_deck()
    handplayer = []
    handdealer = []
    bet_ = bet()
    for _ in range(2):
        handplayer = (deal(deck,handplayer))
        handdealer = (deal(deck,handdealer))
    checkBlackJack(handplayer, handdealer, bet_)
    while answ != "q":
        if handValue(handplayer) > 21 or handValue(handplayer) == 21:
            finalScores(handplayer, handdealer, bet_)
            replay()
        elif handValue(handdealer) > 21 or handValue(handdealer) == 21:
            finalScores(handplayer, handdealer, bet_)
            replay()
            
        afficherhands(handplayer, handdealer)
        answ = input("Do you want to (H)it, (S)tay or (Q)uit")
        clearConsole()
        answ.lower()
        if answ == "q":
            return 
        elif answ == "h":
            if answ == "h":
                handplayer.append(tirer(deck)) 
        else: 
            while handValue(handdealer) < 17:
                    handdealer.append(tirer(deck))
            finalScores(handplayer, handdealer, bet_)
            answ = replay()

clearConsole()
blackJack()