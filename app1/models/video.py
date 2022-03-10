from django.db import models

from app1.models import  Courses






class Video(models.Model):
     title=models.CharField(max_length = 20,null=False)
     courses=models.ForeignKey(Courses , null=False,on_delete=models.CASCADE)
     serial_number=models.IntegerField(null=False)
     video_id=models.CharField(max_length=30, null=False)
     is_preview=models.BooleanField(default=False)

     def __str__(self):
      return self.title