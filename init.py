from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)

# Secret key
app.config['SECRET_KEY'] = 'a73b5850c104ceb2d0edbb8c6f4aec9e'

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Initialize the database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from errors.handlers import errors 

app.register_blueprint(errors)


import routes
