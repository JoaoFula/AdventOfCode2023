file = open("values.txt", "r")

content = file.read()

lines = content.splitlines()
first_i = []
last_i = []
final_i = []
min_index = []
max_index = []

for index, line in enumerate(lines):
    """
    First we find the spelled out values and their position in the line.
    Then we obtain the smallest index.
    If it doesn't exist, we set it to 1000 so that the numerical always shows.
    """
    numericals = [line.find("one"), line.find("two"), line.find("three"),
                  line.find("four"), line.find("five"), line.find("six"),
                  line.find("seven"), line.find("eight"), line.find("nine")]
    try:
        min_index.append(min(i for i in numericals if i >= 0))
    except ValueError:
        min_index.append(1000)
    """
    Then we check if there's any numeral with a smaller index.
    If there is, save that value
    If there isn't, populate with the spelled out value (as int)
    """
    for i, c in enumerate(line):
        if c.isnumeric() and i < min_index[index]:
            first_i.append(c)
            break
    try:
        first_i[index]
    except IndexError:
        first_i.append(numericals.index(min_index[index]) + 1)

    """
    Then we repeat the process for the reversed line 
    and max index from the spelled out numbers.
    """
    rnumericals = [line.rfind("one"), line.rfind("two"), line.rfind("three"),
                  line.rfind("four"), line.rfind("five"), line.rfind("six"),
                  line.rfind("seven"), line.rfind("eight"), line.rfind("nine")]
    try:
        max_index.append(max(i for i in rnumericals if i >= 0))
    except ValueError:
        max_index.append(0)

    for i, c in enumerate(reversed(line)):
        if c.isnumeric() and i < (len(line)-max_index[index]):
            last_i.append(c)
            break
    try:
        last_i[index]
    except IndexError:
        last_i.append(rnumericals.index(max_index[index]) + 1)


for index, value in enumerate(first_i):
    final_i.append(int(str(value) + str(last_i[index])))

print(sum(final_i))
