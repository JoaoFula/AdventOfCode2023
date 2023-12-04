file = open("values.txt", "r")

content = file.read()

lines = content.splitlines()
points = 0

for line in lines:
    game, cards = line.split(":")
    winning_card, our_card = cards.split(" | ")
    winning_numbers = winning_card.split()
    our_numbers = our_card.split()
    found = 0

    for number in our_numbers:
        if number in winning_numbers:
            found += 1

    if found == 0:
        card_points = 0
    else:
        card_points = 2**(found - 1)

    print(f"{game}: {card_points}")
    points += card_points

print(points)
#26346