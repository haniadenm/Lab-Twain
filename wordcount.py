# put your code here.
import fileinput
for line in fileinput.input():
    process(line)
    

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
word_count[argv[1]]
print("***************")
# word_count_strip_punctuation("test.txt")
# print("***************")
# word_count("twain.txt")
# print("***************")
# word_count_strip_punctuation("twain.txt")
