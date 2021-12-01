dept_scans = [0]
dept_increased = 0

with open('01/input.txt') as f:
    for dept in f.readlines():
        if int(dept) > dept_scans[-1]:
            dept_increased+=1
        dept_scans.append(int(dept))

print(dept_increased-1) # -1 to account for initial 0


# PART 2

initial_scan = dept_scans[0] + dept_scans[1] + dept_scans[2]
interval = 3
windows = [initial_scan]
dept_increased = 0

for i in range(0, len(dept_scans)-interval):
    if len(dept_scans) <= i + interval:
        break

    sum_window = 0
    for j in range(i, i+interval):
        sum_window += dept_scans[j]

    if sum_window > windows[-1]:
        dept_increased += 1
    windows.append(sum_window)

print(dept_increased)