from django.contrib import admin
from .models import *

class CourseSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'name']

# Register your models here.
admin.site.register(SpecializeModel)
admin.site.register(CourseModel)
admin.site.register(CourseCommentary) 
admin.site.register(CourseSection, CourseSectionAdmin)
admin.site.register(LessonModel)