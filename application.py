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

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
nltk.data.load('/english.pickle')
nltk.data.load('/averaged_perceptron_tagger.pickle')

# simple flask application definition stupid
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)


message = api.model('message', {
    # 'name': fields.String(required=True, description='message title'),
    'content': fields.String(required=True, description='message content'),
})


message_id = api.model('message_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a message'),
    # 'name': fields.String(required=True, description='message name'),
    'content': fields.String(required=True, description='message content'),
})


'''def num(bool):
    i = 0
    if bool:
        num.counter += 1
    if not bool:
        i += 1
    return num.counter


num.counter = 1
'''


class Message(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    content = db.Column(db.String(120), unique=False, nullable=False)
    # name = db.Column(db.String(80), unique=False, nullable=False)


def __repr__(self):
    return '<Message %r>' % self.content


def yodify(s):
    h = nltk.word_tokenize(s)
    b = nltk.pos_tag(h)
    for item in b:
        if item[1] == 'PP':
            word = re.search(item[0], s)
            num = word.start()
            return str(s[num:] + " " + s[:num])
        if len(b) <= 4:
            return str(' '.join(h[-1:] + h[:len(b)-1]))
        else:
            return str(' '.join(h[-3:] + h[:-3]))


message_list = []


def create_message(data):
    id = str(uuid.uuid4())
    content = data.get('content')
    message = Message(id=id, content=content)
    message_list.append(content)
    db.session.add(message)
    db.session.commit()
    return message


@api.route("/message/yodi")
class MessageBoard(Resource):
    def get(self):      # @api.route("/<int:id>")
        return message_list

# this works, don't change post method
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self):
        result = {'content': yodify(request.get_json().get('content'))}
        new_message = create_message(result)
        return Message.query.filter(Message.id == new_message.id).one()


# must leave <int:id>
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
