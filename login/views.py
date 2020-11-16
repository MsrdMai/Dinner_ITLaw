
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from .models import PageView, User
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)

def my_home(request):

    view = PageView.objects.get(pk=1)
    view.count += 1
    view.save()
    return render(request, template_name='Dinner.html')


def my_web(request):
    return render(request, template_name='web.html')

def save_data(request):
    if request.method == 'POST' and request.FILES:
        numphone = request.POST.get('num') 
        mail = request.POST.get('email')
        name = request.POST.get('name') 
        password = request.POST.get('password')
        hbd = request.POST.get('hbd')
        school = request.POST.get('school')
        gender = request.POST.get('gender')
        img = request.FILES['myfile']

        user = User.objects.create(name=name, password=password, phone=numphone, email=mail, birthday=hbd, gender=gender,
        school=school, cus_img=img)
        user.save()

    return redirect("web")

def my_login(request):
    # if request.method == 'POST':
    #     numphone = request.POST.get('num') 
    #     mail = request.POST.get('email')
    context = {}
    next_page = "web"
    
    if request.method == 'POST':
        if request.GET.get('next'): #check for redirect
            next_page = request.GET.get('next')
        
        numphone = request.POST.get('num')
        email = request.POST.get('email')

        user = authenticate(request, numphone=numphone, email=email)

        if user:
            login(request, user)
            print(next_page)
            return redirect(next_page)
        else:
            context = {'numphone': numphone,
                       'email': email,
                       'error': 'Wrong numphone or email'}
    return render(request, template_name='web.html', context=context)
