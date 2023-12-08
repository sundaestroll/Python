L = input().split() #split method to get string into a list. In this example is to get two input at same time to create a list.
min = int(L[0]) # setting the first enter number aka. min as an integer 
max = int(L[1]) # setting the second enter number aka. max as an integer
# min,max = map (int,input().split()) this could also be a code to use to represent the both
# map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements. 
temp = int(input()) # getting user's input to save on the temperature

while temp != -999: # while loop, the loop contiunes if the temp input is not equal to -999
        if min <= temp <= max: #if statement gets trigger when temp is larger than min and smaller than max
                print("Nothing to report") #first of all it outputs "Nothing to report"
                temp = int(input()) # let the user to re enter the temp input then goes back to the first part (while loop)
        else: # when the temp is either larger than the max or smaller than the min
                print("Alert!") # system output alert!
                break # then break the whole loop as well