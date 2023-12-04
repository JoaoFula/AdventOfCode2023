file = open("values.txt", "r")

content = file.read()

lines = content.splitlines()

card_dict = {}

for line in lines:
    game, cards = line.split(":")
    aux, game_index = game.split()
    card_dict[aux+game_index] = {"instances": 1}

print(card_dict)
for line in lines:
    game, cards = line.split(":")
    aux, game_index = game.split()
    winning_card, our_card = cards.split(" | ")
    winning_numbers = winning_card.split()
    our_numbers = our_card.split()
    found = 0

    for number in our_numbers:
        if number in winning_numbers:
            found += 1
    print("found", found, "in game", game)

    for i in range(found):
        try:
            add_to_game = int(game_index) + int(i) + 1
            next_game = f"{aux}{str(add_to_game)}"
            card_dict[next_game]["instances"] += card_dict[aux+game_index]["instances"]
            print(next_game, card_dict[next_game]["instances"], aux+game_index, card_dict[aux+game_index]["instances"])
            # print(next_game)
        except KeyError:
            continue

total = 0
for game in card_dict:
    total += card_dict[game]["instances"]
    print(game, card_dict[game]["instances"])
print(total)
# 3161132
#8467762