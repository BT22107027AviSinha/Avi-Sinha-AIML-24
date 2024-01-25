def sum_of_series(n):
    result = 0
    term = 2

    for i in range(1, n + 1): #Adjusting the equation for the said problem
        result += term
        term = term * 10 + 2

    return result

n_terms = int(input("Enter the number of terms in the series: "))
result = sum_of_series(n_terms)
print("Sum of the series:", result)
