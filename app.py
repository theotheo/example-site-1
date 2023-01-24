from flask import render_template, Flask, request
from flask_frozen import Freezer

import json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    # with open('index.html', 'r') as f:
    #     content = f.read()
    # return content
    return render_template('index.html')

@app.route('/map.html')
def map():
    # with open('map.html', 'r') as f:
    #     content = f.read()
    # return content
    return render_template('map.html')

@app.route('/women.html')
def women():
    return render_template('women.html')


@app.route('/form.html', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        # if request.form['answer'] == "42":
        #     return 'Вы чертовски правы!'
        # else:
        #     return 'Попробуйте еще раз' 

        return render_template('answer.html', answer=request.form['answer'])



@app.route('/channel.html')
def channel():
    with open('result.json', 'r') as f:
        string = f.read()
    data = json.loads(string)
    messages = data['messages']
    return render_template('channel.html', messages=messages)


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()