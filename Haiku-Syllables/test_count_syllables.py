import sys
import counting_haiku_syllables

with open('Haiku-Syllables\\train.txt') as in_file:
    words=set(in_file.read().split())

missing=[]

for word in words:
    try:
        num_syllables=counting_haiku_syllables.count_syllables(word)
        print(word, num_syllables, end='\n')
    except KeyError:
        missing.append(word)
print("Missing words:",missing, file = sys.stderr)