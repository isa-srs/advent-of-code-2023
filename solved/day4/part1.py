class Cards:
    def __init__(self, cards):
        self.cards = cards
        self.results = 0
    
    def check(self):
        result = 0
        for i in self.numbers:
            if i != '' and i in self.winning:
                if result == 0:
                    result = 1
                else:
                    result *= 2
        return result

    def start(self):
        for row in cards:
            sets = row.replace('\n', '').split('|')
            self.winning = sets[0].split(':')[1].split(' ')
            self.numbers = sets[1].split(' ')
            self.results += self.check()
        
        return self.results
            



if '__main__' == __name__:
    with open('day4/input.txt') as file:
        cards = file.readlines()
    c = Cards(cards)
    print(c.start())