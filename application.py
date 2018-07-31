import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy
import re
import nltk

# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
# simple flask application definition

application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

'''
json marshaller (object <-> json)
'''
rumor = api.model('rumor', {
    'name': fields.String(required=True, description='rumor title'),
    'content': fields.String(required=True, description='rumor content'),
})

rumor_id = api.model('rumor_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a rumor'),
    'name': fields.String(required=True, description='rumor name'),
    'content': fields.String(required=True, description='rumor content'),
})


'''
Rumor object model (Rumor <-> rumor) 
ignore warning as props will resolve at runtime
'''


class Rumor(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Rumor %r>' % self.content


def create_rumor(data):
    id = str(uuid.uuid4())
    name = data.get('name')
    content = data.get('content')
    rumor = Rumor(id=id, name=name, content=content)
    db.session.add(rumor)
    db.session.commit()
    return rumor


'''
API controllers
'''


@api.route("/rumor")
class RumorRoute(Resource):
    def get(self):
        return {'brandon': 'listens to selena gomez'}

    # @api.response(201, 'Rumor successfully created.')
    @api.expect(rumor)
    @api.marshal_with(rumor_id)
    def post(self):
        new_rumor = create_rumor(request.json)
        return Rumor.query.filter(Rumor.id == new_rumor.id).one()


# id is a url-encoded variable
@api.route("/rumor/<string:id>")
class RumorIdRoute(Resource):
    @api.marshal_with(rumor_id)
    # id becomes a method param in this GET
    def get(self, id):
        # use sqlalchemy to get a rumor by ID
        return Rumor.query.filter(Rumor.id == id).one()


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