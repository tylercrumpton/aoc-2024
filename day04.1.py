with open("day04.txt", "r") as file:
    lines = file.readlines()

wordmap = {}
xes = []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        wordmap[(i, j)] = char
        if char == "X":
            xes.append((i, j))
count = 0
for i, j in xes:
    if (
        wordmap.get((i + 1, j)) == "M"
        and wordmap.get((i + 2, j)) == "A"
        and wordmap.get((i + 3, j)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i - 1, j)) == "M"
        and wordmap.get((i - 2, j)) == "A"
        and wordmap.get((i - 3, j)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i, j + 1)) == "M"
        and wordmap.get((i, j + 2)) == "A"
        and wordmap.get((i, j + 3)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i, j - 1)) == "M"
        and wordmap.get((i, j - 2)) == "A"
        and wordmap.get((i, j - 3)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i + 1, j + 1)) == "M"
        and wordmap.get((i + 2, j + 2)) == "A"
        and wordmap.get((i + 3, j + 3)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i - 1, j - 1)) == "M"
        and wordmap.get((i - 2, j - 2)) == "A"
        and wordmap.get((i - 3, j - 3)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i + 1, j - 1)) == "M"
        and wordmap.get((i + 2, j - 2)) == "A"
        and wordmap.get((i + 3, j - 3)) == "S"
    ):
        count += 1
    if (
        wordmap.get((i - 1, j + 1)) == "M"
        and wordmap.get((i - 2, j + 2)) == "A"
        and wordmap.get((i - 3, j + 3)) == "S"
    ):
        count += 1

print(count)
