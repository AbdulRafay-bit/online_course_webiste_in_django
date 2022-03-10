
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from.models import Courses,Video
from django.views import View
from django.contrib.auth import logout
from app1.forms import RegistrationForm,LoginForm
from courses.settings import *
from time import time

#checkout 





class SignupView(View):
    def get(self,request):
        
        form=RegistrationForm()

        print("response form class basesd")
        return render(request,"signup_page.html",context={'form':form})
    def post (self,request):
        form=RegistrationForm(request.POST)
        if(form.is_valid()):
            user=form.save()
            if(user is not None):
                return redirect('login')

        return render(request,"signup_page.html",context={'form':form})

def courses(request):
    cours=Courses.objects.all()
   
    return render(request,"home.html",{"cours":cours})
# Create your views here.
def coursepage(request,slug):

    course=Courses.objects.get(slug=slug)
    serial_number=request.GET.get('lecture')
    videos=course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number=1
    video=Video.objects.get(serial_number =  serial_number)
    print("Preview Video",video.is_preview)
    
    if((request.user.is_authenticated is False) and  (video.is_preview is False)):
        return redirect("login")

    print(video)
    context={
        "course":course,
        "video":video,
        'videos':videos
    }
    return render(request,"course.html",context=context)




    

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        context={
            "form":form
        }
        return render(request,"login_page.html",context=context)

    def post(self,request):
        form=LoginForm(request=request,data=request.POST)
        context={
            "form":form
        }
        if(form.is_valid()):
          return redirect ("courses")
        return render(request,"login_page.html",context=context)


def signout(request):
    logout(request)
    return redirect("courses")



#chek out page

def checkout(request,slug):
    
    course=Courses.objects.get(slug=slug)
    user=None
    if not request.user.is_authenticated:
        # if you are enrolled in this course you can wathch every videos
    
   
        return redirect("login")
    user=request.user
    action=request.GET.get('action')
    order=None
    if action == 'create_payment':
       amount= int((course.price-(course.price * course.discount * 0.01))*100)
       currency="INR"
       notes={
           "email":user.email,
           "name":f'{user.first_name} {user.last_name}'

       }
       reciept=f"courses-{int(time())}"
       order=client.order.create({'reciept':reciept,'notes':notes,'amount':amount,'currency':currency})
    context={
        "course":course,
        "order":order
    }
    return render(request,"checkout.html",context=context)




