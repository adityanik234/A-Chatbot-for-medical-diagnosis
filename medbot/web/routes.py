from web import app
from flask import render_template, redirect, url_for, flash, request, abort
from web import app, db, bcrypt
from web.forms import RegistrationForms, LoginForm, UpdateProfileForm
from web.models import User
from flask_login import login_user, current_user, logout_user, login_required
from chatbot.chatbot_function import chatbot_response, get_user_intent


@app.route('/')
def home():
    return render_template("home.html")


app.static_folder = 'static'


@app.route("/chat")
def chatbot():
    return render_template("index.html")


@app.route("/get")
def get_human_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)

