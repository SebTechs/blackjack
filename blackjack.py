#Python 3.9.13

import random
import os
import time

#Adjustable Paramater
computer_stand = 17

card = ["Ace", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King"]
computer_cards = []
human_cards = []

i=0
def showcards(cards, show):
    global i 
    
    if show == False and i == 1:
        print("[?]")
        i=0
    else:
        i = 1
        if cards == "Ace":
            print("[A]", end = " ")
        elif cards == "one":
            print("[1]", end = " ")
        elif cards == "two":
            print("[2]" ,end = " ")
        elif cards == "three":
            print("[3]" ,end = " ")
        elif cards == "four":
            print("[4]" ,end = " ")
        elif cards == "five":
            print("[5]" ,end = " ")
        elif cards == "six":
            print("[6]" ,end = " ")
        elif cards == "seven":
            print("[7]" ,end = " ")
        elif cards == "eight":
            print("[8]" ,end = " ")
        elif cards == "nine":
            print("[9]" ,end = " ")
        elif cards == "ten":
            print("[10]" ,end = " ")
        elif cards == "Jack":
            print("[J]" ,end = " ")
        elif cards == "Queen":
            print("[Q]" ,end = " ")
        elif cards == "King":
            print("[K]" ,end = " ")
        else:
            print(f"invalid {cards}")

def clearconsole():
    os.system('cls')


def initiateshowcards(show = False):
    global computer_cards, human_cards, i
    print("Computer cards")
    for cards in computer_cards:
        showcards(str(cards),show)
    i = 0
    print("\nPlayer cards")
    for cards in human_cards:
        showcards(str(cards),True)
    print("\n")

def getvalue(val_card, low_ace = False):
    if val_card == "Ace" and low_ace == True:
        return 1
    elif val_card == "Ace" and low_ace == False:
        return 11
    elif val_card == "one":
        return 1
    elif val_card == "two":
        return 2
    elif val_card == "three":
        return 3
    elif val_card == "four":
        return 4
    elif val_card == "five":
        return 5
    elif val_card == "six":
        return 6
    elif val_card == "seven":
        return 7
    elif val_card == "eight":
        return 8
    elif val_card == "nine":
        return 9
    elif val_card == "ten" or val_card == "Jack" or val_card == "Queen" or val_card == "King":
        return 10
    else:
        print(f"invalid {val_card}")

totalcomputer = 0
totalhuman = 0
def initiategetvalue(low_ace = False):
    global computer_cards, human_cards, totalcomputer ,totalhuman
    for cards in computer_cards:
        totalcomputer += getvalue(cards, low_ace)
    for cards in human_cards:
        totalhuman += getvalue(cards, low_ace)

def generate(card):
    cards = []
    cards.append(random.choice(card))
    cards.append(random.choice(card))
    return cards

def hit(card):
    hit_card = random.choice(card)
    return hit_card

def computercardsshow():
    global computer_cards
    for cards in computer_cards:
        showcards(str(cards),True)
    print("\n")

player_name = ""


clearconsole()  
print("Welcome to this amazing blackjack game.")
print("Game is simple get 21 and dont go over AND win against the dealer (computer)")
print(f"Computer will always stand on {computer_stand}")
print("Let's begin with your name please:")
player_name = input(" - ")
playing = True
print(f"hi {player_name}")
while playing == True:
    human_cards = generate(card)
    computer_cards = generate(card)
    print(human_cards )
    print(computer_cards)
    game = True
    blackjack = "None"
    bust = "None"
    while game == True:
        clearconsole()
        initiateshowcards()
        totalcomputer = 0
        totalhuman = 0
        initiategetvalue()
        if (totalcomputer == 21):
            blackjack = "C"
            print("BLACKJACK")
            break
        if (totalhuman == 21):
            blackjack = "human"
            print("BLACKJACK")
            break

        if(totalhuman > 21 ):
            totalhuman = 0
            initiategetvalue(True)
            if(totalhuman > 21):
                bust = "human"
                print("BUST")
                break
        while(True):
            print("Would you like to (1)hit or (2)stand?")
            option = int(input("- "))
            if option == 1 or option == 2:
                break
            else:
                print("Input either 1 or 2")

        if option == 1:
            human_cards.append(hit(card))
        else:
            break

    clearconsole()
    if blackjack == "human" and bust == "None":
        winner = player_name
        reason = "Blackjack / 21"
    elif bust == "human":
        winner = "Computer"
        reason = "player bust computer won by deafult."
    elif blackjack == "C":
        winner = "Computer"
        reason = "BlackJack"
    elif totalhuman > totalcomputer:
        while True:
            clearconsole()
            totalcomputer = 0
            totalhuman = 0
            initiategetvalue()
            if totalcomputer < computer_stand and totalcomputer <= totalhuman:
                computer_cards.append(hit(card))
                print("Computer has decided to hit.")
                computercardsshow()
                totalcomputer = 0
                totalhuman = 0
                initiategetvalue()
                time.sleep(1)
                if totalcomputer > 21:
                    totalcomputer = 0
                    totalhuman = 0
                    initiategetvalue(True)
                    if totalcomputer > 21:
                        print("Bust")
                        bust = "C"
                        winner = player_name
                        reason = "Computer has busted"
                        break       
            elif totalcomputer == computer_stand and totalcomputer < totalhuman:
                winner = player_name
                reason = f"Computer stands at {computer_stand}"
                break
            elif totalcomputer == computer_stand and totalcomputer > totalhuman:
                winner = "Computer"
                reason = "Computer has a greater number."
                break
            elif totalcomputer > totalhuman:
                winner = "Computer"
                reason = "Computer has a greater number."
                break
            elif totalcomputer == computer_stand and totalcomputer == totalhuman:
                winner = "Nobody"
                reason = "It's a draw!"
                break
            else:   
                winner = player_name
                reason = f"{player_name} has a greater number than computer"             
                break
    elif totalcomputer > totalhuman:
        winner = "Computer"
        reason = "Computer has a greater number."
    else:
        winner = "Nobody"
        reason = "It's a draw!"

    clearconsole()
    print(f"Computer must stand at {computer_stand}")
    initiateshowcards(True)
    print(f"\nThe winner is {winner} because {reason}\n")
    while(True):
        print("Would you like to play again?")
        print("(1) Yes\n(2) No")
        option = int(input("- "))
        if option == 1 or option == 2:
            break
        else:
            print("Input either 1 or 2")
    if option == 1:
        print("Let's gooo...")
        winner = "None"
        reason = "None"
        totalcomputer = 0
        totalhuman = 0
        human_cards = []
        computer_cards = []
    else:
        playing = False
    
print("Goodbye...")


    
    
