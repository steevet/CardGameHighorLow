print('''My name is Steeve Toussaint
I currently live in Mississauga, Canada
''')

# --------------------------------------------------------------------------------------------------------------------------

print('--- Welcome to High-Low ---')
print('''Start with 100 points. Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose.
Try to make it to 500 points within 10 tries.
''')

from random import randint

def getCardValue():
    value = randint(1, 14)
    return value

def getCardStr(cardvalue):
    valuestg = str(cardvalue).replace('10', 'T').replace('11', 'J').replace('12', 'Q').replace('13', 'K').replace('14', 'A')
    return valuestg

def getHLGuess():
    bet = ''
    while bet != 'H' or bet != 'L':
        bet = input('High or Low (H/L)?: ').upper().strip()
        if bet == 'H':
            high = 'HIGH'
            return high
        elif bet == 'L':
             low = 'LOW'
             return low

def getBetAmount(maximum):
    betP = 0
    while (betP < 1) or (betP > maximum):
        betP = int(input('Input bet amount: '))
    return betP

def playerGuessCorrect(card1, card2, betType):
    if betType == 'HIGH' and card1 > card2:
        return False
    elif betType == 'HIGH' and card1 < card2:
        return True
    elif betType == 'HIGH' and card1 == card2:
        return ""

    if betType == 'LOW' and card1 > card2:
        return True
    elif betType == 'LOW' and card1 < card2:
        return False
    elif betType == 'LOW' and card1 == card2:
        return ""

# --------------------------------------------------------------------------------------------------------------------------

# points = 100
# round = 1
# maxround = 10

def main():
    points = 100
    round = 1
    maxround = 10
    while True:
        print('\n-------------------------------------------------------------------')
        print("OVERALL POINTS: {} ROUND {}/{}".format(points, round, maxround))
        card1 = getCardValue()
        card11 = getCardStr(card1)
        card2 = getCardValue()
        card22 = getCardStr(card2)
        print("First card is a [{}]".format(card11))
        bettype = getHLGuess()
        betamount = getBetAmount(points)
        playerguess = playerGuessCorrect(card1, card2, bettype)
        print("Second card is a [{}]".format(card22))

        concl = ''
        if playerguess == True:
            points = points + betamount
            concl = "WON"
        elif playerguess == False:
            points = points - betamount
            concl = "LOST"
        else:
            points = points
            concl = "SAME CARD"

        print("Card1 [{}] Card2 [{}] - You bet '{}' for {} - YOU {}".format(card11, card22, bettype, betamount, concl))

        if points > 500 or points == 500:
            concl = 'LOSE'
            print("\n------------------WIN---------------------")
            print('YOU MADE IT TO *{}* POINTS IN {} ROUNDS!'.format(points, round))
            print("-------------------------------------------")
            break

        elif (points < 0 or points == 0):
            print("\n------------------LOSE---------------------")
            print('YOU HAVE *{}* POINTS AFTER {} ROUNDS!'.format(points, round))
            print("-------------------------------------------")
            break

        elif round == maxround:
            print("\n------------------LOSE---------------------")
            print('ONLY *{}* POINTS IN {} ROUNDS!'.format(points, round))
            print("-------------------------------------------")
            break

        else:
            round = round + 1


if __name__ == "__main__":
    main()
    x = True
    response = int(input('''Enter 1) to play again
Enter 2) to exit
'''))
    if response == 1:
        x = True
    else:
        x = False

    while x:
        main()
        response = int(input('''Enter 1) to play again
Enter 2) to exit
'''))
        if response == 1:
            x = True
        else:
            x = False




