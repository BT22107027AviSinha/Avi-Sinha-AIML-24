def extract(email):
    position = email.index('@')  # Finding the position of '@' in the email address
    domain = email[position + 1:]  # Splitting the substring starting from the character after '@'
    dot = domain.index('.')
    domain = domain[:dot]
    return domain

email = "user@example.com"
result = extract(email)
print(result)

def extract(New_Email):
    position = New_Email.index('@')  # Use the function parameter New_Email here
    domain = New_Email[position + 1:]
    dot = domain.index('.')
    domain = domain[:dot]
    return domain

New_Email = input("You can enter your own email address as well:")
result1 = extract(New_Email)
print(result1)
