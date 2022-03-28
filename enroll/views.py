from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# this function works as add student and show all students.


def add_show(request):
   
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # To check the form is valid or not
        if fm.is_valid():
            # used to save form data to the database.
            # fm.save()

            # to get data from the particular input field in form
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            # to create User object and save data to the database using save() method.
            user = User(name=name, email=email, password=password)
            user.save()

            # To clear th form.
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()

    # to get all student data from the database.
    studentData = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'formData': fm, 'studentData': studentData})


# This function  will performed for updating student data
def editStudent(request , stdId):
   
    if request.method == 'POST':
        std = User.objects.get(id  = stdId)
        fm = StudentRegistration(request.POST , instance = std)

        if fm.is_valid():
            fm.save()
    else:
        std = User.objects.get(id  = stdId)
        fm = StudentRegistration(instance = std)
    return render(request , 'enroll/updatestudent.html' , {'formData' : fm })



# This function will performed for deleting student
def deleteStudent(request, stdId):
    std = User.objects.get(id=stdId)
    std.delete()
    return HttpResponseRedirect('/')
