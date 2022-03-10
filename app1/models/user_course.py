from django.db import models
from django.contrib.auth.models import User
from app1.models import  Courses






class UserCourse(models.Model):
     user =models.ForeignKey(User , null=False,on_delete=models.CASCADE)
     course =models.ForeignKey(Courses , null=False,on_delete=models.CASCADE)

     date=models.DateTimeField(auto_now_add=True)

     def  __str__(self):
         return f'{self.user.username} - {self.course.name}'

     def __str__(self):
      return self.title