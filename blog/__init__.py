from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '734a53fd01858fdbbacdf3fceebbbc1b441296019df78bbc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2037820:Zhengyi123456@csmysql.cs.cf.ac.uk:3306/c2037820_myblog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from blog import routes