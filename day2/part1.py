class CubeGame:
    def __init__(self):
        self.red = 12
        self.green = 13
        self.blue = 14
        self.possible = True
        self.possible_games = []
    
    def split_row(self, row):
        row = row.replace('\n', '')
        sets = row.replace(':', ';').split(';')
        return sets
    
    def count_cubes(self, set):
        for i in range(len(set)):
            if set[i] == 'red':
                self.red -= int(set[i-1])
            elif set[i] == 'blue':
                self.blue -= int(set[i-1])
            elif set[i] == 'green':
                self.green -= int(set[i-1])
        
        if self.red < 0 or self.blue < 0 or self.green < 0:
            return False
        return True
        
    def reset_cubes(self):
        self.red = 12
        self.green = 13
        self.blue = 14

    def game(self):
        with open('day2/input.txt') as file:
            for row in file:
                sets = self.split_row(row)
                for set in sets[1:]:
                    set = set.replace(',', '').split()
                    if not self.count_cubes(set):
                        self.possible = False
                        break
                    self.reset_cubes()
                if self.possible:
                    game = int(sets[0][5:])
                    self.possible_games.append(game)
                self.reset_cubes()
                self.possible = True
        return sum(self.possible_games)


                        
            

if '__main__' == __name__:
    game = CubeGame()
    print(game.game())

