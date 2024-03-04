# Store a list of words
word_list = input("Enter a list of words: ").split()

# Create a new list using list comprehension containing only the words with odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the new list
print("Words with odd number of characters:", odd_length_words)
