# This script allows the user to paste words one by one from a word sequence
# they previously input, and to change the word they are pasting by
# pressing ctrl+v. The script adds a space at the end of each word
# when it is copied to the clipboard.

# Import the clipboard and keyboard modules
import clipboard
import keyboard

# Prompt the user to input a sentence
sentence = input("Enter a word sequence: ")
print("Do you want to add space at the end of each word ? y/n(default):")
space = input()
# Split the word sequence into a list of words
words = sentence.split()

# Keep track of the current word index
word_index = -1

if(space == "y"):
    while True:
        # Loop until the user presses ctrl+c to exit
        # Copy the current word to the clipboard, with a space at the end
        clipboard.copy(words[word_index] + " ")

        # Prompt the user to paste the next word
        print("Paste the next word (press ctrl+v to change the word):")

        # Wait for the user to press ctrl+v
        keyboard.wait("ctrl+v")

        # Increment the current word index
        word_index = (word_index + 1) % len(words)

else:
    # Loop until the user presses ctrl+c to exit
    while True:
        # Copy the current word to the clipboard, with a space at the end
        clipboard.copy(words[word_index])

        # Prompt the user to paste the next word
        print("Paste the next word (press ctrl+v to change the word):")

        # Wait for the user to press ctrl+v
        keyboard.wait("ctrl+v")

        # Increment the current word index
        word_index = (word_index + 1) % len(words)


