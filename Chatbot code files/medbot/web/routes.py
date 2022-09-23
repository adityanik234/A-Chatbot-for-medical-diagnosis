from web import app
from flask import render_template, redirect, url_for, flash, request, abort
from web import db, bcrypt
from web.forms import RegistrationForms, LoginForm, UpdateProfileForm
from web.models import User
from flask_login import login_user, current_user, logout_user, login_required
from chatbot.chatbot_function import chatbot_response, get_user_intent


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForms()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('You have done Great', 'Success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('you logged in successfully ', 'success')
            # return redirect(url_for('home'))
            return redirect(next_page if next_page else url_for('home'))
        else:
            flash('Your email or your password is incorrect', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you logged Out', 'success')
    return redirect(url_for('home'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('account updated', 'info')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('profile.html', form=form)


app.static_folder = 'static'


@app.route("/chat")
def chatbot():
    return render_template("index.html")


@app.route("/get")
def get_human_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)
