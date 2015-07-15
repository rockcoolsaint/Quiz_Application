#from flask import *
#from flask.ext.sqlalchemy import SQLAlchemy
#from functools import wraps
#from models import *
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools  import wraps
from models import *

app = Flask(__name__)

app.secret_key = 'my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#create the sqlalchemy object
db = SQLAlchemy(app)

#from models import *

@app.route('/')
def home():
	# return "Hello, Word" # return a string
	#posts = db.session.query(Quiz).all()
	#g.db = connect_db()
	#cur = g.db.execute('select * from posts')
	#posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	#g.db.close()
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('log'))
	return wrap

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You are loggedout')
	return redirect (url_for('log'))

@app.route('/quiz')
@login_required
def quiz():
	quest = db.session.query(Quiz).all()
	return render_template('quiz.html', quest=quest)

@app.route('/admin', methods=['GET','POST'])
@login_required
def admin():
	#"""
	if request.method == "POST":
		question = request.form['question']
		option_1 = request.form['option_1']
		option_2 = request.form['option_2']
		ans = request.form['ans']
		if not question or not option_1 or not option_2 or not ans:
			flash("All fields are required. Please try again.")
			#return redirect(url_for('success'))
			#return render_template('admin.html')

		else:
			quiz = Quiz(question, option_1, option_2, ans)
			db.session.add(quiz)
			#db.session.add(option_1)
			#db.session.add(option_2)
			#db.session.add(ans)
			db.session.commit()
			db.session.close()
			flash('New entry was successfully posted!')
			#return redirect(url_for('success'))
			#"""
	return render_template("admin.html")
	
@app.route('/log', methods= ['GET', 'POST'])
def log():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('quiz'))
	return render_template('log.html', error = error)

#def connect_db():
#	return sqlite3.connect(app.database)

if __name__ == "__main__":
	app.run(debug=True)

