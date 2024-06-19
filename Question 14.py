#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
num_lines = int(input("How many lines would you like to enter? "))
lines = []
i = 0

for i in range(num_lines):
    line = input("Enter a line: ")
    lines.append(line)

print("\nYou entered:")
for line in lines:
    print(line)