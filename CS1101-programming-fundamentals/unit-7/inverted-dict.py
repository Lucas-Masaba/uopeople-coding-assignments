def invert_dictionary(original_dict):
    # Declare variable for inverted dictionary
    inverted_dict = {}
    # Using nested for loop
    for student, courses in original_dict.items():
        for course in courses:
            if course not in inverted_dict:
                inverted_dict[course] = [student]
            else:
                inverted_dict[course].append(student)
    return inverted_dict

# Sample input
original_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Original dictionary
print(f"Original Dictionary: {original_dict}")

# Inverted dictionary
inverted_dict = invert_dictionary(original_dict)
print(f"\nInverted Dictionary: {inverted_dict}")