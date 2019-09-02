from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cfaa54ba35133fedf8cce33ad2527e68'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
