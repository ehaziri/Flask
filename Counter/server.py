from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def counter():
    try:
        session['nr']
    except:
        session['nr'] = 0
    session['nr'] += 1
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    session['nr']+=1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['nr'] = 0
    return redirect('/')

app.run(debug=True)
