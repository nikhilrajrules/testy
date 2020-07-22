from django.shortcuts import render
from django.http import HttpResponse
from register.models import Student
from dashboard.models import Profile
# from questions.models import Joiners
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from register.models import Student
from exam.models import Mcq
from dashboard.forms import ProfileForm

def profile(request,email):
	# Create your views here.
    # If this is a POST request then process the Form data

    # user=Student.objects.filter(student_email__exact=email)
    profile=Profile()
    # jr=Joiners()
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ProfileForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            profile.test_uid = form.cleaned_data['test_uid']
            # jr.test_uid=profile.test_uid
            profile.test_score=0
            profile.ques_used=0
            # profile.ques_id=1
            profile.student_emailid = email
            # jr.save()
            profile.save()
            zero=0
            zero=str(zero)
            # redirect to a new URL:
            return HttpResponseRedirect('/test/%s/%s/%s' % (email,profile.test_uid,zero) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = ProfileForm()

    context = {
        'form': form,
        'email':email,
        'Profile': profile
    }

    return render(request, 'dashboard.html', context)
