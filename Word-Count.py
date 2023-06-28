from sys import argv
# this is how we get command line arguments
print(argv)
if len(argv) < 2:
    print("Please provide a filename.")
else:
    file = open(argv[1])
    print(file)
    lines = file.read()

    new_lines = lines.split("\n") # a list of strings
    line_count = len(new_lines) - 1
    word_count = 0
    letter_count = 0

    for line in new_lines:
        words = line.split(" ") # split each list of strings
        word_count += len(words) # word_count = word_count + len(words)
        letter_count += len(line) # letter_count = letter_count + len(line)

    print(f"The line count is {line_count}")
    print(f"The word count is {word_count}")
    print(f"The letter count is {letter_count}")
#%%
