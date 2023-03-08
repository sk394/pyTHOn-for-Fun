import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()

def main():
    haiku=load_haiku("Haiku-Syllables\\train.txt")
    exceptions=cmudict_missing(haiku)
    build_dict=input("\nManually build an exceptions dictionary(y/n)? \n")
    if build_dict.lower()=='n':
        sys.exit()
    else:
        missing_words_dict=make_exceptions_dict(exceptions)
        save_exceptions_dict(missing_words_dict)

def load_haiku(filename):
    '''open the training corpus of haiku as a set'''
    with open(filename) as in_file: 
        haiku=set(in_file.read().replace('-',' ').split())
        return haiku
def cmudict_missing(word_set):
    '''find and return words in word set missing from cmudict'''
    exceptions=set()
    for word in word_set:
        word=word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print("\nexceptions:")
    print(*exceptions,sep='\n')
    print("\nNumber of unique words in haiku corpus = {}".format(len(word_set)))
    print("\nNumber of words not in cmudict ={}".format(len(exceptions)))
    membership=(1-(len(exceptions)/len(word_set)))*100
    print("cmudict membership={:.1f}{}".format(membership,'%'))
    return exceptions

            
def make_exceptions_dict(exception_set):
    '''return dictionary of words and counts from a set of words'''
    missing_words = {}
    print("Input # of syllables in word. Mistakes can be corrected at end\n")
    for word in exception_set:
        while True:
            num_sylls = input("Enter a number syllables in {}:".format(word))
            if num_sylls.isdigit():
                break
            else:
                print("    Not a valid answer. ", file=sys.stderr)
        missing_words[word] = int(num_sylls)
    print()
    pprint.pprint(missing_words, width=1)
    print("\nMake changes to Dictionary before saving")
    print("""
    0-Exit & Save
    1-Add a word or change a syllable count
    2-Remove a word """) 
    while True:
        choice=input("\nEnter choice")
        if choice=='0':
            break
        elif choice=='1':
            word=input("\nWord to add or change: ")
            missing_words[word] = int(input("Enter number syllables in {}: ".format(word)))
        elif choice=='2':
            word=input("\nWord to remove: ")
            missing_words.pop(word,None)
    print("\nNew words or syllable change")
    pprint.pprint(missing_words, width=1)
    return missing_words

    
def save_exceptions_dict(missing_words):
    '''save exceptions dictionary as json file'''
    json_string=json.dumps(missing_words)
    f=open('missing_words.json','w')
    f.write(json_string)
    f.close()
    print("\nFile saved as missing_words.json")

if __name__=='__main__':
    main()