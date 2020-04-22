#!/usr/bin/python3
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
def pythonic():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def evenodd(n=None):
    if n % 2 == 0:
        numtype = 'even'
        return render_template('6-number_odd_or_even.html', n=n, numtpye)
    else:
        numtype = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, numtype)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
