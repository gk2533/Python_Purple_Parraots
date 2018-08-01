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
   print(b)
   for item in b:
       if item[1]== 'IN' :
           word = re.search(item[0],s)
           # print(word.start())
           num = word.start()
           return s[num:]+ " " +s[:num]
       if item[1] == 'TO':
           word_ = re.search(item[0], s)
           # print(word.start())
           n = word_.start()
           return s[n:] + " " + s[:n]
       else:
           item[1]
           # if(tag == 'IN'):
           #   return b[-3]+ b[-2] +b[-1] + tuple(b[l:l-3]+ b[:l-3])
           # else:
           #     return b[-2] + b[-1] + tuple(b[l:l - 3] + b[:l - 3])



s= "the dog ate the food bowl"
y = "I like to go to the beach"
i = "He spoke to Beck and Evan"
j = "the dog is in the house"



print(yodify(i))
print(yodify(y))
print(yodify(j))
print(yodify(s))
