from tabnanny import verbose
from django.db import models

from account.models import User
from courses.models import CourseModel, CourseSection
# Create your models here.

class Test(models.Model):
    class Meta:
        verbose_name_plural = 'Tests'
    title = models.CharField(max_length=80)
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True, help_text='choose one of the courses')
    section_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE, null=True, help_text='choose one of the courses section')
    max_grade = models.PositiveBigIntegerField(null=True)
    score_to_pass = models.FloatField(help_text='enter required score to pass by percents', \
        null=True)
    number_of_active_questions = models.PositiveBigIntegerField(help_text="here you should enter \
        How many questions are should be active?...", null=True)
    begin_time = models.DateTimeField(help_text="you should select test's start time here", blank=True, null=True)
    finish_time = models.DateTimeField(help_text="you should select test's finish time here", blank=True, null=True)
    duration = models.PositiveBigIntegerField(help_text="Enter duration of the test \
        If you enter only 0 i't means Test's duration time will be limitless", default=0, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return self.title
    
    def get_questions(self):
        questions = self.question_set.all().order_by('?')
        if len(list(questions)) > self.number_of_active_questions:
            questions = questions[:self.number_of_active_questions]
        return questions
        

class Question(models.Model):
    class Meta:
        verbose_name_plural = 'Questions'
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)
    
    def __str__(self):
        return self.text
    
    def get_answers(self):
        return self.answer_set.all().order_by('?')
    

class Answer(models.Model):
    class Meta:
        verbose_name_plural = 'answers'
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=150, null=True)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    
    

class StudentResult(models.Model):
    class Meta:
        verbose_name = "Student's Result"
        verbose_name_plural = "Students's Results"
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(CourseModel, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, related_name='test_result')
    result = models.FloatField()
    is_passed = models.BooleanField(default=False, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
     
    def __str__(self):
        return f"{self.student}"