from functools import cmp_to_key

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


def page_compare(a, b):
    for rule in rules:
        before, after = rule.split("|")
        if a == before and b == after:
            return -1
        elif a == after and b == before:
            return 1
    return 0


total = 0
for update in updates:
    pages = update.split(",")
    valid = True
    sorted_pages = pages
    for rule in rules:
        before, after = rule.split("|")
        try:
            i_before = pages.index(before)
            i_after = pages.index(after)
            if i_before > i_after:
                sorted_pages = sorted(pages, key=cmp_to_key(page_compare))
                valid = False
                break
        except ValueError:
            pass
    if not valid:
        total += int(sorted_pages[(len(sorted_pages) - 1) // 2])

print(total)
