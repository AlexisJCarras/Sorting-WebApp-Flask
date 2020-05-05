from prepare import prepare_input
from bubble_sort import Bubble_sort 
from sorters import bubble_sort
from flask import Flask, render_template, request, session
from flask_session import Session #data specific to a users interaction


#terminal
#export FLASK_APP=application.py
#export FLASK_ENV=development
#flask run

app = Flask(__name__) #instance of the flask app and call it app

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods = ["GET", "POST"])
def index():

    # if session.get("notes") is None:
    #     session["notes"] = []
    
    # if request.method == "POST":
    #     note = request.form.get("note")
    #     session["notes"].append(note)
    # if request.method == 'POST':
    #     if request.form['submit_button'] == 'Sort':

    #         return render_template("sorting.html")
    return render_template("index.html")

@app.route('/data/<input>')
def data_input(input):
    userInput = input
    prepared_data = prepare_input(userInput)
    
    sorted_result = Bubble_sort(prepared_data)
    #Visualise(sorted_result)
    str_sorted_result = str(sorted_result)

    return ('Sorted result ' + str_sorted_result)

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/hello', methods = ["GET","POST"])#only accept request method POST
def hello():
    if request.method == "GET":
        return "Please submit the form instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name = name)

@app.route('/sort', methods = ["POST"])
def sort():

    if request.method == 'POST': 
        if request.form.get("sort_selection") == "Bubble Sort":
            unsorted = prepare_input(request.form.get("Numbers"))
            sorted_list = bubble_sort(unsorted)

            return render_template("sorting.html", sorted = sorted_list)

    return render_template("sorting.html")






