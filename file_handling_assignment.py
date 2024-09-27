try:
    with open("my_file.txt", "w") as file:
        file.write("This is a line of text.\n")
        file.write(
            "The number 42 is the answer to life, the universe, and everything.\n")
        file.write("All letters of English alphabets are 26 and 10 numbers.\n")
        file.write("The number 444 is used to represent a man.\n")
        file.write("I'm keen on python programming. Thank you!\n\n")

    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("my_file.txt contents:\n\n")
        print(contents)

    with open("my_file.txt", "a") as file:
        file.write("\nThis is a first appended line of text.\n")
        file.write("This is a second appended line of text.\n")
        print("Two sentences appended to the original file\n")
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except PermissionError:
    print("You don't have permission to read and write this file.")
finally:
    print("File operations completed successfully.")
