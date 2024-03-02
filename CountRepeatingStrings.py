import colorama
import colorama
from colorama import Fore, Style


def CountRepeatingStrings(list_of_strings):
    # Create a dictionary to store the count of each string
    string_counts = {}

    # Iterate over the list of strings
    for string in list_of_strings:
        # If the string is already in the dictionary, increment its count 
        if string in string_counts:
            string_counts[string] += 1
        # Otherwise, add the string to the dictionary with a count of 1
        else:
            string_counts[string] = 1

    # Return the dictionary with the string counts
    return string_counts

# Example list of strings
list_of_strings = ["apple", "banana", "cherry", "apple", "dog", "cat", "banana"]

# Get the count of repeating strings
string_counts = CountRepeatingStrings(list_of_strings) 

# Print the count of each string in different colors
for string, count in string_counts.items():
    print(f"{Fore.GREEN}{string}: {Fore.RED}{count}{Style.RESET_ALL}")
