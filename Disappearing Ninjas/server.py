from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html', tekst="No ninjas here.")

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def ninjas(color):
    if color == "blue":
        return render_template('index.html', imazhi="img/donatello.jpg", tekst="")
    elif color == "orange":
        return render_template('index.html', imazhi="img/michelangelo.jpg", tekst="")
    elif color == "red":
        return render_template('index.html', imazhi="img/raphael.jpg", tekst="")
    elif color == "purple":
        return render_template('index.html', imazhi="img/leonardo.jpg", tekst="")
    else:
        return render_template('index.html', imazhi="img/notapril.jpg", tekst="")

app.run(debug=True)
