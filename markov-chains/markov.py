"""Generate Markov text from text files."""

from random import choice
import sys

file_name = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_name)
    text = file.read()
    return text



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
        
        {Would, you} : [could, could, could, like, like]
    """
    full_text = open_and_read_file(file_name)
    full_text_lst = full_text.rstrip('\n').split()
    
    chains = {}

    for i in range(len(full_text_lst) - 2):
        key_list = []
        
        key_list.append(full_text_lst[i])
        key_list.append(full_text_lst[i + 1])

        key_tuple = tuple(key_list)

        value = []
        value.append(full_text_lst[i + 2])
        print(full_text_lst[i+2])

        chains[key_tuple] = value


    print(chains)
    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
