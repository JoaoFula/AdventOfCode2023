"""
The second exercise asks us what's the maximum number of cubes
for each colour for each game (they ask the other way around, what's the minimum for it to be played)

in exercise 2, we need to read through the values.txt
Each game is a line (with ID) followed by :
Each set is separated by a semicolon
The cubes taken are in the format: number colour
We need to find the maximum value for each colour in each game
I'm going to assume we cannot repeat colours in one set.
We then have to multiply the maximum value per colour per game
We then add the values of each game
"""


def multiplyList(list):
    #function to multiply elements on a list
    result = 1
    for i in list:
        result = result * i
    return result


file = open("values.txt", "r")

content = file.read()
result = []
games = content.splitlines()
game_ids = []
for game in games:
    each_set = []
    # We first split between game and ID and the sets
    game_id, sets = game.split(": ")

    game, id = game_id.split()
    game_ids.append(int(id))
    # Then we split the sets
    each_set = sets.split("; ")

    """ 
    We then create a dictionary where the keys are the colours and the values
    are the lists of the number cubes of that colour
    
    Note: we initialize the values with zero, in case that colour doesn't exist in the bag
    Otherwise we get an error"""

    numbers = {"red": [0],
               "green": [0],
               "blue": [0]}
    # Then we split between the colours in each set
    for set in each_set:
        # We then split the sets into cubes
        cubes = set.split(", ")
        for cube in cubes:
            # We then split each cube into a number and a colour
            number, colour = cube.split()
            numbers[colour].append(int(number))
    # Then we check the maximum values for each colour in the dict.
    max_numbers = []
    for i in numbers:
        max_numbers.append(max(numbers[i]))
    result.append(multiplyList(max_numbers))
print(sum(result))

#84538