from django.shortcuts import render , redirect
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate , login , logout
from django.contrib.sessions.models import Session
from django.db import connection
from attendance.models import *
from attendance.forms  import *
from .resources import AttendanceResources , studentResources , FacultyResources
from tablib import Dataset
from django.core import serializers
from django.core.mail import send_mail
from .utils import render_to_pdf
import datetime
# Create your views here.

### ADMIN TASK IS DONE HERE.....................................................................

def home(request):
    return render(request,'home.html')
   
def admin_login(request): 
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        count=Admin.objects.filter(username=eusername,password=epassword).count()
        if  count>0:
            request.session['is_logged'] = eusername
            return redirect('/index/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'login.html',context)
    return render(request,'login.html') 

def index(request):
            if (request.session.has_key('is_logged')):
                 return render(request,'index.html')
            return redirect('/login/')


def change_pw_admin(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        ecpassword = request.POST['cpassword']
        count=Admin.objects.filter(username=eusername,password=epassword).count()
        if  count>0:
            Admin.objects.filter(username=eusername,password=epassword).update(password=ecpassword)
            return redirect('/login/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'change_pw.html',context)
    return render(request,'change_pw.html')


### STUDENT CRUD IS PERFORMS HERE...................................................

def manage_std(request):   #READ STUDENT DATA
        form = Student_Data.objects.all()
        return render(request ,'manage_std.html',{'form':form})


def add_std(request):     #INSERT STUDENT DATA
        form = studentForm()
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']
            title = 'Registration is done in Attendance Management System'
            form = studentForm(request.POST)
            if form.is_valid:
                form.save()
                send_mail(title,'Hello,\n\n\t\t\t\t You are successfully register in Attendance Management system kindly check your daily registration on site\nUsername:' + username + '\nPassword:' + password,'soninisha2709@gmail.com',[username],fail_silently=False)
                return redirect('/manage_std/')
            else:
                return render(request,'add_student.html',{'form':form})
        else:
            return render(request,'add_student.html',{'form':form})


def edit_std(request,id): #EDIT TABLE
    student = Student_Data.objects.get(std_id=id)     
    return render(request,'editstd.html', {'form':student})  
    

def update_std(request,id):  # UPDATE STUDENT DATA 
   student = Student_Data.objects.get(std_id=id)     
   form = studentForm(request.POST , instance=student)  
   if form.is_valid(): 
           form.save()
           return redirect("/manage_std/")
   return render(request,'editstd.html',{'form':student}) 

def delete_std(request,id):  # DELETE STUDENT DATA
    student = Student_Data.objects.get(std_id=id)  
    student.delete()  
    return redirect("/manage_std")  

def add_std_multi(request):
     return render(request,'add_std_multi.html')

def insert_std_sheet(request):
    context={}
    if request.method == 'POST':
        std_resource = studentResources()
        dataset = Dataset()
        new_sheet = request.FILES['mysheet']

        if not new_sheet.name.endswith('xlsx'):
            context['message']="File must be in excel formate only..."
            return render(request,'add_att.html',context)
        
        import_data = dataset.load(new_sheet.read(),format='xlsx')
        for data in import_data:
            value = Student_Data(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
            )
            value.save()
        return redirect('/manage_std/')

### FACULTY CRUD PERFORMS HERE...

def manage_faculty(request):
        form = FacultyData.objects.all()
        return render(request ,'manage_faculty.html',{'form':form})

def add_faculty(request):
        form = facultyForm()
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']
            title = 'Registration is done in Attendance Management System'
            form = facultyForm(request.POST)
            if form.is_valid:
                form.save()
                send_mail(title,'Res. Madam/Sir,\n\n\t\t\t\t You are successfully register in Attendance Management system kindly check your daily registration on site\nUsername: ' + username + '\nPassword: ' + password,'soninisha2709@gmail.com',[username],fail_silently=False)
                return redirect('/manage_faculty')
            else:
                return render(request,'add_faculty.html',{'form':form})
        else:
            return render(request,'add_faculty.html',{'form':form})

def edit_stf(request,id): #EDIT TABLE
    faculty = FacultyData.objects.get(f_id=id)     
    return render(request,'editstf.html', {'form':faculty})  
    

def update_stf(request,id):  # UPDATE STUDENT DATA 
   faculty = FacultyData.objects.get(f_id=id)     
   form = facultyForm(request.POST , instance=faculty)  
   if form.is_valid(): 
           form.save()
           return redirect("/manage_faculty/")
   return render(request,'editstf.html',{'form':faculty}) 

def delete_faculty(request,id): 
    faculty = FacultyData.objects.get(f_id=id)  
    faculty.delete()  
    return redirect("/manage_faculty") 

def add_stf_multi(request):
     return render(request,'add_stf_multi.html')

def insert_stf_sheet(request):
    context={}
    if request.method == 'POST':
        stf_resource = FacultyResources()
        dataset = Dataset()
        new_sheet = request.FILES['mysheet']

        if not new_sheet.name.endswith('xlsx'):
            context['message']="File must be in excel formate only..."
            return render(request,'add_stf_multi.html',context)
        
        import_data = dataset.load(new_sheet.read(),format='xlsx')
        for data in import_data:
            value = FacultyData(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
            )
            value.save()
        return redirect('/manage_faculty/')



# subject CRUD.....
def manage_sub(request):
        form = Subject_Table.objects.all()
        return render(request ,'manage_sub.html',{'form':form})

def add_sub(request):
        form = subjectForm
        if request.method == 'POST':
            form = subjectForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/manage_sub')
            else:
                return render(request,'add_subject.html',{'form':form})
        else:
            return render(request,'add_subject.html',{'form':form})

def edit_sub(request,id): #EDIT TABLE
    subject = Subject_Table.objects.get(sub_id=id)     
    return render(request,'editsub.html', {'form':subject})  

def update_sub(request,id):  # UPDATE STUDENT DATA 
    subject = Subject_Table.objects.get(sub_id=id)     
    form = subjectForm(request.POST , instance=subject)  
    if form.is_valid(): 
           form.save()
           return redirect("/manage_sub/")
    return render(request,'editsub.html',{'form':subject})

def delete_sub(request,id): 
    subject = Subject_Table.objects.get(sub_id=id)   
    subject.delete()  
    return redirect("/manage_sub/") 



# Semester CRUD.....
def manage_sem(request):
        form = Semesters.objects.all()
        return render(request ,'manage_sem.html',{'form':form})

def add_sem(request):
        form = semesterForm
        if request.method == 'POST':
            form = semesterForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/manage_sem/')
            else:
                return render(request,'add_sem.html',{'form':form})
        else:
            return render(request,'add_sem.html',{'form':form})




# attendance operations....
def manage_att(request):
       form = Attendance_Master.objects.all().order_by('att_id')
       return render(request ,'manage_att.html',{'form':form})
    

def add_att(request):
            return render(request,'add_att.html')

def insert_att_sheet(request):
    context={}
    if request.method == 'POST':
        att_resource = AttendanceResources()
        dataset = Dataset()
        new_sheet = request.FILES['mysheet']

        if not new_sheet.name.endswith('xlsx'):
            context['message']="File must be in excel formate only..."
            return render(request,'add_att.html',context)
        
        import_data = dataset.load(new_sheet.read(),format='xlsx')
        for data in import_data:
            value = Attendance_Master(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
            )
            value.save()
        return redirect('/manage_att/')

def edit_att(request,id): #EDIT TABLE
    att = Attendance_Master.objects.get(att_id=id)     
    return render(request,'editatt.html', {'form':att})  

def update_att(request,id):  # UPDATE ATTENDANCE DATA 
    att = Attendance_Master.objects.get(att_id=id)     
    form = attendaceForm(request.POST , instance=att)  
    if form.is_valid(): 
           form.save()
           return redirect("/manage_att/")
    return render(request,'editatt.html',{'form':att})

def delete_att(request,id): 
    att = Attendance_Master.objects.get(att_id=id)   
    att.delete()  
    return redirect("/manage_att/") 


def manage_complaint(request):
    form = complain_table.objects.all()
    return render(request ,'manage_complaint.html',{'form':form})




# OPERATIONS OF STUDENT MODULES...

def std_index(request):
       if (request.session.has_key('is_std_logged')):
            data = request.session['is_std_logged']
            s = Student_Data.objects.get(email=data)
            return render(request,'student/index.html',{'form':s})
       return redirect('/std_login/')

def std_login(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['email']
        epassword = request.POST['password']
        count=Student_Data.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            request.session['is_std_logged'] = eusername
            return redirect('/std_index/')
        else:
           context['error']= 'Enter valid username or password...'
           return render(request,'student/login.html',context)
    return render(request,'student/login.html')

def std_profile(request,id):
    if (request.session.has_key('is_std_logged')):
            data = request.session['is_std_logged']
            s = Student_Data.objects.get(email=data)
            return render(request,'student/std_profile.html',{'form':s})
    return redirect('/std_login/')

def std_change_pw(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        ecpassword = request.POST['cpassword']
        count=Student_Data.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            Student_Data.objects.filter(email=eusername,password=epassword).update(password=ecpassword)
            return redirect('/std_login/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'student/change_pw.html',context)
    return render(request,'student/change_pw.html')

def complain(request,id):
    if (request.session.has_key('is_std_logged')):
        com = complainForm()
        return render(request,'student/add_complaint.html',{'cmp':com})
    return redirect('/std_login/')

def add_complaint(request):
    if (request.session.has_key('is_std_logged')):
        #context={}
        form = complainForm()
        if request.method == 'POST':
            form = complainForm(request.POST)
            if form.is_valid():
                     form.save()
                     #context={'success':"your complaint has been sent..."}
                     #return render(request,'student/add_complaint.html',context)
                     return redirect('/std_index/')
            else:
                return render(request,'student/add_complaint.html',{'form':form})
        else:
            return render(request,'student/add_complaint.html',{'form':form})
    return redirect('/std_login/')


def view_att(request,id):
    if request.session.has_key('is_std_logged'):
        cursor = connection.cursor()
        cursor.callproc('studentAttendance',[id])
        res = cursor.fetchall()
        result = []
        for r in res:
            result.append(r)
            #result.sort()
            #print(result)
        return render(request,'student/view_attendance.html',{'data':result})
    return render(request,'student/login.html')

def s_forgot(request):
        return render(request,'student/forgot_password.html')

def std_forgetpass(request):
    count =0 
    if request.method == 'POST':
        em = request.POST['email']
        print(type(em))
        count = Student_Data.objects.filter(email=em).count()
        if count > 0:
            title = 'Attendance Management System Password Reset'
            link = 'http://127.0.0.1:8000/std_resetpass/'+ em
            send_mail(title,'Here we send you a link to reset your password :\n' + link ,'soninisha2709@gmail.com',[em],fail_silently=False)
            msg = 'Your request has been sent please check your mail....'
            return render(request,'student/forgot_password.html',{'success':msg})
        msg = 'Please enter your registered Email ID...'
        return render(request,'student/forgot_password.html',{'fail':msg})
    return render(request,'student/forgot_password.html')

def std_resetpass(request,em):
    context={}
    count =0
    count =  Student_Data.objects.filter(email=em).count()
    if count>0:
            if request.method == "POST":
                psw = request.POST['password']
                cpass= request.POST['cpassword']
                if psw == cpass:
                    Student_Data.objects.filter(email=em).update(password=psw)
                    return redirect('/std_login/')
                else:
                    context={'error':'Password and Confirm password should not match...'}
                    return render(request,'student/reset_password.html',context) 
    return render(request,'student/reset_password.html',{'email':em})




## OPERATIONS OF FACULTY MODULES...

def stf_index(request):
    if (request.session.has_key('is_flt_logged')):
            data = request.session['is_flt_logged']
            f = FacultyData.objects.get(email=data)
            return render(request,'staff/index.html',{'form':f})
    return redirect('/stf_login/')

def stf_login(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['email']
        epassword = request.POST['password']
        count=FacultyData.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            request.session['is_flt_logged'] = eusername
            return redirect('/stf_index/')
        else:
           context['error']= 'Enter valid username or password...'
           return render(request,'staff/login.html',context)
    return render(request,'staff/login.html')

def stf_profil(request,id):
    f = FacultyData.objects.get(f_id=id)
    return render(request,'staff/stf_profil.html',{'form':f})

def stf_change_pw(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        ecpassword = request.POST['cpassword']
        count=FacultyData.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            FacultyData.objects.filter(email=eusername,password=epassword).update(password=ecpassword)
            return redirect('/stf_login/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'staff/change_pw.html',context)
    return render(request,'staff/change_pw.html')


def manage_att_std(request,id):
    if request.session.has_key('is_flt_logged'):
             sub = Subject_Table.objects.filter(faculty=id)
             return render(request,'staff/attendancesheet.html',{'form':sub})
    return render(request,'staff/login.html')

def mark_attendance(request,id1,id2):
    if request.session.has_key('is_flt_logged'):
        cursor = connection.cursor()
        cursor.callproc('attendaceProcedure',[id1,id2])
        res = cursor.fetchall()
        result = []
        for r in res:
            result.append(r)
            result.sort()
            print(result)
        now = datetime.datetime.now()
        return render(request,'staff/make_att.html',{'data':result,'dt':now})
    return render(request,'staff/login.html')

    
def make_attendance(request,semid,subid): 
    std_attid=[] 
    count = 0
    if request.session.has_key('is_flt_logged'):
        if request.method == 'POST':
            att_id = request.POST['att']
            print(att_id)
            a = Attendance_Master.objects.filter(sem = semid , sub =subid).order_by('att_id')
            for aid in a:
                std_attid.append(aid.att_id)
            print('student att id=',std_attid)
            present = att_id.split(",")
            present_attid = []
            for i in range(len(present)-1): 
                present_attid.append(int(present[i]))
            print('Present att id=',present_attid)
            for x in std_attid:
                count = 0
                for y in present_attid:
                    if x == y:
                         attendance = student_Attendance_Sheet(att=x,present=1)
                         attendance.save()
                         count = 1
                if count == 0:
                        attendance = student_Attendance_Sheet(att=x,present=0)
                        attendance.save()
            return redirect('/stf_index/')
            #return render(request,'staff/make_att.html')
    return render(request,'staff/login.html')

def my_lecs(request,id):
    if request.session.has_key('is_flt_logged'):
        data = request.session['is_flt_logged']
        fname = FacultyData.objects.get(email=data)
        faculty_report = []
        f_report = []
        sub = Subject_Table.objects.filter(faculty=id)
        for s in sub:
            print(s.sub_id,"---",s.sub_name)
            aid = Attendance_Master.objects.filter(sub=s.sub_id)
            for a in aid:
                print(a.att_id)
                lec = student_Attendance_Sheet.objects.filter(att=a.att_id).values('date').count()
                faculty_report=[s.sub_name,lec]
            f_report.append(faculty_report)
        print(f_report)
        f = fname.name
        print(fname.name)
        #print(f)
        return render(request,'staff/report.html',{'data':f_report,'name':f})  
    return redirect('/stf_index/')

def stf_forgot(request):
        return render(request,'staff/forgot_password.html')

def stf_forgetpass(request):
    count =0 
    if request.method == 'POST':
        em = request.POST['email']
        print(type(em))
        count = FacultyData.objects.filter(email=em).count()
        if count > 0:
            title = 'Attendance Management System Reset Password'
            link = 'http://127.0.0.1:8000/stf_resetpass/'+ em
            send_mail(title,'Here we send you a link to reset your password :\n' + link ,'soninisha2709@gmail.com',[em],fail_silently=False)
            msg = 'Your request has been sent please check your mail....'
            return render(request,'staff/forgot_password.html',{'success':msg})
        msg = 'Please enter your registered Email ID...'
        return render(request,'staff/forgot_password.html',{'fail':msg})
    return render(request,'staff/forgot_password.html')

def stf_resetpass(request,em):
    context={}
    count =0
    count =  FacultyData.objects.filter(email=em).count()
    if count>0:
            if request.method == "POST":
                psw = request.POST['password']
                cpass= request.POST['cpassword']
                if psw == cpass:
                    FacultyData.objects.filter(email=em).update(password=psw)
                    return redirect('/stf_login/')
                else:
                    context={'error':'Password and Confirm password should not match...'}
                    return render(request,'staff/reset_password.html',context) 
    return render(request,'staff/reset_password.html',{'email':em})
    



# REPORST ---------------------------------------------------------------------------
def reports(request):
    return render(request,'reports.html')

def student_report(requst):
    context = {}
    std = []
    std_report = []
    count = 0 
    if requst.method == 'POST':
        sem = requst.POST['sem']
        sub = requst.POST['sub']
        student = Student_Data.objects.filter(s_sem=sem)
        for s in student:
                aid = Attendance_Master.objects.filter(std = s.std_id,sub=sub)
                for a in aid:
                         count = student_Attendance_Sheet.objects.filter(att=a.att_id,present=1).count()
                         std = [s.Roll_no,s.name,count]
                         print(std)
                         std_report.append(std)
        print(std_report)
        now = datetime.datetime.now()
        context = {'data':std_report,'dt':now}
        #return render(requst,'view_reports.html',context)
        pdf = render_to_pdf('view_reports.html',context)
        return HttpResponse(pdf,content_type='application/pdf')

    return redirect('/reports/')

def faculty_report(request):
    faculty_report = []
    f_report = []
    if request.method == 'POST':
        fclid = request.POST['fid'] 
        fname = FacultyData.objects.get(f_id= fclid)
        sub = Subject_Table.objects.filter(faculty=fclid)
        for s in sub:
            print(s.sub_id,"---",s.sub_name)
            aid = Attendance_Master.objects.filter(sub=s.sub_id)
            for a in aid:
                print(a.att_id)
                lec = student_Attendance_Sheet.objects.filter(att=a.att_id).values('date').count()
                faculty_report=[s.sub_name,lec]
            f_report.append(faculty_report)
        print(f_report)
        f = fname.name
        print(fname.name)
        now = datetime.datetime.now()
        context = {'data':f_report,'name':f,'dt':now}
        pdf = render_to_pdf('faculty_report.html',context)
        return HttpResponse(pdf,content_type='application/pdf')
        #return render(request,'faculty_report.html',{'data':f_report,'name':f})  
    return redirect('/reports/')


