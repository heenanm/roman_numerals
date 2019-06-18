def numerals_to_number(numerals):
    """ Function to convert roman numerals """    
    
    numeral_values = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'm': 1000}
    integer_values = []

# Get a list numeric values from roman numerals.
    for char in numerals:
        integer_values.append(numeral_values[char])   

# Empty list to store numbers after addition/subtraction of numeral values.
    converted_values = []

# Deal with each integer pair and decide if addition or subtraction required.
    while integer_values:
        last_number = integer_values.pop(-1)
        previous_number = 0

# Check if integer values is empty before attempting to pop value.      
        if integer_values:
            previous_number = integer_values.pop(-1)

# Run tests to see if addition/subtraction necessary.
        if previous_number == 0:
            pair_total = last_number
        
        elif last_number > previous_number:
            pair_total = last_number - previous_number
        
        elif last_number <= previous_number:
            pair_total = last_number + previous_number   
        
        converted_values.append(pair_total)

# When all values moved from integer values to converted values print sum.
    return sum(converted_values)


print(numerals_to_number('i'))
print(numerals_to_number('ii'))
print(numerals_to_number('iii'))
print(numerals_to_number('iv'))
print(numerals_to_number('v'))
print(numerals_to_number('vi'))
print(numerals_to_number('vii'))
print(numerals_to_number('viii'))
print(numerals_to_number('ix'))
print(numerals_to_number('x'))



