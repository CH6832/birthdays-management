#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Add birthday entries into database
"""

from flask import Flask, redirect, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)

# adding configurations and create SQLAlchemy instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birthdays_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
birthdays_db = SQLAlchemy(app)
migrate = Migrate(app, birthdays_db)

with app.app_context():
    birthdays_db.create_all()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

class UserModel(birthdays_db.Model):
    """User model for name and birthday data"""
    # name = request.form["name"]
    name = birthdays_db.Column(birthdays_db.String(20), unique=False, nullable=False, primary_key=True)
    # year
    year = birthdays_db.Column(birthdays_db.Integer, nullable=False)
    # month = request.form["month"]
    month = birthdays_db.Column(birthdays_db.Integer, nullable=False)
    # day = request.form["day"]
    day = birthdays_db.Column(birthdays_db.Integer, nullable=False)


    def __repr__(self):
        return f"Name : {self.name}, Year: {self.year} Month: {self.month}, Day: {self.day}"

@app.route("/",)
def index():
    """Generate updated template"""
    rows = UserModel.query.all()
    return render_template("index.html", rows=rows)

@app.route('/add', methods=["POST"])
def profile():
    """Add data inserted by user"""
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")
    year = request.form.get("year")

    if name != '' and year is not None and month is not None and day is not None:
        user_profile = UserModel(name=name, year=year, month=month, day=day)
        birthdays_db.session.add(user_profile)
        birthdays_db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

@app.route('/delete/<string:name>', methods=["POST"])
def delete_birthday(name):
    """Delete birthday entry"""
    user_profile = UserModel.query.get(name)
    if user_profile:
        birthdays_db.session.delete(user_profile)
        birthdays_db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()

