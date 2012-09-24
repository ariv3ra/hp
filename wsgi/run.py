import os
from flask import Flask
from flask import render_template
from pymongo import Connection
from pymongo.errors import ConnectionFailure

HOST = os.environ['OPENSHIFT_NOSQL_DB_HOST']
PORT = int(os.environ['OPENSHIFT_NOSQL_DB_PORT'])
DB_USER = os.environ['OPENSHIFT_NOSQL_DB_USERNAME']
DB_PWD = os.environ['OPENSHIFT_NOSQL_DB_PASSWORD']
DB_NAME = 'hp'

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    title = {"first":"Tutorial 01","second":"Tutorial 02"}
    #users = ["Angel","Kristin","Etienne"]
    c = Connection(host=HOST,port=PORT)
    mdb = c[DB_NAME]
	# Get a Database handler to a database named "mydb"
    mdb.authenticate(DB_USER,DB_PWD)

    assert mdb.connection == c
    users = mdb.users.find({})


    conn = "Connected successfully"

    return render_template("index.html",title = title,users = users,conn = conn)


if __name__ == "__main__":
    app.run(debug = "True")
