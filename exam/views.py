from django.shortcuts import render
from django.http import HttpResponse
from exam.models import Mcq
from dashboard.models import Profile
from register.models import Student
from exam.models import Mcq
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from exam.forms import TestForm

def exam(request,email,testno,qno):
    qno=int(qno)
    pr=list(Profile.objects.filter(test_uid__exact=testno,student_emailid__exact=email))
    mcq=Mcq.objects.filter(test_no__exact=testno)
    total_ques=mcq.count()

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            one = form.cleaned_data['ans1']
            two = form.cleaned_data['ans2']
            three = form.cleaned_data['ans3']
            four = form.cleaned_data['ans4']
            if one==mcq[qno].ans1 and two==mcq[qno].ans2 and three==mcq[qno].ans3 and four==mcq[qno].ans4 :
                pr[0].test_score=pr[0].test_score+mcq[qno].points
                pr[0].save()
                
                
            # pr[0].save()
            qno=qno+1
            qno=str(qno)
            return HttpResponseRedirect('/test/%s/%s/%s' % (email,testno,qno) )
    else:
        form = TestForm()
    if qno<total_ques:
        context = {'form':form,'Mcq':mcq[qno],'Profile':pr[0]}
        return render(request,'ques.html',context)
    else:
        context = {'form':form,'Mcq':mcq[qno-1],'Profile':pr[0]}
        return render(request,'result.html',context)


    
    





