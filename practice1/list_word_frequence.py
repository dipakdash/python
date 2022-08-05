#!/usr/bin/python3

# Given a string create one word frequency dictionaly and one list of tuples (word, frequency)
# Sort the Dict, Tuple List, and find the highest and lowest word occurrence

string1 = "apple mango apple orange orange apple guava mango mango banana banana apple grape"

word_list = string1.split(" ")
word_list_unique = list(set(word_list))

####################################################################################

# Using own logic

word_dict = {}
word_tuple_list = []

def word_frequency():
    for i in range(len(word_list_unique)):
        count = 0
        for j in range(len(word_list)):
            if word_list_unique[i] == word_list[j]:
                count = count + 1
        word_dict[word_list_unique[i]] = count
        word_tuple_list.append((word_list_unique[i], count))
    print(word_dict)
    print(word_tuple_list)

def sort_frequency_dict():
    # Starting from Python 3.6, dict objects are now ordered by insertion order. It's officially in the specs of Python 3.7. Before that, you had to use OrderedDict.
    sorted_word_dict = dict(sorted(word_dict.items(), key = lambda x: x[1]))
    print(sorted_word_dict)

def sort_frequency_tuple_list():
    sorted_word_tuple_list = sorted(word_tuple_list, key = lambda x: x[1])
    print(sorted_word_tuple_list)

####################################################################################

# Using python count method

word_dict1 = {}
word_tuple_list1 = []

def word_frequency1():
    for word in word_list_unique:
        word_dict1[word] = word_list.count(word)
        word_tuple_list1.append((word, word_list.count(word)))
    print(word_dict1)
    print(word_tuple_list1)

####################################################################################

if __name__ == "__main__":
    word_frequency()
    sort_frequency_dict()
    sort_frequency_tuple_list()

    word_frequency1()

