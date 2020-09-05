from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import JsonResponse,HttpResponse

# Create your views here.

def login_page(req):
    return render(req,'login.html')


def login(req):
    userid=req.POST.get('lEmail')
    password=req.POST.get('lpassword')
    user=auth.authenticate(username=userid,password=password)
    if user is not None:
        auth.login(req,user)
        return render(req,'home.html')
    else:
        messages.info(req,'Invalid creditionals')
        return redirect('/')
def signup(req):
    mail=req.POST.get('email')
    password=req.POST.get('pass')
   
 
    if User.objects.filter(username=mail).exists():
        return JsonResponse({'status':'emailtaken'})
    else:
        user=User.objects.create_user(username=mail,email=mail,password=password)
        user.save()
        return JsonResponse({'status':'success'})

def home(req):
    return render(req,'home.html')