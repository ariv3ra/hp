import os
from flask import Flask
from flask import render_template
from flask import request
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

mdb = PyMongo(app, config_prefix='MDB') #Create instance of PyMongo object

@app.route("/")
@app.route("/index")
def index():
    title = {"first":"Tutorial 01-Flask-Pymongo extension","second":"Tutorial 02"}    
    users = mdb.db.users.find({})
    conn = "Connected successfully"
    return render_template("index.html",title = title,users = users,conn = conn)

@app.route("/record", methods=["GET","POST"])
def record():
    users = mdb.db.users.find({})
    return render_template("record.html",users = users)

#route to post data that is associated in the role collection
@app.route("/associate", methods=["GET","POST"])
def associate():    
    uid = request.form['uid'] #Get the data from the user drop down
    lst = request.form['listed']#Get the data from the roles dropdown
    role = {"uid":uid,"role":lst}#Build the document to be saved
    #insert into the mongodb
    mdb.db.role.insert(role)
    #inUser = mdb.db.role.find({}) #Here we need to query the information inserted
    return render_template("associate.html",uid = uid,lst = lst)
    
if __name__ == "__main__":
    app.run(debug = "True")
