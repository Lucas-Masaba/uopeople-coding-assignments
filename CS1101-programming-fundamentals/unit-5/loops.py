# Function to display n characters from the left of the name
def display_n_characters(name, n):
    print(f"Displaying {n} characters from the left of the name:")
    print(name[:n])

# Function to count the number of vowels in the name
def count_vowels(name):
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in name if char in vowels)
    print("Number of vowels in the name:", vowel_count)

# Function to reverse the name
def reverse_name(name):
    reversed_name = name[::-1] # Using string slicing to reverse string
    print("Reversed name:", reversed_name)

# Main function
def main():
    # Input name from the user
    name = input("Enter your name: ")

    # Display name
    print("Original name:", name)

    # Prompt user for the number of characters to display from the left
    n = int(input("Enter the number of characters to display from the left: "))
    # Call function to display n characters from the left of the name
    display_n_characters(name, n)

    # Call function to count the number of vowels
    count_vowels(name)

    # Call function to reverse the name
    reverse_name(name)

main()