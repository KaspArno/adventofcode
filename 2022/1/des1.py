
with open('1/input.txt') as input:
    elf_total_calories = []
    total_calories = 0
    for line in input.readlines():
        line = line.strip()
        # print(line)
        if line == '':
            elf_total_calories.append(total_calories)
            total_calories = 0
        else: total_calories += int(line)

    elf_total_calories.sort()

    top3 = sum([elf_total_calories[-3], elf_total_calories[-2], elf_total_calories[-1]])
    print(top3)
