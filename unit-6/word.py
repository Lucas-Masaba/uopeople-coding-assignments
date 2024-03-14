# Create a function to convert a sentence into a word list and reverse it
def reverse_wordlist(sentence):
    # Split the sentence into words using the split method
    word_list = sentence.split()
    # Reverse the word list using slicing
    reversed_word_list = word_list[::-1]
    # Return the reversed word list
    return reversed_word_list

# Input sentence
sentence = "the quick brown fox jumps over the lazy dog."

# Convert sentence into a word list and reverse it by cakking the reverse_wordlist function
reversed_list = reverse_wordlist(sentence)

# Output
print("Original Sentence:", sentence)
print("Reversed Word List:", reversed_list)