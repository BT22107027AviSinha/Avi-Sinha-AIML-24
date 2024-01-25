def filter_words_starting_with_s(word_list):
    filtered_words = list(filter(lambda word: word.startswith('s'), word_list))
    return filtered_words

# Example usage with a predefined list
seq = ['soup', 'dog', 'salad', 'cat', 'great']
filtered_seq = filter_words_starting_with_s(seq)
print("Filtered words from predefined list:", filtered_seq)

# User input for the list
user_list = input("Enter a list of words separated by spaces: ").split()
filtered_user_list = filter_words_starting_with_s(user_list)
print("Filtered words from user input:", filtered_user_list)
