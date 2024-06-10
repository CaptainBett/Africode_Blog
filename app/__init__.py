
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import  Mail



app = Flask(__name__)
app.config['SECRET_KEY'] = '3f7927fd62f53d171e842d8dfc31d54b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'enockbett427@gmail.com'
app.config['MAIL_PASSWORD'] = 'rfyr iqxi xtfu ikhy'

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


mail = Mail(app)

from app import routes