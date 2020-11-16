
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from .models import PageView, User

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
