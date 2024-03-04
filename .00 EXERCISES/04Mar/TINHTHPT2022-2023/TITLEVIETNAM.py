import re

def normalize_string(s):
    # Remove excess spaces
    s = re.sub(r'\s+', ' ', s).strip()

    # Convert the first letter of each word to uppercase and other characters to lowercase
    words = s.title().split()

    # Count the number of words in the string
    num_words = len(words)

    # Return the normalized string and the number of words
    return " ".join(words), num_words

# Example usage
input_string = "TrẦn THị MiNh Én"
normalized_string, num_words = normalize_string(input_string)
print("Normalized string:")
print(normalized_string)
print("Number of words in the string:", num_words)
