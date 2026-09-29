import os, secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ubcandle_db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ubcandledb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password><username>.mysql.pythonanywhere-services.com/<username>$<database_name>'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ubcf2026_zx3p_user:SIhiJ069BbzU3xteDmnVZoXsqDZiIdrv@dpg-daqafsad0e5s739shl0g-a.oregon-postgres.render.com/ubcf2026_zx3p'
# app.config['SECRET_KEY'] = b'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

print(os.environ.get('DATABASE_URI'))
print(os.environ.get('SECRET_KEY'))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from ubcf import routes, models