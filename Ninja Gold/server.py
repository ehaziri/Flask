from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def index():
    session['money'] = 0
    session['farm'] = 0
    session['cave'] = 0
    session['house'] = 0
    session['casino'] = 0
    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():
    money = session['money']
    teksti=""

    if(request.form['building'] == 'farm'):

        rand = random.randrange(10,21)
        print rand
        session['money'] += rand
        session['farm'] += rand
        teksti="Earned", session['farm'], "golds from the farm."

    elif(request.form['building'] == 'cave'):
        rand = random.randrange(5,11)
        print rand
        session['money'] += rand
        session['cave'] += rand
        teksti="Earned", session['cave'], "golds from the cave."

    elif(request.form['building'] == 'house'):
        rand = random.randrange(2,6)
        print rand
        session['money'] += rand
        session['house'] += rand
        teksti="Earned", session['house'], "golds from the house."

    elif(request.form['building'] == 'casino'):
        rand = random.randrange(0,51)
        print rand
        session['money'] -= rand
        session['casino'] += rand
        teksti="Entered a casino and lost", session['casino'], "golds"

    return render_template('index.html', gold=money, komentet=teksti )

app.run(debug=True)
