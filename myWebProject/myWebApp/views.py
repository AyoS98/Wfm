from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login')

def home(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     if name:
    #         return HttpResponse(f'<h2>Hello {name}! Thank you for contacting us</h2>')
    #     else:
    #         return HttpResponse("<h3>Please enter a valid name</h3>")
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        WfmAnonContactsubmission.objects.create(subject=subject, message=message)
        return redirect('success')

    return render(request, 'AnonContactWfm.html')

def success(request):
    return render(request, 'success.html')

# def home2(request):
#     return render (request, 'messicr7.html')

# def home3(request):
#     return render (request, 'artisanform.html')

# def home4(request):
#     return render (request, 'messi.html')

# def home5(request):
#     info = Info.objects.all()
#     return render (request, 'cr7.html', {'info' : info},)

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.error(request, 'Login Details are incorrect')
#             return redirect('login')

#     else:
#         return render(request, 'messicr7.html')

# def register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if  User.objects.filter(email=email).exists():
#                 messages.error(request, 'Email Already Exists')
#                 return redirect('register')
            
#             elif User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username Already Exists')
#                 return redirect('register')
            
#             # elif User.objects.filter(phone=phone).exists():
#             #     messages.error(request, 'Phone Number is already in use')
#             #     return redirect('register')
            
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password1)
#                 user.save;
#                 return redirect('login')
    
#         else:
#             messages.error(request, 'Passwords Do not Match')
#             return redirect('register')
#     else:
#         return render(request, 'register.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('/')


