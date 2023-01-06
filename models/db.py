from flask_mongoengine import MongoEngine
from decouple import config

database_name="userinfo"
password="aXEOI75eMSchXUNj"
DB_URI="mongodb+srv://admin:{}@userinfo.wtnrcuz.mongodb.net/{}?retryWrites=true&w=majority".format(password,database_name)

db=MongoEngine()
db.connect(db=database_name,username='admin',password=password,host=DB_URI)

def initialize_db(app):
    db.init_app(app)