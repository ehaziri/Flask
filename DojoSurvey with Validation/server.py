from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"

    if len(request.form['name']) < 1 or len(request.form['comment']) < 1:
        flash("The Name and Comment fields should not be blank.")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comment should not be longer than 120 characters.")
        return redirect('/')
    else:
        session['fname'] = request.form['name']
        session['flocation'] = request.form['location']
        session['flanguage'] = request.form['language']
        session['fcomment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def res():
    return render_template("result.html", name = session['fname'], location = session['flocation'], language = session['flanguage'], comment = session['fcomment'])


app.run(debug=True)
