import os
from models import db
from routes.applicant import applicant
from dotenv import load_dotenv
from flask import Flask

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db.init_app(app)

app.register_blueprint(applicant)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
