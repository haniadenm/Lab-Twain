# put your code here.
import sys

# import fileinput
# for line in fileinput.input():
#     process(line)
print("Filename = ", sys.argv[1])


def word_count(file):
    input_file = open(file)
    word_count = {}
    for line in input_file:

        words = line.split()
        for word in words:
            word.strip()
            word_count[word] = word_count.get(word, 0) + 1
    input_file.close()

    for key, value in word_count.items():
        print(f"{key} {value}")


def word_count_strip_punctuation(file):
    input_file = open(file)
    word_count = {}
    for line in input_file:

        words = line.split()
        for word in words:
            word = word.lower()
            word = word.strip()
            word = word.strip(',.?')
            word_count[word] = word_count.get(word, 0) + 1
    input_file.close()

    for key, value in word_count.items():
        print(f"{key} {value}")


print("***************")
word_count(sys.argv[1])
print("***************")
word_count_strip_punctuation(sys.argv[1])


def count_using_collections(file):
    input_file = open(file)
    count_collections = {}
    # Need to change the code below to read in the file in one string,
    # and then split, then use a collections object and the method .count()
    # passing it the  word_count dictionary.

    # for line in input_file:
    #     words = line.split()
    #     for word in words:
    #         word = word.lower()
    #         word = word.strip()
    #         word = word.strip(',.?')
    #         count_collection[word] =
