
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.


def my_login(request):
    return render(request, template_name='Dinner.html')


def my_web(request):
    return render(request, template_name='web.html')

def save_data(request):
    return redirect('my_web')

# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form})