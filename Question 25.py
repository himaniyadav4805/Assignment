# Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except IOError as e:
        print(f"Error copying file: {e}")