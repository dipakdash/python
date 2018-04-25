#!/usr/bin/python

# How to sort a dict by keys (Python 2.4 or greater):
#    mydict = {'carl':40,
#              'alan':2,
#              'bob':1,
#              'danny':3}
#
#    for key in sorted(mydict.iterkeys()):
#        print "%s: %s" % (key, mydict[key])
#    Results:

#    alan: 2
#    bob: 1
#    carl: 40
#    danny: 3

def sort_dict_by_key_and_value():
    # Sort by key
    mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
    for key in sorted(mydict.keys()):
        print(key + ' : ' + str(mydict[key]))
        
    print("\n")
    #Sort by value using lambda
    for key, value in sorted(mydict.items(), key=lambda x: x[1]):
        print(str(key) + "," + str(value))
    
if __name__ == "__main__":
    sort_dict_by_key_and_value()