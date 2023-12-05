class Engine:
    def __init__(self):
        self.file = 'day3/test.txt'
        self.schem = []
        self.result = 0
    
    def read_file(self):
        with open(self.file) as file:
            for row in file:
                row = row.replace('\n', '')
                self.schem.append(row)

    def check_character(self, row, column):
        character = self.schem[row][column]
        if character.isdigit() or character == '.':
            return False
        return True


    def check_adjacents(self, row, column):
        adjacent_to_symbol = False
        if row != 0:
            if column != 0:
                if self.check_character(row-1, column-1):
                    adjacent_to_symbol = True
            if self.check_character(row-1, column):
                adjacent_to_symbol = True
            if column < self.schem[0]:
                if self.check_character(row-1, column+1):
                    adjacent_to_symbol = True
            



    def start(self):
        for i in range(len(self.schem)):
            for j in range(len(i)):
                number = ''
                character = self.schem[i][j]
                if character.isdigit():
                    number += character
                elif number != '':
                    self.check_adjacents(i, j)
                else:
                    number = ''

if '__main__' == __name__:
    en = Engine()
    en.read_file()