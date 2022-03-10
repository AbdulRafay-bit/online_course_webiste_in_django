from django.db import models
class Courses(models.Model):
    name = models.CharField(max_length=30, null=False)
    slug = models.CharField(max_length=500, null=False)

    description = models.CharField(max_length=600, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)

    thumbnail = models.ImageField(upload_to="files/thumbnail")

    date=models.DateTimeField(auto_now_add=True)
    resource=models.FileField(upload_to="files/resource")
    length=models.IntegerField(null=False)
    #image=models.ImageField('upload_to','app1/images')
    #name=models.CharField(max_length=230 ,null=False)
    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description = models.CharField(max_length=20, null=False)
    course = models.ForeignKey(Courses, null=False, on_delete=models.CASCADE)


        
    class Meta:
        abstract = True


class Tag(CourseProperty):
    pass


class Prerequisite(CourseProperty):
    pass


class Learning(CourseProperty):
    pass
