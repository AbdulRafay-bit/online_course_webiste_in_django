from django.urls import path
from.import views
urlpatterns = [
   # path('' ,views.home,name="home"),
    path('',views.courses,name="courses"),
    path('logout',views.signout,name="logout"),

    path('signup',views.SignupView.as_view(),name='signup'),
    path('login',views.LoginView.as_view(),name='login'),
    

    path('course/<str:slug>',views.coursepage,name='coursepage'),
    path('check-out/<str:slug>',views.checkout,name='checkout'),

     
]
  