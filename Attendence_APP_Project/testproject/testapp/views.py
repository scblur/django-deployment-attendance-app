from django.shortcuts import render
# from django.http import HttpResponse
from . import forms
from django.utils import timezone
from datetime import datetime
from testapp.forms import UserSessionForm

# Create your views here.
def a_submit(request):
    return render(request,'testapp/a_submit.html')

def index(request):
    form = forms.UserSessionForm()

    if request.method == "POST":
        form = UserSessionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("Session: "+form.cleaned_data['session'])
            print("Date: "+str(form.cleaned_data['t_date']))
            print(timezone.localtime())
            return a_submit(request)
        else:
            print("ERROR! Form Invalid!")
    return render(request,'testapp/index.html',{'form':form})
