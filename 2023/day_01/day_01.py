from word2number import w2n

with open("input", 'r') as input_file:
    lines = input_file.readlines()


def can_be_int(letter):
    try:
        int(letter)
        return letter
    except ValueError:
        return ''


calibration_values = []

for line in lines:
    value = ''.join(can_be_int(letter) for letter in line)
    if len(value) == 2:
        calibration_values.append(int(value))
    elif len(value) == 1:
        value += value
        calibration_values.append(int(value))
    elif len(value) >= 2:
        new_value = value[0] + value[-1]
        calibration_values.append(int(new_value))

print(calibration_values)
output = sum(calibration_values)
print(f"Solution task 1: {output}")


# Task 2
class BreakOutOfLoop(Exception):
    pass


calibration_values = []
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6',
           '7', '8', '9']


def find_numbers_in_string(line):
    string = ''
    output = ''
    try:
        for letter in line:
            string += letter
            for number in NUMBERS:
                index = string.find(number)
                if index != -1:
                    output += str(w2n.word_to_num(number))
                    raise BreakOutOfLoop
    except BreakOutOfLoop:
        string = ''
        for i in range(len(line) - 2, -1, -1):
            string = line[i] + string
            for number in NUMBERS:
                index = string.find(number)
                if index != -1:
                    output += str(w2n.word_to_num(number))
                    return output


for line in lines:
    value = find_numbers_in_string(line)
    if len(value) == 2:
        calibration_values.append(int(value))
    elif len(value) == 1:
        value += value
        calibration_values.append(int(value))
    elif len(value) >= 2:
        new_value = value[0] + value[-1]
        calibration_values.append(int(new_value))

print(calibration_values)
output = sum(calibration_values)

print(f"Solution task 2: {output}")
