def count_dog_occurrences(input_string):
    # Convert the input string to lowercase for case-insensitive matching
    input_lower = input_string.lower()

    # Count the occurrences of the word 'dog'
    count = input_lower.count('dog')

    return count


str1 = input("Enter your sentence here:")
count = count_dog_occurrences(str1)
print("Number of occurrences of 'dog':", count)
