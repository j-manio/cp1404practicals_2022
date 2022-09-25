# odd numbers
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A. by 10s
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# B. count down by 1s
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C. star count
star_count = int(input('Number of stars: '))

for i in range(0, star_count, +1):
    print('*', end='')
print()

# D. star sequence
star_count = int(input('Number of stars: '))
for i in range(1, star_count + 2, 1):
    for n in range(1, i, 1):
        print('*', end=' ')
    print()
