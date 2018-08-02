import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy
import nltk.corpus
import nltk.tag
import nltk
import re
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
  pass
else:
   ssl._create_default_https_context = _create_unverified_https_context
#Downloading nessecary tools for nltk
nltk.download('punkt', download_dir='/opt/python/current/app')
nltk.download('averaged_perceptron_tagger', download_dir='/opt/python/current/app')

nltk.data.path.append("/opt/python/current/app")


application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)


message = api.model('message', {
    'post a message here': fields.String(required=True, description='message post a message here'),
})


message_id = api.model('message_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a message'),
    'post a message here': fields.String(required=True, description='message post a message here'),
})


class Message(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    content = db.Column(db.String(120), unique=False, nullable=False)


def __repr__(self):
    return '<Message %r>' % self.content


def yodify(s):  # takes in a string/sentence
    h = nltk.word_tokenize(s)  # converting every word in the sentence into list
    b = nltk.pos_tag(h)  # tagging every word in list with what type of word it is ( noun, verb,etc.)
    # b is a list of tupples. the tupples are in the format of ( "word", "tag")
    for item in b:  # going through each tupple in the list
        if item[1] == 'PP':  # searching if any word is tagged as a preposition( PP)
            word = re.search(item[0], s)
            num = word.start()
            return str(s[num:] + " " + s[:num])
        if len(b) <= 4:  # for sentences that have 4 or less words
            return str(' '.join(h[-1:] + h[:len(b)-1]))
        else:
            return str(' '.join(h[-3:] + h[:-3]))  # if sentence bigger than 4
            # words has no prep, return the last 3 words in front of the sentence


def dog(sentence):  # changes all the words in the sentence to "woof"
    tokens = nltk.word_tokenize(sentence)
    i = 0
    str = ''
    while i < len(tokens):
        str += 'woof '
        i += 1
    return str


def cookie(sentence):  # all "my"s and "I"s and "My"s change to "me" and "cookie" is inserted every other word
    tokens = nltk.word_tokenize(sentence)
    str = ''
    for word in tokens:
        if word == 'my' or word == 'I' or word == 'My':
            str += 'me cookie '
        else:
            str += word + ' cookie '
    return str


def kermit(sentence):  # all instances of the word "commit" and turns to "kermit" and "Commit" to "Kermit"
    tokens = nltk.word_tokenize(sentence)
    str = ''
    for word in tokens:
        if word == 'commit':
            str += 'kermit '
        elif word == 'Commit':
            str += 'Kermit '
        else:
            str += word + ' '
    return str


def british(sentence):  # talking like Daniel
    tokens = nltk.word_tokenize(sentence)
    str = ''
    for index in tokens:
        if index == 'color':
            str += 'colour '
        elif index == 'favorite':
            str += 'favourite '
        elif index == 'labor ':
            str += 'labour '
        elif index == 'tv':
            str += 'telly '
        elif index == 'line':
            str += 'queue '
        else:
            str += index + ' '

    str += 'mate'
    return str


message_list = []  # creates a list, and later this list will have all the messages in it


def create_message(data):  # this creates the messages, this method is called in the post method
    id = str(uuid.uuid4())
    content = data.get('post a message here')
    message = Message(id=id, content=content)
    message_list.append(content)
    db.session.add(message)
    db.session.commit()
    return message


@api.route("/messageboard") # this get class returns all the messages
class MessageBoard(Resource):
    def get(self):
        return message_list


@api.route("/message/yoda")
class YodaMessage(Resource):    # this is the yoda post class
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self): # this post method posts a message with yodify, calls create_message method
        result = {'post a message here': yodify(request.get_json().get('post a message here'))}
        new_message = create_message(result)
        return Message.query.filter(Message.id == new_message.id).one()


@api.route("/message/dog")
class DogMessage(Resource):     # this is the dog post class
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self): # this post method posts a message with dog
        result = {'post a message here': dog(request.get_json().get('post a message here'))}
        new_message = create_message(result)
        return Message.query.filter(Message.id == new_message.id).one()


@api.route("/message/cookie")
class CookieMessage(Resource):      # this is the cookie post class
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self):     # this post method posts a message with cookie
        result = {'post a message here': cookie(request.get_json().get('post a message here'))}
        new_message = create_message(result)
        return Message.query.filter(Message.id == new_message.id).one()


@api.route("/message/kermit")
class KermitMessage(Resource):      # this is the kermit post class
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self):     # this post method posts a message with kermit
        result = {'post a message here': kermit(request.get_json().get('post a message here'))}
        new_message = create_message(result)
        return Message.query.filter(Message.id == new_message.id).one()


@api.route("/message/british")      # this is the british post class
class BritishMessage(Resource):
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self):     # this post method posts a message with british
        result = {'post a message here': british(request.get_json().get('post a message here'))}
        new_message = create_message(result)
        return Message.query.filter(Message.id == new_message.id).one()


@api.route("/message/<string:id>")
class MessageId(Resource):
    @api.marshal_with(message_id)
    def get(self, id):
        return Message.query.filter(Message.id == id).one()


def configure_db():
    db.create_all()
    db.session.commit()


def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
