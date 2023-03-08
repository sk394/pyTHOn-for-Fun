'''we are generating an algorithm to count the syllables in a haiku'''
import sys
from string import punctuation
import json
from nltk.corpus import cmudict 

#load dictionary of words in haiku corpus but bot not in cmudict
with open('Haiku-Syllables\\missing_words.json') as f:
    missing_words=json.load(f)

cmudict=cmudict.dict()

def count_syllables(words):
    '''use corpora to count syllables in English word or phrase'''
    words= words.replace('-',' ').lower().split()
    num_sylls =0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word in missing_words:
            num_sylls += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_sylls += 1
    return num_sylls

def main():
    while True:
        print("Syllable Counter")
        word = input("Enter a word or phrase, else press Enter to quit: ")
        if word =='':
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print(f"number of syllables in {word} is {num_syllables}")
            print()
        except KeyError:
            print(f"Sorry, {word} is not in the dictionary", file=sys.stderr)
            print()
if __name__ == '__main__':
    main()