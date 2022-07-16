from statistics import mode
from django.contrib import admin
from .models import Test, Question, StudentResult, Answer
# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course_id', 'section_id', 'max_grade', 'begin_time', 'finish_time', 'duration']
    search_fields = ['title', 'course_id', 'section_id']

class AnswerAdmin(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    list_display = ['id', 'test_id', 'text']
    search_fields =['test_id', 'text']

class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'section', 'test', 'result', 'is_passed','created_at']
    search_fields = ['student', 'course', 'section', 'test']
    
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(StudentResult, StudentResultAdmin)