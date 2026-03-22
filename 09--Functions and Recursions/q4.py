# Write a python function to remove a given word from a list ad strip it at the same time.
l = ["Harry", "Rohan", "Shivam", "Hammad", "an"]

def remove_and_strip(l, word):
    word = word.strip()  # remove extra spaces
    if word in l:
        l.remove(word)
        print("Updated list:", l)
    else:
        print("Word not found in the list.")

word_to_remove = input("Enter the word to remove: ")
remove_and_strip(l, word_to_remove)