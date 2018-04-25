#!/usr/bin/python

#Set 2:
#Q1: 
#Given a sentence
#"The quick brown fox jumps over the lazy dog to catch the chicken, and their lay the dog , and here lay the fox and here lay the chicken."
#a) Give a count of each word and their occurrence , Create a dictionary to store them e.g. output : {'dog' :2 , 'the':4 , 'fox':2 , 'and': 2}
#b) Sort the above dictionary in ascending order of the occurrence count e.g. output  {'dog' :2 , 'fox':2 , 'and':3  , 'the':6 }

def word_frequency():
    my_sentence = "The quick brown fox jumps over the lazy dog to catch the chicken, and their lay the dog , and here lay the fox and here lay the chicken."
    list_words = my_sentence.split()
    dict = {}
    print(list_words)
    
    for word in list_words:
        if word in dict:
            dict[word] = dict.get(word) + 1
        else:
            dict[word] = 1
            
    for k,v in dict.items():
        print(str(k)+':'+str(v))
    
if __name__ == "__main__":
    word_frequency()