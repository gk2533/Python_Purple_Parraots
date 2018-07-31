# import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy

# simple flask application definition stupid
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

'''
json marshaller (object <-> json)
'''
message = api.model('message', {
    'name': fields.String(required=True, description='message title'),
    'content': fields.String(required=True, description='message content'),
})

message_id = api.model('message_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a message'),
    'name': fields.String(required=True, description='message name'),
    'content': fields.String(required=True, description='message content'),
})

def num():
    num.counter += 1
    return num.counter

num.counter = 0

'''
Rumor object model (Rumor <-> rumor) 
ignore warning as props will resolve at runtime
'''


class Message(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.content


def create_message(data):
    # id = str(uuid.uuid4())
    # static variable, not a uuid
    name = data.get('name')
    content = data.get('content')
    message = Message(id=id, name=name, content=content)
    db.session.add(message)
    db.session.commit()
    return message


'''
API controllers
'''


@api.route("/message")
class MessageRoute(Resource):
    def get(self):
        return {'brandon': 'listens to selena gomez'}

    # @api.response(201, 'Rumor successfully created.')
    @api.expect(message)
    @api.marshal_with(message_id)
    def post(self):
        new_message = create_message(request.json)
        return Message.query.filter(Message.id == new_message.id).one()


# id is a url-encoded variable
@api.route("/message/<string:id>")
class MessageIdRoute(Resource):
    @api.marshal_with(message_id)
    # id becomes a method param in this GET
    def get(self, id):
        # use sqlalchemy to get a rumor by ID
        return Message.query.filter(Message.id == id).one()


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