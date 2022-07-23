from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sosualfred:snakeeyes1996@localhost:5432/foo'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

# db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello World {}'.format(person.name)




if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5002)