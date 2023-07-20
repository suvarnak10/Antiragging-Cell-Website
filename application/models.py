from .database import db

class Student(db.Model):
    __tablename__ = 'Student'
    Email_Id=db.Column(db.String,primary_key=True,nullable=False,unique=True)
    First_Name=db.Column(db.String,nullable=False)
    Second_Name=db.Column(db.String)
    Password=db.Column(db.String,nullable=False,unique=True)
    Contact_No=db.Column(db.Integer)
    Department=db.Column(db.String,nullable=False)
    Date_Of_Birth=db.Column(db.String,nullable=False)

class Faculty(db.Model):
    __tablename__ = 'Faculty'
    Faculty_Name= db.Column(db.String,nullable=False)
    Faculty_Email = db.Column(db.String,primary_key=True,nullable=False) 
    Password=db.Column(db.String,nullable=False)

class Complaint(db.Model):
    __tablename__ = 'Complaint'
    Complaint_Id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False, unique=True)
    Stud_Email_Id= db.Column(db.String,db.ForeignKey("Student.Email_Id"), nullable=False)
    Complaint_Letter= db.Column(db.String)
    Status=db.Column(db.String)
    Department=db.Column(db.String)
    Contact=db.Column(db.Integer)
