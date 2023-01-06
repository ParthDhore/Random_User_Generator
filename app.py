from flask import Flask, Response, request,jsonify, make_response
from models.db import initialize_db
from flask_restful import Api
from routes.route import initialize_routes
from decouple import config

app=Flask(__name__)

password="aXEOI75eMSchXUNj"
db_name='userinfo'
app.config['MONGODB_SETTINGS']={
    "host":"mongodb+srv://admin:{}@userinfo.wtnrcuz.mongodb.net/{}?retryWrites=true&w=majority".format(password,db_name)
}
initialize_db(app)
api=Api(app)
initialize_routes(api)


if __name__=="__main__":
    app.run(debug=True)