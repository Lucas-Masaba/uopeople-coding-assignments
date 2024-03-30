def read_dict_from_file(file_name):
    # In this method, we will read the content of the input file. It is enclosed in a try-catch block to handle the FileNotFoundError exception.
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file and evaluate it as a dictionary using eval()
            original_dict = dict(eval(file.read())) 
            return original_dict
    except FileNotFoundError:
        # Handle the FileNotFoundError exception if the input file is not found
        print(f"Error: Input file '{file_name}' not found.")
        return {}

def invert_dictionary(original_dict):
    # Initialize an empty dictionary to store the inverted dictionary
    inverted_dict = {}
    # Iterate over each key-value pair in the original dictionary
    for key, value in original_dict.items():
        # Check if the value is a list
        if isinstance(value, list):
            # If the value is a list, iterate over each item in the list
            for item in value:
                # Set the item as the key in the inverted dictionary and append the original key to its value list
                inverted_dict.setdefault(item, []).append(key)
        else:
            # If the value is not a list, set the value as the key in the inverted dictionary and append the original key to its value list
            inverted_dict.setdefault(value, []).append(key)
    return inverted_dict

def write_dict_to_file(file_name, inverted_dict):
    # Open the output file in write mode
    with open(file_name, 'w') as file:
        # Write the string representation of the inverted dictionary to the output file
        file.write(str(inverted_dict))

# Read the original dictionary from the input file
original_dictionary = read_dict_from_file('input.txt')
# Invert the original dictionary
inverted_dictionary = invert_dictionary(original_dictionary)
# Write the inverted dictionary to the output file
write_dict_to_file('output.txt', inverted_dictionary)

# Print the original and inverted dictionaries for verification
print("Original Dictionary:")
print(original_dictionary)
print("\nInverted Dictionary:")
print(inverted_dictionary)
