# put your code here.
import sys

filename = sys.argv[1]


def word_counter():
    #file_text = open(filename)
    word_count = {}

    for line in open(filename): #loops through each line in the file
        line = line.strip()
        words = line.split(" ") #stores each word in a list

        for word in words: #loops through each word in the list 
            word = word.lower() #makes all words lowercase
            if word.endswith(',') or word.endswith('?') or word.endswith('.'):
                word = word[0:len(word) -1]
            word_count[word] = word_count.get(word, 0) + 1

    for key, value in word_count.items(): #loops through and prints out the key and its value
        print("{} {}".format(key, value))


word_counter()
##word_counter('test.txt')
# word_counter("twain.txt")