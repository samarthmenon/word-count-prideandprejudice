#Program to list the letters and words from the book Pride and Prejudice
#then list the frequency of them in the text. The program imports functions
#defined in the module Functions. For limits, only words which occur more than
#500 times are being displayed.

import Functions
from operator import itemgetter
f = open("PrideAndPrejudice.txt")
Text = f.read()
LetterFrequency = {}
WordFrequency = {}

#The following code uses CreateList and DictionaryUpdate to create a list then
#updating the associated dictionary. The list of letters is then displayed in
#descending order of their usage.
for a in Text:
    LetterList = Functions.CreateList(a)
    for Letter in LetterList:
        Functions.DictionaryUpdate(Letter,LetterFrequency)

#The dictionary is sorted then reverse to display in descending order.
print "This program displays the letter and words used in Pride and Prejudice, sorted by their amount of usage.\n"
print "The Frequency of Letters is given in the following table:\n"
print "{:<8} {:<15}".format('Letter','Frequency')
for key, value in sorted(LetterFrequency.items(), key=itemgetter(1), reverse=True):
    print "{:<8} {:<15}".format(key,value)

#This portion of the code deals with counting words and displaying them in descending order.
#For limits, displaying has been restricted to words with 500 occurences in the text.
print "\nThe Frequency of Words is given in the following table (Restricted to usage of 500 and above)\n"
print "{:<8} {:<15}".format('Word','Frequency')
Functions.WordCount(Text,WordFrequency)
for key,value in sorted(WordFrequency.items(), key=itemgetter(1), reverse=True):
    if value >= 500:
        print "{:<8} {:<15}".format(key,value)
        
f.close()
raw_input("\nPress Enter to Exit.")
