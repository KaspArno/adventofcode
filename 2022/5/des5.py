import re

stacks = []

f = open('5/input.txt', 'r')

line = f.readline()
len_line = len(line)
nr_of_stacks = (len_line//4)
stacks = [None] * nr_of_stacks
for i in range(0, len(stacks)):
    stacks[i] = []

pattern = '\w'
i = 0
while not re.search('\d', line):

    for match in re.finditer(pattern, line):
        s = match.start()
        e = match.end()
        stacks[s//4].append(line[s:e])

    line = f.readline()
    i += 1

line = f.readline()
line = f.readline()

while line:
    numbers = re.findall('\d+', line)
    move, fro, to = numbers
    move, fro, to = int(move), int(fro), int(to)
    moving = []
    # for i in range(0, move):
    #     moving.insert(0, stacks[fro-1].pop(0))
    moving = stacks[fro-1][0:move]
    stacks[fro-1] = stacks[fro-1][move:len(stacks[fro-1])]
    stacks[to-1] = moving + stacks[to-1]

    line = f.readline()

result = ''
for stack in stacks:
    result = result + stack[0]

print(result)