class CubeGame:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.results = []

    def split_row(self, row):
        row = row.replace('\n', '')
        sets = row.replace(':', ';').split(';')
        return sets

    def count_cubes(self, set):
        for i in range(len(set)):
            if set[i] == 'red':
                if int(set[i-1]) > self.red:
                    self.red = int(set[i-1])
            elif set[i] == 'green':
                if int(set[i-1]) > self.green:
                    self.green = int(set[i-1])
            elif set[i] == 'blue':
                if int(set[i-1]) > self.blue:
                    self.blue = int(set[i-1])
    
    def power_of_set(self):
        return self.red * self.green * self.blue
    
    def reset_cubes(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def game(self):
        with open('day2/input.txt') as file:
            for row in file:
                sets = self.split_row(row)
                for set in sets[1:]:
                    set = set.replace(',', '').split()
                    self.count_cubes(set)
                self.results.append(self.power_of_set())
                self.reset_cubes()
        return sum(self.results)

if '__main__' == __name__:
    game = CubeGame()
    print(game.game())
