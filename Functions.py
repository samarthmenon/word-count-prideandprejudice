#This file contains the functions that are going to be used for
#generating word count and letter frequency in a text file.

#Function to create the list of letters, after which frequency
#of letters will be counted.

def CreateList(text):
    TextString = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    NewText = text.lower()
    #loop to run through the text one character at a time. If it runs into a
    #character not in the alphabets list, it adds a space after then returns the
    #split letters as a list.
    for t in NewText:
        if t in alphabets:
            TextString = TextString + t
        else:
            TextString = TextString + ' '
    return TextString.split()

#This updates the dictionary of letters with the frequency. If the letter
#exists in the list, then it adds 1 to its value. If it doesn't, then it
#initializes with a value of 1.

def DictionaryUpdate(LetterList,LetterFrequency):
    for x in LetterList:
        letter = x.lower()
        if letter in LetterFrequency:
            LetterFrequency[letter]+= 1
        else:
            LetterFrequency[letter] = 1

#This function first splits the text file into seperate words then counts frequency
#with the dictionary used. If not in the dictionary, it initializes with a value of 1.
#Else it adds 1 to the value of the existing word.

def WordCount(Text,WordFrequency):
    for word in Text.split():
        if word not in WordFrequency:
            WordFrequency[word] = 1
        else:
            WordFrequency[word] += 1


    
    
    
