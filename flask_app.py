from flask import Flask, request, render_template, flash, redirect,url_for
from users import create_user, verify_user
# import datetime
import git

app = Flask(__name__)

app.config['SECRET_KEY'] = 'TGvPeixXUFWhg83Gk59UAs5o9C3PQH3I'


messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'},
             {'title': 'Message Three',
             'content': 'Message Three Content'}
            ]

@app.route('/adduser')
def add_user():
    print(request.url)  # request.url property
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    email = request.args.get('email')
    password = request.args.get('password')
    return create_user(firstname, lastname, email, password)

@app.route('/api/login')
def get_user_by_password():
    password = request.args.get('password')
    email = request.args.get('email')
    return verify_user(password, email)


@app.route('/')
def home_page():
    return render_template('./index.html',  messages=messages)


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    return render_template('comments.html')


@app.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        if not email:
            flash('email is required!')
        elif not password:
            flash('password is required!')
        else:
            messages.append({'title': email, 'content': password})
            return redirect(url_for('home_page'))

    return render_template('login.html')

@app.route('/api/git', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/hubertchen200/mysite')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
    return "Get"

