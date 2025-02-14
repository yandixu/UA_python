'''
 Author: Yandi Xu

 File: Rhymes.py

 Purpose: This project is used to find the word has same phoneme with the input word.

'''

def main():
    #fname = input()

    fname = 'PronunciationDictionary.txt'
    #open the input file an sread it by lines to a list.
    lines = open(fname).readlines()
    words_dic = create_dic(lines)   
    query,sub_phon,ssub_phon = queries(words_dic)
    print_out(query,sub_phon,ssub_phon,words_dic)

def create_dic(lines):
    """Create a dictionary to store pronunciations of words.
  
    Parameters: lines: a list of words and their pronunciation.
  
    Returns: words_dic: a dictionary store words paired with pronunciation.
  
    Pre-condition: lines is a list
  
    Post-condition: return a dictionary"""
    
    words_dic = {}
    for line in lines:
        #strip and split the line to a list.
        line = line.strip().split()
        #find the word and make it as a key.
        word = line[0]
        if word not in words_dic:
            words_dic[word] = []
            words_dic[word].append(line[1:])
        else:
            words_dic[word].append(line[1:])

    return words_dic

def queries(words_dic):
    """User input word and find the pronunciation of this word in dictioinary.
  
    Parameters: words_dic: a dictionary.
  
    Returns: query: user input.
    
             sub_phon: lists of target phoneme of word.
             
             ssub_phon: 1 syllable longer than the target phoneme.
  
    Pre-condition: words_dic is a dictionary
  
    Post-condition: return 2 strings and 1 list."""

    #create a list to store phoneme incase the query has multiple pronunciation.
    sub_phon = []
    query = input().upper()
    for word in words_dic:
        if query == word:           
            phons = words_dic[word]
            
            for phon in phons:
                for i in range(len(phon)):
                    # if 1 appeared on the syllable, the rest part is traget phoneme.
                    if "1" in phon[i]:
                        index = i
                        # store the pohneme to list.
                        sub_phon.append(phon[index:])
                        # define ssub_phon.
                        if int(index-1) >= 0:
                            ssub_phon = [phon[index-1:]]
                        else:
                            ssub_phon = sub_phon
                        
                        
    return query,sub_phon,ssub_phon


def print_out(query,sub_phon,ssub_phon,words_dic):
    """Print out the words have same stress phoneme wiht query.
  
    Parameters: query: user input.
    
                sub_phon: lists of target phoneme of word.
             
                ssub_phon: 1 syllable longer than the target phoneme.

                words_dic: a dictionary store words paired with pronunciation.
  
    Returns: N/A
  
    Pre-condition: query and ssub_phon are strings, sub_phon is a list, words_dic is a dictionary.
  
    Post-condition: print out the matched words."""
    
    for elem in sub_phon: # target
   
        for word_1 in words_dic:  # key

                    #yin jie
                for phons_1 in words_dic[word_1]:

                    # if the phoneme matched,
                    # and word is not the query one,
                    # and the syllable before target phoneme are not same,
                    # then print out the word.
                    if (elem == phons_1[-len(elem):] and word_1 != query):
                        for i in range(len(ssub_phon)):
                            if ssub_phon[i] != phons_1[-len(elem)-1:]:
                                found = word_1
                                print(found) 
    

main()
