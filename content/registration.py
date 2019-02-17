from flask import Blueprint, request, session, redirect, render_template, flash, url_for, g
from database.db import UserTable, db

Registration = Blueprint('registration', __name__, static_folder='./static', template_folder='./template')


@Registration.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        """
        Username and password must be unique
        They will be keywords for login
        """

        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']
        error = None

        user = UserTable.query.filter_by(username=username).first()

        if username == '':
            error = 'Username is required'
        elif age == '':
            error = 'Age is required'
        elif email == '':
            error = 'Email is required'
        elif password == '':
            error = 'Password is required'
        elif user:
            error = 'User is already registered'

        if error == None:
            new_user = UserTable(username, age, email, password)

            db.session.add(new_user)
            db.session.commit()
            return redirect('login')
        flash(error)

        session['email'] = request.form['email']
        session['password'] = request.form['password']
        return redirect('login')
    return render_template('registration.html')


@Registration.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if username == '':
            error = 'Enter your name'
        elif password == '':
            error = 'Enter your password'

        user = UserTable.query.filter_by(username=username).first()

        if user == None:
            error = 'Incorrect username'

        if user.password != password:
            error = 'Incorrect password'
        else:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('content.home'))

        flash(error)
    return render_template('login.html')

@Registration.before_request
def before_request():
    user_id = session.get('user_id')

    if user_id == None:
        g.user = None
    else:
        for user in users:
            if user['id'] == user_id:
                g.user = user
                session.permanent = True

@Registration.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('registration.registration'))
