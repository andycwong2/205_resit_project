from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
app = Flask(__name__)
app.secret_key = 'development key'

db = pymysql.connect("localhost", "andycwong2", "WCHa21Gra", "205ResitWork")

@app.route("/")
def index():
	if 'username' in session:
		user=session['username']
		ident=session['identity']
		if ident=='teacher':
			return render_template('index_teacher.html',user=user)
		else:
			return render_template('index_student.html',user=user)
	else:	
		return render_template('index.html')

@app.route("/about")
def about():
	if 'username' in session:
		user=session['username']
		ident=session['identity']
		if ident=='teacher':
			return render_template('about_teacher.html',user=user)
		else:
			return render_template('about_student.html',user=user)
	else:	
		return render_template('about.html')

@app.route("/register", methods=['POST','GET'])
def register():
	error = ""
	if request.method == 'POST':
		usrname = request.form['username']
		pwd = request.form['password']
		pwd_cf = request.form['password_c']
		identy = request.form['identity']
		if (usrname or pwd or pwd_cf or identy) =='':
			error="All fields are required."
		elif pwd != pwd_cf:
			error="The password confirmation is invalid."
		else:
			# prepare a cursor object using cursor() method
			cursor = db.cursor()

			# Execute the SQL command
			sql = ("SELECT username FROM userlist")
			cursor.execute(sql)

			# Commit your changes in the database
			db.commit()
			results = cursor.fetchall()
			for i in results:
				if usrname == i[0]:
					error="This username is already exists. Please login."
					break
				else:
					# Execute the SQL command
					sql = ("INSERT INTO userlist(username, password, usertype) VALUES (%s, %s, %s)")
					cursor.execute(sql,(usrname, pwd, identy))

					# Commit your changes in the database
					db.commit()

					return redirect(url_for("reg_confirm"))

	return render_template("register.html",error=error)

@app.route("/reg_confirm")
def reg_confirm():
	return render_template("reg_confirm.html")

@app.route("/loginPage", methods=['POST','GET'])
def login():
	error = ""
	if request.method == 'POST':
		usrname = request.form['username']
		pwd = request.form['password']

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# Execute the SQL command
		sql = ("SELECT username, password, usertype FROM userlist WHERE username = '"+usrname+"'")
		cursor.execute(sql)

		# Commit your changes in the database
		db.commit()
		results = cursor.fetchall()
		if results == ():
			error= "The username does not exist. Please try to register a new account."
		for row in results:
			custName = row[0]
			custPassword = row[1]
			custIdentity = row[2]

			if pwd != custPassword:
				error= "The password is wrong. Please try again."

			else:
				session['username'] = custName
				session['identity'] = custIdentity
				#return redirect(url_for('/'))

				return redirect(url_for("index"))

	return render_template("loginPage.html", error = error)
	db.close()

@app.route("/input", methods=['POST','GET'])
def input():
	user=session['username']
	if request.method == 'POST':
		clas = request.form['cls']
		clsno = request.form['clsnumber']
		subj = request.form['subject']
		cw = request.form['cwscore']
		jt = request.form['jtscore']
		exm = request.form['exmscore']

		#capitalize the letter of the class
		clas = clas[0]+clas[1].upper()

		#Make the subject write as full
		if subj=='chi':
			subj='Chinese'
		elif subj=='eng':
			subj='English'
		elif subj=='math':
			subj='Maths'
		elif subj=='phy':
			subj='Physics'
		elif subj=='chem':
			subj='Chemistry'
		elif subj=='bio':
			subj='Biology'
		elif subj=='econ':
			subj='Economics'
		else:
			subj='ICT'
			
		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# Execute the SQL command
		sql = ("INSERT INTO scorelist(cls, clsnumber, subject, cwscore, jtscore, exmscore) VALUES (%s, %s, %s, %s, %s, %s)")
		cursor.execute(sql,(clas, clsno, subj, cw, jt, exm))

		# Commit your changes in the database
		db.commit()

		return redirect(url_for("input_confirm"))

	return render_template("input.html", user=user)

@app.route("/input_confirm")
def input_confirm():
	user=session['username']
	return render_template("input_confirm.html", user=user)

@app.route("/logout")
def layout():
	#remove the username from the session if it is there
	session.pop('identity', None)
	session.pop('username', None)
	return render_template("logout.html")

if __name__ == '__main__':
	app.run(debug = True)