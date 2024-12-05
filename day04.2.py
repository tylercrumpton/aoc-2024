with open("day04.txt", "r") as file:
    lines = file.readlines()

wordmap = {}
aes = []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        wordmap[(i, j)] = char
        if char == "A":
            aes.append((i, j))
count = 0
for i, j in aes:
    if (
        (wordmap.get((i + 1, j + 1)) == "S" and wordmap.get((i - 1, j - 1)) == "M")
        or (wordmap.get((i + 1, j + 1)) == "M" and wordmap.get((i - 1, j - 1)) == "S")
    ) and (
        (wordmap.get((i + 1, j - 1)) == "S" and wordmap.get((i - 1, j + 1)) == "M")
        or (wordmap.get((i + 1, j - 1)) == "M" and wordmap.get((i - 1, j + 1)) == "S")
    ):
        count += 1
print(count)
