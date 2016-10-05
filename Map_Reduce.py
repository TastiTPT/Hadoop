# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:26:11 2016

@author: nicolas
"""

############## The Map / Reduce Function #########################

# Functions implementation #

def map(line): # Take a line in input 
    to_withdraw = [",","?","!",".","\n"] # punctuation and "\n" to withdraw
    group = []   # initialisation of a empty group
    words = line.split(" ") # split line by word
    for word in words:
        for w in to_withdraw: # loop to withdraw all punctuation
            word = word.rstrip(w).lstrip(w).lower() # lower to avoid cast
        key_value = dict()  # initialisation of a new dictionnary
        key_value[word] = 1 # map value 1 to key word
        group.append(key_value) # add the pair of (key and its value) to the group

    return group # output: a list containing dictionnary

def reduce(dic): # take a dictionnary in input
    count = sum(list(dic.values())[0]) # sum values of the key
    key = list(dic.keys())[0] # getting the key
    return {key:count} # output: a dictionnary returning the key and the count as value
    
# test map #
print("Test map: ")
test_1 = "Map function test!"
print("the sentence for the test is: "+str(test_1))
print(map(test_1))
print("\n")

# test reduce #
print("Test reduce")
test_2 = {"reduce":[1,1,1,1]}
print("the input for test reduce is: ")
print(test_2)
print("the output for reduce function is: ")
print(reduce(test_2))

    
##################################################################
    
    
    
    
    
######################### Bonus ################################## 
    
# Functions implementation #
    
def reader(text_file): # Input: a text file
    lines = []
    for line in text_file:
        lines.append(line)
    return lines # output: liste containing all lines
     
def sort_and_shuffle(list_of_list) :
    new_groups = dict()
    for l in list_of_list:
        for dic in l:
            k = list(dic.keys())[0] # getting key
            if(k not in list(new_groups.keys())): # check if the dictionnary for this key already exists
                new_groups[k] = {k:list(dic.values())} # create dictionnary
            else: 
                list(new_groups[k].values())[0].append(list(dic.values())[0]) # add the value at the list of value 
                
    keys = sorted(new_groups.keys()) # sort key in alphabetic order
    result = dict()
    for k in keys:
        result[k] = new_groups[k]
    return result

def count(text_file): # the main function to do all the algorithm
    # reader step
    lines = reader(text_file)
    groups = []

    # map step
    print("$$$ map Step $$$")
    print("\n")
    for line in lines:
        group = map(line)
        print("a group after map step:")
        print(group)
        print("\n")
        groups.append(group)
    print("\n")
    
    # sort and shuffle step
    print("$$$ Sort and Shuffle Step $$$")
    print("\n")
    groups = sort_and_shuffle(groups)


    
    # reduce step
    print("$$$ reduce step $$$")
    print("\n")
    result_reducer = []
    for key in sorted(groups.keys()):
        print("a group before reduce step")
        print(groups[key])
        dic = reduce(groups[key])
        print("a group after reduce step")
        print(dic)
        result_reducer.append(dic)
        print("\n")
        
    # final output
    print("output:")
    return result_reducer
    
        
# test count MapReduce
text = open('text_file_test.txt','r')


print("\n")
print("\n")
print("Test all MapReduce:")
print("\n")
print(count(text))

###################################################################

