from flask_app import app
from flask import render_template,request,redirect,flash, session
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas


@app.route('/')
def index():
    return redirect('/dashboard')

@app.route("/dashboard")
def all_dojos():
    dojo = {
        "id":id
       }
    dojos = Dojos.ninja_with_dojo(dojo)
    return render_template("index.html", dojos = dojos)

@app.route('/add_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojos.add_dojo(data)
    return redirect("/")

@app.route("/show_dojo/<int:id>")
def show_dojo(id):
    data = {
        "id":id
    }
    dojo = Dojos.dojo_with_ninjas(data)
    return render_template("dojo_show.html", dojo=dojo)

@app.route("/ninjas/new")
def new_ninja():
    
    return render_template("new_ninja.html")

@app.route('/add_ninja', methods=["POST"])
def create_ninja():    
    data = {
        "name":request.form ["dojo.name"],
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }
    dojo_id =  request.form['dojo_id']
    Ninjas.add_ninja(data)
    return redirect("/show_dojo")