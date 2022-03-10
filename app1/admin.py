from django.contrib import admin
from app1.models import Courses,Payment,UserCourse,Tag,Prerequisite,Learning,Video

class TagAdmin(admin.TabularInline):
    model= Tag
class LearningAdmin(admin.TabularInline):
    model= Learning

class PrerequisiteAdmin(admin.TabularInline):
    model= Prerequisite


class VideoAdmin(admin.TabularInline):
    model= Video


class CourseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin, LearningAdmin , PrerequisiteAdmin,VideoAdmin]
admin.site.register(Courses,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)

