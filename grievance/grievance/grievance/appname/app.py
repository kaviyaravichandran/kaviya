from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine=create_engine('postgresql://postgres:kgisl@localhost/grievancee')

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kgisl@localhost/grievancee'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


@app.route("/")
def root():
	return render_template("home.html")

@app.route("/home")
def homee():
	return render_template("home.html")
	
@app.route("/login")
def login():
	return render_template("login.html")
	
@app.route("/complaint_form")
def complaint_form():
	return render_template("complaint_form.html")
	
	
@app.route("/adminlogin")
def adminlogin():
	return render_template("adminlogin.html")
	
@app.route("/adminarea")
def adminarea():
	return render_template("adminarea.html")
	
@app.route("/complaint_form_admin")
def complaint_form_admin():
	return render_template("complaint_form_admin.html")
	
@app.route("/logout")
def logout():
	return render_template("login.html")
	
@app.route("/register")
def register():
	return render_template("register.html")	
	
@app.route("/feedback_form")
def feedback_form():
	return render_template("feedback_form.html")	
	
@app.route("/feedback_admin_view")
def feedback_admin_view():
	return render_template("feedback_admin_view.html")	
	
class register(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	name=db.Column(db.String)
	email=db.Column(db.String)
	username=db.Column(db.String)
	password=db.Column(db.String)
	confirm=db.Column(db.String)
	
	def __init__(self,name,email,username,password,confirm):
		self.name=name
		self.email=email
		self.username=username
		self.password=password
		self.confirm=confirm
		
	@app.route("/register_db",methods=["GET","POST"])
	def register_db():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['username'] or not request.form['password'] or not request.form['confirm']:
				flash("Error")
			else:
				student=register(request.form['name'],request.form['email'],request.form['username'],request.form['password'],request.form['confirm'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('register'))
		return render_template("register.html")

@app.route('/user_login',methods=['GET','POST'])
def user_login():
	user_name=str(request.form['username'])
	password=str(request.form['password'])
	Session=sessionmaker(bind=engine)
	S=Session()
	query=S.query(register).filter(register.email.in_([user_name]),register.password.in_([password]))
	result=query.first()
	if result is None:
		flash('Username or Password is invalid' , 'error')
		return redirect(url_for('login'))
	return redirect(url_for('complaint_form'))
	
@app.route('/admin_login',methods=['GET','POST'])
def admin_login():
	user_name=str(request.form['username'])
	password=str(request.form['password'])
	Session=sessionmaker(bind=engine)
	S=Session()
	query=S.query(register).filter(register.email.in_([user_name]),register.password.in_([password]))
	result=query.first()
	if result is None:
		flash('Username or Password is invalid' , 'error')
		return redirect(url_for('login'))
	print user_name
	stop
	if user_name==request.form['username']:
		return redirect(url_for('adminarea'))
	else:
		return redirect(url_for('login'))
		
	
	

class complaint(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	employee_name=db.Column(db.String)
	supervisor_name=db.Column(db.String)
	department=db.Column(db.String)
	id_number=db.Column(db.String)
	complaint=db.Column(db.String)
	complaint_detail=db.Column(db.String)
	complaint_desc=db.Column(db.String)
	date=db.Column(db.String)
	signature=db.Column(db.String)
	
	def __init__(self,employee_name,supervisor_name,department,id_number,complaint,complaint_detail,complaint_desc,date,signature):
		self.employee_name=employee_name
		self.supervisor_name=supervisor_name
		self.department=department
		self.id_number=id_number
		self.complaint=complaint
		self.complaint_detail=complaint_detail
		self.complaint_desc=complaint_desc
		self.date=date
		self.signature=signature

	@app.route("/complaint_form_db",methods=["GET","POST"])
	def complaint_form_db():
		if request.method == 'POST':
			if not request.form['employee_name'] or not request.form['supervisor_name'] or not request.form['department'] or not request.form['id_number'] or not request.form['complaint'] or not request.form['complaint_detail']  or not request.form['complaint_desc']  or not request.form['date']  or not request.form['signature']:
				flash("Error")
			else:
				student=complaint(request.form['employee_name'],request.form['supervisor_name'],request.form['department'],request.form['id_number'],request.form['complaint'],request.form['complaint_detail'],request.form['complaint_desc'],request.form['date'],request.form['signature'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('complaint_form'))
		return render_template("complaint_form.html")



class feedback(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	label_input=db.Column(db.String)
	feedback_describe=db.Column(db.String)
	first_name=db.Column(db.String)
	last_name=db.Column(db.String)
	email=db.Column(db.String)
	department=db.Column(db.String)
	
	def __init__(self,label_input,feedback_describe,first_name,last_name,email,department):
		self.label_input=label_input
		self.feedback_describe=feedback_describe
		self.first_name=first_name
		self.last_name=last_name
		self.email=email
		self.department=department
		

	@app.route("/feedback_form_db",methods=["GET","POST"])
	def feedback_form_db():
		if request.method == 'POST':
			if not request.form['label_input'] or not request.form['feedback_describe'] or not request.form['first_name'] or not request.form['last_name']  or not request.form['email'] or not request.form['department']:
				flash("Error")
			else:
				student=feedback(request.form['label_input'],request.form['feedback_describe'],request.form['first_name'],request.form['last_name'],request.form['email'],request.form['department'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('feedback_form'))
		return render_template("feedback_form.html")



if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)





