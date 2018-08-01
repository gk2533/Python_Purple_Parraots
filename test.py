import nltk.corpus
import nltk.tag
import nltk
import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def yodify(s):
   h = nltk.word_tokenize(s)
   b = nltk.pos_tag(h)
   l = len(b)
   # return b[-2]+ b[-1] + tuple(b[l:l-3]+ b[:l-3])
   # print(b)
   for item in b:
       for tag in item:
           print(tag)
           if(tag == 'CC'):
             return b[int(item-1)] + b[int(item)]+ b[int(item+1)] + b[:int(item)-1]




s= "the dog ate the food bowl"
y = "I like to go to the beach"
i = "He spoke to Beck and Evan"



print(yodify(s))
print(yodify(y))
print(yodify(i))
