from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt #lets us encrypt
import json #lets us read json
import requests # lets us send HTTP requests using Python.
from datetime import datetime #lets us use datetime for getting times and dates and using those methods
from functools import wraps #lets us use decorators to confirm things before function gets processed 
import database #gets import for sqlite3, and any other db stuff.

app = Flask(__name__)

app.debug=True

@app.route('/')
def index():
	body = 'home'
	return render_template('home.html', body = body)


#user login
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		#get form fields
		username = request.form['username']
		password_candidate = request.form['password']

		#create cursor
		cur = mysql.connection.cursor()

		#get user by username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		#by using fetchone, we don't have to say LIMIT 1 in this query

		if result > 0:
			#get stored hash - fetchone as a method only gets the first match.
			#this means usernames should be unique
			data = cur.fetchone()
			password = data['password']

			#compare passwords
			if sha256_crypt.verify(password_candidate, password):
				app.logger.info('password match')
				#passed
				session['logged_in'] = True #just like PHP
				session['username'] = username 

				flash('you are now logged in', 'success')
				return redirect(url_for('dashboard'))
			else:
				app.logger.info('no password match')	
				error = 'invalid login'
				return render_template('login.html', error=error)		
			#close connection
			cur.close()		
		else:
			error = 'Username not found'
			return render_template('login.html', error=error)		

	return render_template('login.html')

#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, please login', 'danger')
			return redirect(url_for('login'))
	return wrap		

@app.route('/dashboard')
@is_logged_in
def dashboard():
	return render_template('dashboard.html')		


@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out.', 'success')
	return redirect(url_for('login'))


if __name__ == '__main__':
#	 app.secret_key = secretKey() #make a better secret key and put this in creds.
	 app.run(); #host and port can be added into parameters