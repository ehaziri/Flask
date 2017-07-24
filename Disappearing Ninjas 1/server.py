from flask import Flask, request, render_template,redirect, url_for
app = Flask(__name__)

turtles = {'red':'donatello.jpg', 'green':'leonardo.jpg', 'blue':'michelangelo.jpg', 'purple':'raphael.jpg', 'april': 'notapril.jpg'}


@app.route('/ninja', methods = ['GET'])
def index():
    data = turtles
    data.pop('april')
    contents = turtles
    return render_template('index.html', contents = data)

@app.route('/ninja/<turtle>', methods = ['GET'])
def show(turtle):
    data = {}
    if turtle == 'red' or turtle == 'green' or turtle == 'blue' or turtle == 'purple':
        data[turtle] = turtles[turtle]
    else:
        data['april']=turtles['april']
    return render_template('index.html', contents = data)

if __name__ == '__main__':
    app.run(debug=True)


#{{ url_for('static', filename='main.css') }}
