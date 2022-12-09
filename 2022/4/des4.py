results = 0
results2 = 0

with open('4/input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        elf1, elf2 = line.split(',')
        elf1 = elf1.split('-')
        elf2 = elf2.split('-')

        if (int(elf1[0]) <= int(elf2[0]) and (int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and (int(elf2[1]) >= int(elf1[1])))): results += 1 

        for i in range(int(elf1[0]), int(elf1[1])+1):
            if (i in range(int(elf2[0]), int(elf2[1])+1)): 
                results2 += 1
                break

print(results)
print(results2)

