from flask import Flask
from flask import render_template
from pymongo import Connection
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    title = {"first":"Tutorial 01","second":"Tutorial 02"}
    #users = ["Angel","Kristin","Etienne"]
    c = Connection(host="localhost", port=27018)
    
	# Get a Database handle to a database named "mydb"
    dbh = c["hp"]
    assert dbh.connection == c
    users = dbh.users.find({})


    conn = "Connected successfully"

    return render_template("index.html",title = title,users = users,conn = conn)


if __name__ == "__main__":
    app.run(debug = "True")
