from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    last_name = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, upload_to="images/user_avatars/", blank=True)
    
    STATUS_CHOICES = (
        ("None", "none"),
        ("Student", "student"),
        ("Teacher", "teacher"),
        ("Teacher_And_Student", "teacher_and_student"),
        )
    status = models.CharField(max_length=22, choices=STATUS_CHOICES, default="None")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    
    # def get_all_of_my_enrolled_courses(self):
    #     """This function can get all of student's enrolled courses"""
    #     my_courses = []
    #     all_courses = self.coursemodel_set.all()
    #     if self.status == "Student" or self.status == "Teacher_And_Student":
    #         for course in all_courses:
    #             learners = course.learners.all()
    #             for learner in learners:
    #                 if self.email == learner.email:
    #                     my_courses.append(course)
    
    
    # def get_all_all_courses_created_by_myself(self):
    #     """This function created special for getting teacher's all courses"""
    #     pass
    
    
    

 
    

    