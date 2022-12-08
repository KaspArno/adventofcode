forward = 0
depth = 0

with open('02/input.txt') as f:
    for line in f.readlines():
        direction, value = line.split(' ')
        value = int(value)

        if direction == 'forward': forward+=value
        elif direction == 'down': depth+=value
        elif direction == 'up': depth-=value
        else:
            print("Unknown direction: " + direction)
            break

# print("forward: " + str(forward))
# print("depth: " + str(depth))
# print("PRODUCT: " + str(forward*depth))


# PART 2

forward = 0
depth = 0
aim = 0

with open('02/input.txt') as f:
    for line in f.readlines():
        direction, value = line.split(' ')
        value = int(value)
        
        if direction == 'forward': 
            forward+=value
            depth+=value*aim
        elif direction == 'down': aim+=value
        elif direction == 'up': aim-=value
        else:
            print("Unknown direction: " + direction)
            break
        print("")

print("forward: " + str(forward))
print("depth: " + str(depth))
print("aim: " + str(aim))
print("PRODUCT: " + str(forward*depth))