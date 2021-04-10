from django.db import models
# Create your models here.
# Create your models here.

# Admin Table
class Admin(models.Model):
    admin_id = models.AutoField(primary_key='True')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

# Semester Table
class Semesters(models.Model):
    sem_id = models.AutoField(primary_key='True')
    sem = models.CharField(max_length=10,unique='True')

#Student Table
class Student_Data(models.Model):
    std_id = models.AutoField(primary_key='True')
    Roll_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100,unique='True')
    email = models.CharField(max_length=100,unique='True')
    password = models.CharField(max_length=100)
    s_sem = models.CharField(models.ForeignKey(Semesters,on_delete=models.CASCADE),max_length=10)
    class Meta:
        db_table='Student_master'
    
# Faculty Table
class FacultyData(models.Model):
    f_id = models.AutoField(primary_key='True')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique='True')
    password = models.CharField(max_length=100)

# Subject Table   
class Subject_Table(models.Model):
    sub_id = models.AutoField(primary_key='True')
    sub_name = models.CharField(max_length=100)
    faculty = models.CharField(models.ForeignKey(FacultyData,on_delete=models.CASCADE),null='True',max_length=5)
    sem = models.CharField(models.ForeignKey(Semesters,on_delete=models.CASCADE),null='True',max_length=5)

# Attendance Table
class Attendance_Master(models.Model):
    att_id = models.AutoField( db_index=True,primary_key=True)
    sem = models.CharField(models.ForeignKey(Semesters,on_delete=models.CASCADE),null='True',max_length=5)
    std = models.CharField(models.ForeignKey(Student_Data,on_delete=models.CASCADE),null='True',max_length=5)
    sub = models.CharField(models.ForeignKey(Subject_Table,on_delete=models.CASCADE),null='True',max_length=5)
    faculty = models.CharField(models.ForeignKey(FacultyData,on_delete=models.CASCADE),null='True',max_length=5)
    class Meta:
        db_table='Attendance_master'
        unique_together = (('sem', 'std','sub','faculty'),)

# student attendance Table  
class student_Attendance_Sheet(models.Model):
        std_att_id = models.AutoField(primary_key='True')
        date = models.DateField(auto_now_add='True')
        att = models.CharField(models.ForeignKey(Attendance_Master , on_delete=models.CASCADE),null='True',max_length=3)
        present = models.CharField(max_length=3)
        


# Complain Table
class complain_table(models.Model):
    cid = models.AutoField(primary_key=True)
    Std = models.CharField(models.ForeignKey(Student_Data , on_delete=models.CASCADE),max_length=10)
    msg = models.CharField(max_length=250)
