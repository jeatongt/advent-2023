# Python
def string_to_calibration_value(calibration_string):
    for character in calibration_string:
        if character.isnumeric():
            first_number = character
            break
    for character in calibration_string:
        if character.isnumeric():
            last_number = character
    return 10*int(first_number) + int(last_number)

total = 0
with open('/Users/jeaton/Git/advent-2023/Day01-1/calibration-input.txt', 'r') as file:
    for line in file.readlines():
        calibration_string = line.strip()  # remove newline characters
        calibration_value = string_to_calibration_value(calibration_string)
        total += calibration_value
print(total)