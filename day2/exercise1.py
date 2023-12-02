"""
We have
12 red
13 green
14 blue
in exercise 1, we need to read through the values.txt
Each game is a line (with ID) followed by :
Each set is separated by a semicolon
The cubes taken are in the format: number colour
Each set can have a maximum of 12 red, 13 green or 14 blue
We then get the IDs where it is possible and we sum them.
"""

file = open("values.txt", "r")

content = file.read()

games = content.splitlines()
game_ids = []
bad_game_ids = []
for game in games:
    each_set = []
    #We first split between game and ID and the sets
    game_id, sets = game.split(": ")

    game, id = game_id.split()
    game_ids.append(int(id))
    #Then we split the sets
    each_set = sets.split("; ")

    #Then we split between the colours in each set
    for set in each_set:
        #We then split the sets into cubes
        cubes = set.split(", ")
        for cube in cubes:
            #We then split each cube into a number and a colour
            number, colour = cube.split()
            #Then we check the maximum values for each
            if "red" in colour and int(number) > 12:
                bad_game_ids.append(int(id))
            elif "green" in colour and int(number) > 13:
                bad_game_ids.append(int(id))
            elif "blue" in colour and int(number) > 14:
                bad_game_ids.append(int(id))

#We now have a list of all the games and a list of all the bad games
#We now check which games don't exist in the bad games list and we add it to the good games list
#We then sum that list (since they're ints) and we obtain the value
good_games = []
for game in game_ids:
    if game not in bad_game_ids:
        good_games.append(game)
print(sum(good_games))

#1867