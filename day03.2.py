import re

with open("day03.txt", "r") as file:
    text = file.read()

text = text.replace("\n", "")

total = 0
is_dont = False
for i in range(len(text)):
    if text[i - 7 : i] == "don't()":
        is_dont = True
    elif text[i - 4 : i] == "do()":
        is_dont = False
    elif text[i - 4 : i] == "mul(" and not is_dont:
        match = re.match(r"^(\d+),(\d+)\)", text[i:])
        if match:
            print(f"mul: {match.groups()}")
            total += int(match.group(1)) * int(match.group(2))

print(total)
