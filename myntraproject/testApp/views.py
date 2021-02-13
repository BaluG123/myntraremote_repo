from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from testApp import forms
from testApp.models import buyer

# Create your views here.
@login_required
def homeview(request):
    return render(request,'testApp/home.html')

def logoutview(request):
    return render(request,'testApp/logout.html')

def signupview(request):
    form=forms.signupForm()
    if request.method=='POST':
        form=forms.signupForm(request.POST)
        username=request.POST['username']
        request.session['username']=username
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})

class buyersview(ListView):
    model=buyer
    template_name='testApp/home.html'

def imagesview(request):
    return render(request,'testApp/images.html')

def page1view(request):
    return render(request,'testApp/page1.html')

def buyitemview(request):
    return render(request,'testApp/buy.html')

def buyitemview1(request):
    return render(request,'testApp/buy1.html')

def buyitemview9(request):
    return render(request,'testApp/buy9.html')

def infoview(request):
    form=forms.infoform()
    if request.method=='POST':
        form=forms.infoform(request.POST)
        if form.is_valid():
            print('order confirmed...!')
            print('your item delver soon..!')
            print('thanks for choosing our website')
        return redirect('/home')
    return render(request,'testApp/info.html',{'form':form})

def aboutview(request):
    return render(request,'testApp/aboutus.html')

def rateview(request):
    return render(request,'testApp/rateus.html')      
