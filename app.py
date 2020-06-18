import os
from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request, abort, flash, session
from flask_sqlalchemy import SQLAlchemy
import webbrowser
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from random import randrange
from forms import RegistrationForm, Login, AdminLogin
from database import db, Register, Admin

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()

db.init_app(app)

@app.route("/")
@app.route("/home")
def home():
    # Za napraviti admina
    #admin = Admin(email='neki@email.com', password=generate_password_hash('nekakvalozinka'))
    #db.session.add(admin)
    #db.session.commit()
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='Gallery')

@app.route("/prijava", methods=['GET', 'POST'])
def prijava():
    login = Login()
    if request.method == 'GET':
        return render_template("login.html", login=login)
    elif request.method == 'POST':
        if login.validate_on_submit():
            user = Register.query.filter_by(email=login.email.data).first()
            if user:
                if check_password_hash(user.password, login.password.data):
                    session['user'] = user.email
                    flash(f'Dobrodošli {user.name}!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash(f'Pogrešan email ili lozinka!', 'danger')
                    return redirect(url_for('prijava'))
            else:
                flash(f'Korisnik ne postoji', 'danger')
                return redirect(url_for('prijava'))
        elif not login.validate_on_submit():
            flash(f'Nešto ste krivo upisali!', 'danger')
            return redirect(url_for('prijava'))

@app.route('/admin-prijava', methods=['GET', 'POST'])
def admin_prijava():
    adminLogin = AdminLogin()
    if request.method == 'GET':
        return render_template('admin-login.html', adminLogin=adminLogin)
    elif request.method == 'POST':
        if adminLogin.validate_on_submit():
            admin = Admin.query.filter_by(email=adminLogin.email.data).first()
            #return str(admin)
            if admin:
                if check_password_hash(admin.password, adminLogin.password.data):
                    session['admin'] = admin.email
                    flash(f'Dobrodošao Admin!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash(f'Pogrešan email ili lozinka!', 'danger')
                    return redirect(url_for('admin_prijava'))
            else:
                flash(f'Korisnik ne postoji', 'danger')
                return redirect(url_for('admin_prijava'))
        elif not adminLogin.validate_on_submit():
            flash(f'Nešto ste krivo upisali!', 'danger')
            return redirect(url_for('admin_prijava'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/korisnici" ,methods=['GET'])
def korisnici():
    if request.method == 'GET':
        svi_korisnici = Register.query.all()
        return render_template('korisnici.html', svi_korisnici=svi_korisnici)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('register.html', title='Register', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            ime=form.name.data
            prezime=form.surname.data
            email=form.email.data
            spol=form.gender.data
            password=form.password.data
            try:
                temp = Register(name=ime, surname=prezime, email=email, password=generate_password_hash(password), spol=spol)
                db.session.add(temp)
                db.session.commit()
                flash(f'Dobro došli {form.name.data}!', 'success')
                return redirect(url_for('home'))
            except:
                db.session.rollback()
                flash(f'Pogreška!', 'danger')
                return redirect(url_for('register'))
        elif not form.validate_on_submit():
            flash(f'Nešto ste krivo upisali!', 'danger')
            return redirect(url_for('register'))
    
if __name__ == '__main__':
    app.run(debug=True)