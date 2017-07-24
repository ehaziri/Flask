from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/', methods=["POST", "GET"])
def index():
    rand = random.randrange(0,101)
    session['someKey'] = rand
    print session['someKey']
    return render_template('index.html')
@app.route('/guess', methods=["POST"])
def guess():
    box="kuti"
    color=""
    text=""
    inputi = int(request.form['inputi'])

    if (inputi < session['someKey']):
         color="red"
         text="Too low!"

    elif (inputi > session['someKey']):
          color="red"
          text="Too big!"

    elif (inputi == session['someKey']):
          return render_template('win.html')
          session.pop('someKey')



    return render_template('index.html', box=box, color=color, text=text)


app.run(debug=True)
