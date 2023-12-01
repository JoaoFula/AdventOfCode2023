file = open("values.txt", "r")

content = file.read()

lines = content.splitlines()
first_i = []
last_i = []
final_i = []
for index, line in enumerate(lines):
    for c in line:
        if c.isnumeric():
            first_i.append(c)
            break

    for c in reversed(line):
        if c.isnumeric():
            last_i.append(c)
            break

for index, value in enumerate(first_i):
    final_i.append(int(value + last_i[index]))

print(sum(final_i))
