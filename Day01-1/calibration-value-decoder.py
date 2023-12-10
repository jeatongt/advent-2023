# Python


def string_to_calibration_value(calibration_string):
    for character in calibration_string:
        if character.isnumeric():
            first_number = character
            break
    for character in calibration_string:
        if character.isnumeric():
            last_number = character
    return int(first_number) + int(last_number)


file = open('calibration-input.txt', 'r')
calibration_value = string_to_calibration_value(calibration_string)
print(calibration_value)
