#Write a python program that takes a string as input and returns its length.
def calculate_length(input_string):
    length = len(input_string)
    return length

user_input = input("Enter a string: ")

length_of_string = calculate_length(user_input)

print(f"Length of the string '{user_input}' is {length_of_string}")