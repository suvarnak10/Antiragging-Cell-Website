from flask import Flask, url_for,request,redirect,session
from flask import render_template
from flask import current_app as app
from application.models import *
import smtplib
import json 

@app.route("/")
def main():
     return render_template('home.html')

@app.route("/student_signin",methods =['GET', 'POST'])
def student_signin():
     if request.method=='POST':
        Email = request.form['Email Id']
        password = request.form['Password']
        print(Email,password) 
        all_students=db.session.query(Student).filter(Student.Email_Id == Email).all()
        print(all_students)
        if len(all_students)!=0 and all_students[0].Password==password:
            eid=all_students[0].Email_Id
            return redirect(url_for('test',eid=eid))
            
        else:
            return render_template('student_signin.html',msg='Wrong credentials,try again')
     return render_template('student_signin.html')

@app.route("/faculty_signin", methods=["GET","POST"])
def faculty_signin():
    if request.method=='POST':
        Email = request.form['Email']
        Password = request.form['password']
        print(Email,Password) 
        all_faculty=db.session.query(Faculty).filter(Faculty.Faculty_Email == Email).all()
        print(all_faculty)
        if len(all_faculty)!=0 and all_faculty[0].Password==Password:
         return redirect(url_for('test_faculty'))
        else:
            return render_template('faculty_signin.html',msg='Wrong credentials,try again')
    
    return render_template('faculty_signin.html')


@app.route('/student_signup', methods =['GET', 'POST'])
def student_signup():
   if request.method=='POST':
      if request.method=='POST':
            firstname = request.form['First Name']
            lastname = request.form['Last Name']
            email = request.form['Email Id']
            password = request.form['Password']
            contactno = request.form['Contact No']
            dept = request.form['Department']
            dob = request.form['Date Of Birth']
            all_students=db.session.query(Student).filter(Student.First_Name == firstname and Student.Last_Name == lastname ).all()
            if len(all_students)!=0:
                 return render_template('student_signup.html',msg='user already exists')
            new_student=Student(First_Name=firstname,Second_Name=lastname,Email_Id=email,Password=password,Contact_No=contactno,Department=dept,Date_Of_Birth=dob)
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('student_signin'))
   return render_template('student_signup.html',msg='')

@app.route('/faculty_signup', methods =['GET', 'POST'])
def faculty_signup():
   if request.method=='POST':
        if request.method=='POST':
            firstname = request.form['First Name']
            email = request.form['Email Id']
            password = request.form['Password']
            all_faculty=db.session.query(Faculty).filter(Faculty.Faculty_Name == firstname).all()
            print(all_faculty)
            if len(all_faculty)!=0:
                 return render_template('faculty_signup.html',msg='user already exists')
            new_faculty=Faculty(Faculty_Name=firstname,Faculty_Email_Id=email,Password=password)
            db.session.add(new_faculty)
            db.session.commit()
            return redirect(url_for('faculty_signin'))
   return render_template('faculty_signup.html',msg='')

@app.route("/test/<eid>", methods=['GET','POST'])
def test(eid):
        print("hello")
        all_complaint=db.session.query(Complaint).filter(Complaint.Stud_Email_Id== eid).all()
        print("hello1")
        print(all_complaint)
        if len(all_complaint)==0:
             return render_template('test.html',msg='No complaint added',eid=eid)
        return render_template('test.html',all_complaint=all_complaint,eid=eid,msg='')
  
@app.route("/complaint_form/<eid>",methods=['GET','POST'])
def complaint_form(eid):
     if request.method=='POST':
          email=request.form['email']
          dept=request.form['department']
          contact=request.form['phone_no']
          complaint_letter=request.form['complaint']
          if email== eid:
             new_complaint=Complaint(Stud_Email_Id=email,Complaint_Letter=complaint_letter,Status='Registered',Department=dept,Contact=contact)
             db.session.add(new_complaint)
             db.session.commit()
             all_faculty=list(db.session.query(Faculty).filter(Faculty.Faculty_Email).all())
             '''li=['21f1003974@ds.study.iitm.ac.in']'''
             for dest in all_faculty:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("suvarnak10102@gmail.com", "zjhwdaurahknuyaz")
                message = "NOTIFICATION!!!!   A new Complaint is registered in abc website "
                s.sendmail("suvarnak10102@gmail.com", dest.Faculty_Email, message)
                s.quit()
             return render_template('complaint_form.html',eid=eid,msg='Complaint Registered,Notification mail sent!!!')
          else:
            return render_template('complaint_form.html',eid=eid,msg='Use Your Own Email Id!!')

     return render_template('complaint_form.html',eid=eid,msg='')

@app.route("/test_faculty")
def test_faculty():
     all_students=db.session.query(Student).all()
     all_complaint=db.session.query(Complaint).all()
     complaints=[]
     students=[]
     for i in all_students:
        flag=True
        for j in all_complaint:
            if i.Email_Id==j.Stud_Email_Id:
                cid=j.Stud_Email_Id
                complaints.append([i.Email_Id,i.Department,i.Contact_No,j.Complaint_Id,j.Complaint_Letter,j.Status])
                if flag:
                    students.append([i.Email_Id,i.Department,i.Contact_No])
                    flag=False
     print(len(all_students))
     print(len(complaints))
     return render_template('test_faculty.html',all_students=students, all_complaint=complaints,cid=cid)
@app.route("/undertaking")
def undertaking():
     return render_template('undertaking.html')

@app.route("/rules")
def rules():
     return render_template('rules.html')

@app.route("/regulations")
def regulations():
     return render_template('regulations.html')

@app.route("/punishments")
def punishments():
     return render_template('punishments.html')

@app.route('/logout')
def logout():
    return redirect(url_for('student_signin'))

'''import smtplib

# list of email_id to send the mail
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]

for dest in li:
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("sender_email_id", "sender_email_id_password")
	message = "Message_you_need_to_send"
	s.sendmail("sender_email_id", dest, message)
	s.quit()'''

'''@app.route("/pending/<cid>")
def pending(cid):
     all_complaint=db.session.query(Complaint).all()
     new_complaint=Complaint(Status='Registered')
     db.session.add(new_complaint)
     db.session.commit()
     return render_template('test_faculty.html',cid=cid)

@app.route("/in_progress/<cid>")
def in_progress(cid):
     all_complaint=db.session.query(Complaint).all()
     new_complaint=Complaint(Status='In Progress')
     db.session.add(new_complaint)
     db.session.commit()
     return render_template('test_faculty.html',cid=cid)

@app.route("/Resolved/<cid>")
def pending(cid):
     all_complaint=db.session.query(Complaint).all()
     new_complaint=Complaint(Status='Resolved')
     db.session.add(new_complaint)
     db.session.commit()
     return render_template('test_faculty.html',cid=cid)'''
