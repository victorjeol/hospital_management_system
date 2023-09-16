from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Appoinment, Doctor, Patient


def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def about(request):
    return render(request, 'about.html')

def doctor(request):
    return render(request, 'doctor.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appoinment = Appoinment.objects.all()
    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appoinment:
        a+=1
    d1 = {'d':d,'p':p,'a':a}
    return render(request, 'index.html', d1)




def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "No"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

def Delete_Doctor(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('view_doctor')

def Add_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ""
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']

        try:
            Doctor.objects.create(name=n, mobile=m, special=sp)
            error = 'no'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)

def Delete_Patient(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('view_patient')


def Add_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ""
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']

        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = 'no'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == "POST":
        n = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(Name=n).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appoinment.objects.create(
                Doctor=doctor, Patient=patient, date=da, time=t)
            error = 'no'
        except:
            error = 'yes'
    d = {'doctor': doctor1, 'patient':patient1, 'error': error}
    return render(request, 'add_appointment.html', d)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appoinment.objects.all()
    d = {'doc': doc}
    return render(request, 'view_appointment.html', d)

def Delete_Appointment(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    app = Appoinment.objects.get(id=pk)
    app.delete()
    return redirect('view_appointment')