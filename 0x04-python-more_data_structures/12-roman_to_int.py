#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Create a dictionary of Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the result
    result = 0

    # Iterate through the characters in the string, starting from the end
    for i in range(len(roman_string) - 1, -1, -1):
        # If the current character is greater than or equal to the previous
        #  character add its value to the result
        if i == len(roman_string) - 1 or \
         roman_values[roman_string[i]] >= roman_values[roman_string[i + 1]]:
            result += roman_values[roman_string[i]]
        # Otherwise, subtract its value from the result
        else:
            result -= roman_values[roman_string[i]]

    return result
