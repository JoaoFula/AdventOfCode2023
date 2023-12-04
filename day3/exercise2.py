"""
We have to find the numbers adjacent to *
We only consider those that have EXACTLY two numbers adjacent to *
Less or more than two adjacent numbers means we discard that *
We then need to multiply those two numbers and add it to our good_numbers list
We then sum that list up
"""


def is_gear(character):
    if character in gear:
        return True
    return False


def check_line(line, index):
    try:
        if is_gear(line[index-1]):
            print("found a symbol:", line[index-1])
            return index-1
    except IndexError:
        pass
    try:
        if is_gear(line[index]):
            print("found a symbol:", line[index])
            return index
    except IndexError:
        pass
    try:
        if is_gear(line[index+1]):
            print("found a symbol:", line[index+1])
            return index+1
    except IndexError:
        pass
    return 0


file = open("values.txt", "r")

content = file.read()

lines = content.splitlines()
gear = {"*"}
good_numbers = ["0"]

number = ""
number_flag = False
gear_dict = {}

lines = ["-123......1#1..",
         "58*...555.*.111",
         "@34...*555...8/"]

for line_index, line in enumerate(lines):
    number = ""
    number_flag = False
    for character_index, character in enumerate(line):
        """We search for the *
         Once we have it, we check the surroundings for the numbers.
         If we find one number, we add it to a two element list
         If we find another one, add it to the second element
         If we find a third one, we catch the exception and proceed"""
        if character.isnumeric() and character not in number:
            try:
                if line[character_index + 1].isnumeric():
                    number = character + line[character_index + 1]
                    try:
                        if line[character_index + 2].isnumeric():
                            number = number + line[character_index + 2]
                    except IndexError:
                        print("end of line")
                else:
                    number = character
            except IndexError:
                print("end of line")
            print("number is", number)
        elif not character.isnumeric():
            number_flag = False
            number = ""

        """
        From here we created two functions, one to check if a character is a symbol
        Then to check the previous index, actual index and next index"""
        flag = False
        if character.isnumeric():
            if check_line(line, character_index) != 0:
                gear_dict[f"{line_index}, {check_line(line, character_index)}"] = number
                flag = True

            if line_index != 0:
                if check_line(lines[line_index-1], character_index) != 0:
                    gear_dict[f"{line_index}, {check_line(line, character_index)}"] = number
                    flag = True
            if line_index != len(lines)-1:
                if check_line(lines[line_index+1], character_index):
                    gear_dict[f"{line_index}, {check_line(line, character_index)}"] = number
                    flag = True


