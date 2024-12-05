with open("day05.txt", "r") as file:
    lines = file.readlines()

hit_space = False
rules = []
updates = []
for line in lines:
    if line == "\n":
        hit_space = True
        continue
    elif hit_space:
        updates.append(line.strip())
    else:
        rules.append(line.strip())

print(updates)

total = 0
for update in updates:
    pages = update.split(",")
    valid = True
    for rule in rules:
        before, after = rule.split("|")
        try:
            i_before = pages.index(before)
            i_after = pages.index(after)
            if i_before > i_after:
                valid = False
                break
        except ValueError:
            pass
    if valid:
        total += int(pages[(len(pages) - 1) // 2])

print(total)
