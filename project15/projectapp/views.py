from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from projectapp.forms import RegistrationForm,LoginForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
           uname=form.cleaned_data.get("username")
           pwd=form.cleaned_data.get("password")
           usr=authenticate(request,username=uname,password=pwd)
           if usr:
                 login(request,usr)
                 return redirect('signup')
           else:
                 return render(request,"sigin.html",{"form":form})
           
class IndexView(View):
     def get(self,request,*args,**kw):
          return render(request,"home.html")
     

#this is done in SQl lite database due to low spec for integrating it with MySql just Uncomment database direction in settings and migrate the project
     