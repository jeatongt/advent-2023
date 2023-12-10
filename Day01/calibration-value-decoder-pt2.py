# Python
def string_to_calibration_value(calibration_string):
    number_string = ''
    for character in calibration_string:
        if character.isnumeric():
            first_number = character
            break
        number_string = number_string + character
        if 'one' in number_string:
            first_number = '1'
            break
        if 'two' in number_string:
            first_number = '2'
            break
        if 'three' in number_string:
            first_number = '3'
            break
        if 'four' in number_string:
            first_number = '4'
            break
        if 'five' in number_string:
            first_number = '5'
            break
        if 'six' in number_string:
            first_number = '6'
            break
        if 'seven' in number_string:
            first_number = '7'
            break
        if 'eight' in number_string:
            first_number = '8'
            break
        if 'nine' in number_string:
            first_number = '9'
            break
        if 'zero' in number_string:
            first_number = '0'
            break
    last_number_string = ''
    for character in calibration_string:
        if character.isnumeric():
            last_number = character
            last_number_string = ''
        last_number_string = last_number_string + character
        if 'one' in last_number_string:
            last_number = '1'
            last_number_string = character
        if 'two' in last_number_string:
            last_number = '2'
            last_number_string = character
        if 'three' in last_number_string:
            last_number = '3'
            last_number_string = character
        if 'four' in last_number_string:
            last_number = '4'
            last_number_string = character
        if 'five' in last_number_string:
            last_number = '5'
            last_number_string = character
        if 'six' in last_number_string:
            last_number = '6'
            last_number_string = character
        if 'seven' in last_number_string:
            last_number = '7'
            last_number_string = character
        if 'eight' in last_number_string:
            last_number = '8'
            last_number_string = character
        if 'nine' in last_number_string:
            last_number = '9'
            last_number_string = character
    return 10*int(first_number) + int(last_number)

total = 0
with open('/Users/jeaton/Git/advent-2023/Day01/calibration-input.txt', 'r') as file:
    for line in file.readlines():
        calibration_string = line.strip()  # remove newline characters
        calibration_value = string_to_calibration_value(calibration_string)
        total += calibration_value
print(total)