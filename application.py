from prepare import Prepare_input
from visualise import Visualise  #From file visualise import function Visualise
from bubble_sort import Bubble_sort 
from flask import Flask
from flask import render_template
from flask import request

# from flask import static_url_path

#terminal
#export FLASK_APP=main.py
# flask run

#export FLASK_ENV=development
#flask run
# @app.route("/<var>")


#Taking an input string which will be then numbers that are to be sorted
app = Flask(__name__) #instance of the flask app and call it app
# @app.route("/")
# def home():
#      return render_template("testHTML.html")

#@app.route('/test/')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/data/<input>')
def data_input(input):
    userInput = input
    prepared_data = Prepare_input(userInput)
    
    sorted_result = Bubble_sort(prepared_data)
    #Visualise(sorted_result)
    str_sorted_result = str(sorted_result)

    return ('Sorted result ' + str_sorted_result)


@app.route('/info')
def info():
    return render_template("testHTML.html")


@app.route('/api/data')
def get_data():
    return app.send_static_file("data.json")

#prevents other scripts from running
if __name__ == "__main__":
    app.run(debug=True)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


# def save_visualisation():
#      Visualise(prepared_data)

#     return 






