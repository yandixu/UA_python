'''
    File: rhymes-oo.py
    
    Author: Yandi Xu
    
    Purpose: This program is used to find all words on an input filethat
             rhyme with some given input word.

'''

import sys

class Word:
    '''This class is used to represent a word.

    Attributes: self._word: a string that makes up the word.
                self._pronu: a collection of pronuciations for the word.
    '''

    def __init__(self, line):
        elem = line.strip().split()
        self._word  = elem[0].lower()
        self._pron =[elem[1:]]

    def update(self, line):
        '''if the word object has existed, add the new pronunciation to the list

        Parameters: line: the line in the file
        '''
        pron = line.strip().split()[1:]
        self._pron.append(pron)

    def get_word(self):
        '''get the word'''
        return self._word

    def get_pron(self):
        '''get the pronuciations of the word'''
        return self._pron

    def _find1(self):
        '''check the pronuciations of the word and find where is the
        primary stress，store the index in the list

        Return: indexes: a list with the index of the primary stress
        '''
        indexes = []
        for pron in self._pron:
            for i in range(len(pron)):
                if pron[i][-1] == '1':
                    indexes.append(i)

        return indexes

    def __eq__(self, other):
        '''compare if the two word object has the same rhymes'''
        indexes1 = self._find1()
        indexes2 = other._find1()
        
        for i in range(len(indexes1)):
            for j in range(len(indexes2)):
                if self._pron[i][indexes1[i]:] == other._pron[j][indexes2[j]:]:
                    
                    if indexes1[i]-1 >= 0 and indexes2[j]-1 >= 0:
                        if self._pron[i][indexes1[i]-1] != other._pron[j][indexes2[j]-1]:
                            
                            return True
                    elif indexes1[i]-1 >= 0:                       
                        return True
                    elif indexes2[j]-1 >= 0:
                        return True
        return False
        
    def __str__(self):
        return self._word + ' : ' + str(self._pron)
        

class WordMap:
    '''this class is used tor epresent data structures and methods
        to associate words with the corresponding Word objects.

    Attributes:
        self._word_dic, a dictionary whose key is the word string
                    and the value is the word object.
    '''
    
    def __init__(self):
        self._word_dic = {}

    def read_dic(self):
        '''this method is to read the file and store the words and
        their pronunciations in the sictionary'''
        fname = input()

        #try if the input file exist.
        try:        
            file = open(fname)
        except IOError:
            print("ERROR: Could not open file " + fname)
            sys.exit(1)

        lines = file.readlines()
        for line in lines:
            line = line.strip()
            word = Word(line)
            word_str = line.split()[0].lower()
            
            if word_str not in self._word_dic.keys():
                self._word_dic[word_str] = word
            else:
                self._word_dic[word_str].update(line)
        file.close()

    def input_word(self):
        '''this method is to read the word and check which words rhymes with it.'''
        word = input().lower()

        #try if word exist in the dictionary.
        try:
            assert word in self._word_dic
        except AssertionError:
            print("ERROR: the word input by the user is not in the pronunciation dictionary " + word)
            exit(1)
            
        for k, v in self._word_dic.items():
            if word != k and self._word_dic[word] == v:
                print(k)

    def __str__(self):
        return self._word_dic

def main():
    #build the wordmap object, read the dictionary file and input the word.
    
    words = WordMap()
    words.read_dic()
    words.input_word()

main()
            
