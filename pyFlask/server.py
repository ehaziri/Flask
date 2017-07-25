from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"

    session['name'] = request.form['name']
    session['email'] = request.form['email']

    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html')





# @app.route('/result', methods=['POST'])
# def create_user():
#     print "Got Post Info"
#
#     fname = request.form['name']
#     flocation = request.form['location']
#     flanguage = request.form['language']
#     fcomment = request.form['comment']
#     # email = request.form['email']
#
#     return render_template("result.html", name = fname, location = flocation, language = flanguage, comment = fcomment)

app.run(debug=True)
