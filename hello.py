from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/login/')
@app.route('/login/<name>', methods=['GET', 'POST'])
def login(name=None):
    if request.method == 'POST':
        return 'Post login'
    else:
        return render_template('login.html', name=name)

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('hello_world', param='aaa'))
    print(url_for('profile', username='Hiden'))
    print(url_for('static', filename='css/style.css'))
    print(url_for('static', filename='js/app.js'))