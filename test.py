import nltk.corpus
import nltk.tag
import nltk
import re
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
class yodify():

    def yodify(s):
       h = nltk.word_tokenize(s)
       b = nltk.pos_tag(h)

       l = len(b)
       # return b[-2]+ b[-1] + tuple(b[l:l-3]+ b[:l-3])
       # print(b)

       for item in b:
           if item[1]== 'PP' :
               word = re.search(item[0],s)
               # print(word.start())
               num = word.start()
               return s[num:]+ " " +s[:num]
           if len(b) <= 4:
               return ' '.join(h[-1:] + h[:len(b)-1])

           else:
               return ' '.join(h[-3:] + h[:-3])
                # return h[-3:] + h[:-3]
               # return h[-3:] + " " + h[-2:] + " " + h[-1:]+ " " + str(h[l:l - 3]) + " " + str(h[:l - 3])


    s= "the dog ate the food bowl"
    y = "I like to go to the beach"
    i = "He spoke to Beck and Evan"
    j = "the dog is in the house"
    r = "The quick brown fox jumps over the lazy dog"
    g = "When I was little I had a car door slammed shut on my hand"
    u = "I like dogs"
    x = "My name is Beck"



    print(yodify(i))
    print(yodify(y))
    print(yodify(j))
    print(yodify(s))
    print(yodify(r))
    print(yodify(u))
    print(yodify(x))