# 1
out_file = open('name.txt', 'w')
get_name = str(input('What is your name?: '))
print(get_name, file=out_file)
out_file.close()

# 2
in_file = open('name.txt', 'r')
name = in_file.read()
in_file.close()
print(f'Your name is {name}')

# 3
in_file = open('numbers.txt', 'r')
read_line_one = int(in_file.readline())
read_line_two = int(in_file.readline())

in_file.close()
print(read_line_one + read_line_two)

# 4

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    all_lines = int(line)
    total += all_lines

in_file.close()
print(total)

