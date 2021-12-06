zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
onese = [0,0,0,0,0,0,0,0,0,0,0,0]
binary_array = []

# 111010101100
with open('03/input.txt') as f:
    for line in f.readlines():
        binary_str = line.strip()
        binary_array.append(binary_str)

        desimal = int(binary_str, 2)
        inverse_str = desimal ^ (2 ** (len(binary_str) + 1) - 1)
        binary_str_reversed = bin(inverse_str)[3 : ]

        # zeros += int(binary_str_reversed, 2)
        # onese += int(binary_str, 2)

        for i in range(0, len(binary_str)):
            zeros[i] += int(binary_str_reversed[i])
            onese[i] += int(binary_str[i])

print(zeros)
print(onese)

gamma = ''
epsilon = ''

for i in range(0, len(zeros)):
    if (zeros[i] > onese[i]):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(gamma)
print(epsilon)

result = int(gamma,2)*int(epsilon,2)
print(result)


# PART 2

oxygen = binary_array
co2 = binary_array
len_o = len(oxygen)
len_c = len(co2)

while len_o > 1 and len_c > 1:
    for i in range(0, len(zeros)):
        for b in range(0, len(binary_array)):
            if onese[i] < zeros[i]:
                oxygen[b] = ''
            if onese[i] > zeros[i]:
                co2[b] = ''
    
    len_o = len(list(filter(lambda a: a != '', oxygen)))
    len_c = len(list(filter(lambda a: a != '', co2)))

#     print(oxygen)


oxygen = len(list(filter(lambda a: a != '', oxygen)))
co2 = len(list(filter(lambda a: a != '', co2)))
print(oxygen)
print(co2)

print(int(oxygen[0],2)*int(co2[0],2))
