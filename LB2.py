import re

digitsList = {
    '0': "ноль", '1': "один", '2': "два", '3': "три",
    '4': "четыре", '5': "пять", '6': "шесть", '7': "семь",
    '8': "восемь", '9': "девять"
}

def isPrime(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

def middleFour(num):
    num_str = str(num)
    mid_index = len(num_str) // 2
    return num_str[mid_index] == '4' if len(num_str) % 2 != 0 else num_str[mid_index - 1] == '4'

def digitToWord(number):
    return ' '.join(digitsList[digit] for digit in str(number))

inputFilename = 'LB2_input.txt'
outputFilename = 'LB2_result.txt'

with open(inputFilename, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'\b\d*4\d*\b'
matches = re.findall(pattern, content)

primesMidFour = [int(match) for match in matches if isPrime(int(match)) and int(match) <= 1000 and middleFour(int(match))]

minPrime = min(primesMidFour) if primesMidFour else None
maxPrime = max(primesMidFour) if primesMidFour else None


with open('LB2_result.txt', 'w', encoding='utf-8') as file:
    if minPrime is not None and maxPrime is not None:
        file.write("Минимальное число: " + digitToWord(minPrime) + '\n')
        file.write("Максимальное число: " + digitToWord(maxPrime) + '\n')
    else:
        file.write("Простые числа с средней цифрой 4 не найдены.\n")