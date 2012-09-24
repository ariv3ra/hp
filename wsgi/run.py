import os
from flask import Flask
from flask import render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

#Build the varibles that use the assigned environment variables
HOST = os.environ['OPENSHIFT_NOSQL_DB_HOST']
PORT = int(os.environ['OPENSHIFT_NOSQL_DB_PORT'])
DB_USER = os.environ['OPENSHIFT_NOSQL_DB_USERNAME']
DB_PWD = os.environ['OPENSHIFT_NOSQL_DB_PASSWORD']
DB_NAME = 'hp' #data base name

app.config['MDB_HOST'] = HOST
app.config['MDB_PORT'] = PORT
app.config['MDB_USERNAME'] = DB_USER
app.config['MDB_PASSWORD'] = DB_PWD
app.config['MDB_DBNAME'] = DB_NAME

mdb = PyMongo(app, config_prefix='MDB')

@app.route("/")
@app.route("/index")
def index():
    title = {"first":"Tutorial 01-Flask-Pymongo extension","second":"Tutorial 02"}
    #users = ["Angel","Kristin","Etienne"]
    
    users = mdb.db.users.find({})
    
    conn = "Connected successfully"

    return render_template("index.html",title = title,users = users,conn = conn)


if __name__ == "__main__":
    app.run(debug = "True")
