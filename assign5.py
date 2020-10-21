input_string = "MISSISSIPPI"
frequencies = {}

for ele in input_string:
    if ele in frequencies:
        frequencies[ele] += 1
    else:
        frequencies[ele] = 1

print("Please enter a string in '{}' is :\n{}".format(input_string, str(frequencies)))
