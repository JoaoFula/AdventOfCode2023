"""
We have to find the numbers that are adjacent to a symbol.
This can be above, below, left, right or even diagonally.
I will solve this exercise by separating the file into lines.
Then going line by line and checking if a number is adjacent to a symbol.
If it is, then we add it to the list to be summed up.
We check number by number instead of checking the symbols and their adjacencies for two reasons:
Easiness in reading the numbers
One number may be adjacent to 2 symbols but we only want to add it once.
We'll check the adjacencies by checking the line above (unless first line) and the
space to the left of where our number starts (i-1)(unless first column)
Then the space above it (i) and the space to the right (i+1).
Then we check the space to the left, above and to the right of the space where our
number finishes (unless last column)
Then we check the places to the left and right of our number (unless first or last column, respectively)
and finally we perform the same check as above to below (except last line)
We check left and right to cover for 4 digit numbers (even though I didn't see any)
"""


def check_symbols(character):
    if character in symbols:
        return True
    return False


def check_line(line, index):
    try:
        if check_symbols(line[index-1]):
            print("found a symbol:", line[index-1])
            return True
    except IndexError:
        pass
    try:
        if check_symbols(line[index]):
            print("found a symbol:", line[index])
            return True
    except IndexError:
        pass
    try:
        if check_symbols(line[index+1]):
            print("found a symbol:", line[index+1])
            return True
    except IndexError:
        pass


file = open("values.txt", "r")

content = file.read()

lines = content.splitlines()
symbols = {"!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","/"}
good_numbers = ["0"]

number = ""
number_flag = False
"""lines = ["-123......1#1..",
         "58....357..111",
         "@34....42...8/"]"""
for line_index, line in enumerate(lines):
    number = ""
    number_flag = False
    for character_index, character in enumerate(line):
        """We get the number and check the chars around the digit. If any of the chars is a symbol, we save the whole number.
        TODO case when a symbol is adjacent to two digits of the same number as it will """
        flag = False
        if character.isnumeric() and character not in number:
            #We assume numbers only have 3 digits here
            #We can have single digits, two digits and 3 digits
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
        if character.isnumeric():
            flag = check_line(line, character_index)
            if line_index != 0:
                if check_line(lines[line_index-1], character_index):
                    flag = True
            if line_index != len(lines)-1:
                if check_line(lines[line_index+1], character_index):
                    flag = True
        if flag is True and number_flag is False:
            good_numbers.append(number)
            number_flag = True

final_numbers = [int(number) for number in good_numbers]

#511305
#511346
#512106
#530849

"""
Conclusions:
Missed quite a few because did not account for /
Missed quite a few because did not account for two repeated numbers like 55$55 or 55.55 (solved this with flag)
Used Lines to practice. Better to have a practice list to make the program failproof"""