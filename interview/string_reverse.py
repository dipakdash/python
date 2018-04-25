#!/usr/bin/python

#Set 3:
#Q1:
#Given a string:
#"The quick brown fox jumps over the lazy dog to catch the chicken, and their lay the dog , and here lay the fox and here lay the chicken."
#a) Reverse the sentence e.g. output: chicken the lay here and , dog the lay there , dog lazy the over jumps fox brown quick The.
#b) Reverse the order of letters in each of the words in sentence  e.g. output:  ehT kciuq mworb xof spmuj revo eht.......

def string_reverse():
    my_string = "The quick brown fox jumps over the lazy dog to catch the chicken, and their lay the dog , and here lay the fox and here lay the chicken."
    print(my_string)
    print(my_string[::-1])
    print(" ".join(my_string.split()[::-1]))
    print(" ".join([word[::-1] for word in my_string.split()]))


if __name__ == "__main__":
    string_reverse()