# import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy
import nltk
# import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import nltk
import fields

# simple flask application definition
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

'''
json marshaller (object <-> json)
'''
message = api.model('message', {
    # 'name': fields.String(required=True, description='message title'),
    'content': fields.String(required=True, description='message content'),
})

'''
message_id = api.model('message_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a message'),
    'name': fields.String(required=True, description='message name'),
    'content': fields.String(required=True, description='message content'),
})
'''


def num(bool):
    i = 0
    if bool:
        num.counter += 1
    if not bool:
        i += 1
    return num.counter


num.counter = 1


list = []


def yodify(s):
    s = nltk.word_tokenize(s)
    b = nltk.pos_tag(s)
    l = len(b)
    return b[l:l-3] + b[:l-3]


s = "the dog ate the food bowl"
print(yodify(s))
'''
Rumor object model (Rumor <-> rumor) 
ignore warning as props will resolve at runtime
'''


class Message(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    # name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.content


def create_message(data):
    # id = str(uuid.uuid4())
    # static variable, not a uuid
    # id = str(num.counter)
    # {num(true): 'message'}
    # name = data.get('name')
    content = data.get('content')
    message = Message(id=id, content=content)
    # do we need this?
    dict1 = {num(True): content}
    list.append(dict1)
    db.session.add(message)
    db.session.commit()
    list.append(content)
    return message


'''
API controllers
'''


@api.route("/message")
class MessageRoute(Resource):
    def get(self):
        return list

    # @api.response(201, 'Rumor successfully created.')
    @api.expect(message)
    def post(self):
        create_message(yodify(request.json))


# id is a url-encoded variable
@api.route("/message/<int:id>")
class MessageIdRoute(Resource):
    def get(self, id):
        # use sqlalchemy to get a message by ID
        return list[id]


'''
helper methods (for testing and sqlalchemy configuration)
'''


def configure_db():
    db.create_all()
    db.session.commit()


# for testing only!
def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
# simple flask application definition
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

'''
json marshaller (object <-> json)
'''
message = api.model('message', {
    # 'name': fields.String(required=True, description='message title'),
    'content': fields.String(required=True, description='message content'),
})

'''
message_id = api.model('message_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a message'),
    'name': fields.String(required=True, description='message name'),
    'content': fields.String(required=True, description='message content'),
})
'''


def num(bool):
    i = 0
    if bool:
        num.counter += 1
    if not bool:
        i += 1
    return num.counter


num.counter = 1


list = []


def yodify(s):
    s = nltk.word_tokenize(s)
    b = nltk.pos_tag(s)
    l = len(b)
    return b[l:l-3] + b[:l-3]


s = "the dog ate the food bowl"
print(yodify(s))
'''
Rumor object model (Rumor <-> rumor) 
ignore warning as props will resolve at runtime
'''


class Message(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    # name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.content


def create_message(data):
    # id = str(uuid.uuid4())
    # static variable, not a uuid
    # id = str(num.counter)
    # {num(true): 'message'}
    # name = data.get('name')
    content = data.get('content')
    message = Message(id=id, content=content)
    # do we need this?
    dict1 = {num(True): content}
    list.append(dict1)
    db.session.add(message)
    db.session.commit()
    list.append(content)
    return message


'''
API controllers
'''


@api.route("/message")
class MessageRoute(Resource):
    def get(self):
        return list

    # @api.response(201, 'Rumor successfully created.')
    @api.expect(message)
    def post(self):
        create_message(yodify(request.json))


# id is a url-encoded variable
@api.route("/message/<int:id>")
class MessageIdRoute(Resource):
    def get(self, id):
        # use sqlalchemy to get a message by ID
        return list[id]


'''
helper methods (for testing and sqlalchemy configuration)
'''


def configure_db():
    db.create_all()
    db.session.commit()


# for testing only!
def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()