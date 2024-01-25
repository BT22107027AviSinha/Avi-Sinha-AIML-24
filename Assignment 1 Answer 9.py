def caught_speeding(speed, is_birthday):
    # Adjust speed limit if it's the birthday
    if is_birthday:
        speed -= 5

    # Determine the result based on speed
    if speed <= 60:
        return "No Challan"
    elif 61 <= speed <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

# Example usage:
result1 = caught_speeding(81, True)
result2 = caught_speeding(81, False)

print("Result 1:", result1)  # Output: "Small Challan"
print("Result 2:", result2)  # Output: "Heavy Challan"

# For practical input usage
user_speed = input("Enter the speed of the vehicle, officer: ")

# Convert the input to an integer
user_speed = int(user_speed)

# Assume it's not the driver's birthday 
user_is_birthday = False

result3 = caught_speeding(user_speed, user_is_birthday)
print("Result 3:", result3)
