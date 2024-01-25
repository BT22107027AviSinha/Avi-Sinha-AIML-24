d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

# Getting the nested dictionary to grab the word hello
hello = d['k1'][3]['tricky'][3]['target'][3]

print(hello)
