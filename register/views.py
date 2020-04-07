from django.shortcuts import render
from django.http import HttpResponse
from register.models import Student
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from register.forms import RegisterForm,LoginForm

def index(request):
	# Create your views here.
    # If this is a POST request then process the Form data

    user=Student()

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RegisterForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user.student_name = form.cleaned_data['student_name']
            user.student_email = form.cleaned_data['student_email']
            user.student_mobile = form.cleaned_data['student_mobile']
            user.student_password = form.cleaned_data['student_password']
            user.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/register/login/' )

    # If this is a GET (or any other method) create the default form.
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'Student': user,
    }

    return render(request, 'register.html', context)

def login(request):
	# Create your views here.
    # If this is a POST request then process the Form data


    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = LoginForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            student_email = form.cleaned_data['student_email']
            student_password = form.cleaned_data['student_password']
            user = Student.objects.filter(student_email__exact=student_email)
            if user[0].student_password==student_password :
            	return HttpResponseRedirect('/dashboard/%s/' % student_email)
            else :
            	return HttpResponseRedirect('/register/login/' )



            # redirect to a new URL:
            

    # If this is a GET (or any other method) create the default form.
    else:
        form = LoginForm()
    user=Student()
    context = {
        'form': form,
        'Student': user,
    }

    return render(request, 'login.html', context)