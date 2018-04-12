class Playerpoints(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def count_points(self):
        if self.first == 'J' or self.first == 'Q' or self.first == 'K':
            self.first = 10
        if self.second == 'J' or self.second == 'Q' or self.second == 'K':
            self.second = 10
        if self.first == 'A':
            z = input('would you like the A to be 1 or 11?')
            if z == '1':
                self.first = 1
            if z == '11':
                self.first = 11
        if self.second == 'A':
            z = input('would you like the A to be 1 or 11?')
            if z == '1':
                self.second = 1
            if z == '11':
                self.second = 11
        return self.first + self.second


class Dealerpoints(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def count_dealer_points(self):
        if self.first == 'J' or self.first == 'Q' or self.first == 'K':
            self.first = 10
        if self.second == 'J' or self.second == 'Q' or self.second == 'K':
            self.second = 10
        if self.first == 'A':
            self.first = 11
        if self.second == 'A':
            self.second = 11
        return self.first + self.second


cards = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
         9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']


def select_card():
    global cards
    import random
    a = random.choice(cards)
    cards.remove(a)
    print(a)
    return a


bet = input('how much do you want to bet? ')

print('You Have Been Dealt: ')
b = select_card()
print('The House Has Been Dealt: ')
d = select_card()
print('You Have Been Dealt: ')
c = select_card()
print('The House Has Been Dealt: ')
e = select_card()

print('Your Points Are: ')
f = Playerpoints(b, c)
playerstotal = f.count_points()
print(playerstotal)

print('The Dealers Points Are: ')
g = Dealerpoints(d, e)
dealerstotal = g.count_dealer_points()
print(dealerstotal)

while dealerstotal < 17:
    print('Dealer drawing:')
    h = select_card()
    newcard = Dealerpoints(h, 0)
    newpoint = newcard.count_dealer_points()
    dealerstotal = dealerstotal + newpoint
    print('The Dealers Points Are: ')
    print(dealerstotal)
    if dealerstotal > 21:
        print('dealer bust, you won: ')
        print(int(bet) * 2)

if playerstotal == 21:
    print('BLACKJACK! YOU WON!')
    print('you have won:')
    print(int(bet) * 2)
if dealerstotal == 21:
    print('BLACKJACK FOR THE HOUSE, YOU LOSE')
    print('you have lost:')
    print(int(bet))
if dealerstotal != 21 and playerstotal != 21 and playerstotal < 22:
    hitorstand = input('Hit or Stand?')
    if hitorstand == 'hit' or hitorstand == 'Hit':
        while hitorstand == 'hit' or hitorstand == 'Hit':
            h = select_card()
            i = Playerpoints(h, 0)
            newplayerpoint = i.count_points()
            playerstotal = playerstotal + newplayerpoint
            print('your points are: ')
            print(playerstotal)
            if playerstotal > 21:
                print('You blew it')
                break
            if playerstotal == 21:
                print('BLACKJACK! YOU WON: %s', bet * 2)
                break

            if dealerstotal > 21:
                print('Dealer Bust, you win: ')
                print(int(bet) * 2)
            hitorstand = input('Hit or Stand?')
    if hitorstand != 'hit' and hitorstand != 'Hit':
        if playerstotal > dealerstotal:
            print('you have WON:', )
            print(int(bet) * 2)
        if playerstotal < dealerstotal:
            print('you have LOST:')
            print(int(bet) * 2)
        if playerstotal == dealerstotal:
            print('Draw!, you get back your bet: ')
            print(bet)










