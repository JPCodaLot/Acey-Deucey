# See the README.md for more information

def calcChance(hand, deck):
    apart = abs(hand[0]-hand[1])
    if apart < 2:
        return False
    else:
        # chance = round(((apart-1)/13)*100)
        # print(chance,'%', sep='')
        if hand[0] < hand[1]:
            return round((sum(deck[ hand[0]+1 : hand[1] ])/sum(deck))*100,1)
        else:
            return round((sum(deck[ hand[1]+1 : hand[0] ])/sum(deck))*100,1)

def useCards(cards):
    global deck
    for card in cards:
        deck[card] -= 1

def translate(cards):
    for idx, val in enumerate(cards):
        if val == '1':
            cards[idx] = 8
        elif val == 'j':
            cards[idx] = 9
        elif val == 'q':
            cards[idx] = 10
        elif val == 'k':
            cards[idx] = 11
        elif val == 'a':
            cards[idx] = 12
        else:
            cards[idx] = int(val) - 2
    return cards

i = 0
deck = [4 for i in range(13)]

while sum(deck) > 2:
    i += 1
    print('Round', i, sep=' ')
    str = input()
    if str == 'x':
        break
    hand = translate(list(str))
    useCards(hand)
    chance = calcChance(hand, deck)
    if chance:
        print(chance, '%', sep='')
        hand = translate(list(input()))
        useCards(hand)
    else:
        print('No chance')
