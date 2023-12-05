result = 0

with open('day1/input.txt') as file:
    for row in file:
        numbers = []
        for char in row:
            if char.isdigit():
                numbers.append(char)
        value = numbers[0]+numbers[-1]
        result += int(value)

print(result)