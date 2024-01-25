def contains_dog(input_string):
    # Check if 'dog' is in the input string (case-insensitive)
    return 'dog' in input_string.lower()

str1 = input("Enter the sentence here:")
result1 = contains_dog(str1)
print(result1)  
