import sys
import hashlib
import random
import argparse

# Template for a phrase structure
templates = [
    "verb article adj noun",
    "article adj adj noun",
    "article adv adj noun",
    "adv verb article noun",
]

# Dictionary to store words by type
words_by_type = {}

# List of word types
word_types = ["noun", "verb", "adj", "adv", "article"]

# Set of word types for efficient checking
word_types_set = set(word_types)

def template_for_index(index):
    # Returns the template for a given index.
    # The index is wrapped around the length of the templates list.
    wrapped_index = index % len(templates)
    return templates[wrapped_index]

def is_word_type_valid(word_type):
    # Checks if a given word type is valid.
    # Valid word types are present in the word_types_set.
    return word_type in word_types_set

def words_for_type(word_type):
    # Returns a list of words for a given word type.
    # The words are read from a file named "<word_type>.txt".
    # Caches the words in the words_by_type dictionary for future use.
    if word_type in words_by_type:
        return words_by_type[word_type]

    if not is_word_type_valid(word_type):
        return ""

    with open(word_type + ".txt") as f:
        words = [line.strip() for line in f]
        words_by_type[word_type] = words

    return words_by_type[word_type]

def create_word_list_for_type(word_type):
    # Creates a list of words for a given word type.
    # Reads words from a file named "index.<word_type>" and writes to "<word_type>.txt".
    with open(word_type + ".txt", "w") as f_out, open("index." + word_type) as f_in:
        for line in f_in:
            word = line.split()[0]
            if len(word) < 2 or "_" in word:
                continue
            f_out.write(word + "\n")

def word_for_index_and_type(index, word_type):
    # Returns a word for a given index and word type.
    # The word is selected from the list of words for the given word type.
    # The index is wrapped around the length of the word list.
    words = words_for_type(word_type)
    if not words:
        return word_type

    wrapped_index = index % len(words)
    return words[wrapped_index]

def generate_tripphrase(password):
    # Generates a tripphrase based on a given password.
    # Uses hashlib.md5 to generate a digest from the password.
    # Converts parts of the digest into indexes for selecting a template and words.
    # Constructs the tripphrase by substituting words into the template.
    digest = hashlib.md5(("BV" + password).encode("utf-8")).hexdigest()
    indexes = [int(digest[i:i+4], 16) for i in range(0, len(digest), 4)]

    template = template_for_index(indexes.pop(0))
    types = template.split()
    phrase_words = [word_for_index_and_type(indexes.pop(0), word_type) for word_type in types]
    phrase = " ".join(phrase_words)

    return phrase

def generate_random_tripphrase():
    # Generates a random tripphrase by generating a random secret/password
    # and using it to call the generate_tripphrase function.
    password = str(random.getrandbits(256))
    tripphrase = generate_tripphrase(password)
    return tripphrase

def generate_secret(length=16):
    # Generates a random secret of a specified length.
    # Returns the secret as a hexadecimal string.
    random_number = random.getrandbits(length * 4)  # Generate a random number
    secret = format(random_number, '0{}x'.format(length))  # Convert the random number to a hex string
    return secret

parser = argparse.ArgumentParser(description='Generate tripphrase from secret.')
parser.add_argument('secret', nargs='?', help='The secret to generate tripphrase from (optional).')

args = parser.parse_args()

if args.secret is None:
    password = generate_secret()
else:
    password = args.secret

tripphrase = f'({password}) {generate_tripphrase(password)}'
print(tripphrase)
