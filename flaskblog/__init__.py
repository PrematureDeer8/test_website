from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_bcrypt import Bcrypt;
from flask_login import LoginManager;

app = Flask(__name__);
app.config['SECRET_KEY'] = 'a26f4e9d2f5bc6160538a8101a3bf566';
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db";
db = SQLAlchemy(app);
bcrypt = Bcrypt(app);
login_manager = LoginManager(app);

from flaskblog import routes;