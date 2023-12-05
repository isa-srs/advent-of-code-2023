spelled_out = ['one', 'two', 'three', 'four', 
               'five', 'six', 'seven', 'eight', 'nine']
result = 0

with open('day1/input.txt') as file:
    for row in file:
        numbers = []
        for char in row:
            if char.isdigit():
                numbers.append((char, row.find(char)))
                if row.count(char) > 1:
                    numbers.append((char, row.rfind(char)))
        for word in spelled_out:
            if word in row:
                numbers.append((str(spelled_out.index(word)+1), row.find(word)))
                if row.count(word) > 1:
                    numbers.append((str(spelled_out.index(word)+1), row.rfind(word)))
        numbers.sort(key=lambda x: x[1])
        value = numbers[0][0]+numbers[-1][0]
        result += int(value)

print(result)