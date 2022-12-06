letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum_priority = 0
group = []
sum_group_priority = 0
with open('3/input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        rom1 = line[0 : int(len(line)/2)]
        rom2 = line[int(len(line)/2) : len(line)]

        for char in rom1:
            if char in rom2:
                sum_priority += letters.index(char)+1
                break

        group.append(line)
        if (len(group) >= 3):
            for char in line:
                if (char in group[0]) and (char in group[1]):
                    sum_group_priority += letters.index(char)+1
                    break
            group = []


print(sum_priority)
print(sum_group_priority)