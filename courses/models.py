from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

from ckeditor.fields import RichTextField


from account.models import User

# Create your models here.

class SpecializeModel(models.Model):
    class Meta:
        verbose_name = 'Specialize or Subject'
        verbose_name_plural = 'Specializes or Subjects'
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/subject_specialize_images', null=True)
    desciption = models.CharField(max_length=250, null=True, help_text='Write something about specialize or subjects. For instance about its advantages')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name





class CourseModel(models.Model):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = "Courses"
    specialize_id = models.ForeignKey(SpecializeModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="teacher")
    image = models.ImageField(upload_to='images/course_images', null=True)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True, default=0, verbose_name='price by $(dollar)',\
        validators=[MinValueValidator(Decimal('0'))])
    learners = models.ManyToManyField(User, related_name='learners', blank=True)
    
    finished_users = models.ManyToManyField(User, verbose_name='Course finished users', blank=True)
    
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    # def get_all_sections_of_course(self):
    #     return self.coursesection_set.all()
    
    
    
class CourseCommentary(models.Model):
    class Meta:
        verbose_name = 'Commentary for course'
        verbose_name_plural = 'Commentaries for courses'
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=80, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment[:20]   
    

class CourseSection(models.Model):
    class Meta:
        verbose_name = 'Section of courses'
        verbose_name_plural = "Sections of courses"
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='section')
    name = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='images/couse_section_images', null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    
    fn_cs_users = models.ManyToManyField(User, verbose_name='Course section finished users', blank=True)
    
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def count_lessons(self):
        lessons = LessonModel.objects.filter(section_id=self.id)
        # lessons = self.lesson_set.all().count()
        return lessons.count()
    
class LessonModel(models.Model):
    class Meta:
        verbose_name = 'Lessons'
        verbose_name_plural = "Lessons"
    name = models.CharField(max_length=80, null=True)
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE, verbose_name='Course')
    section_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE, verbose_name='Section', related_name = 'lesson')
    document = models.FileField(upload_to='documents/lessons', null=True, blank=True)
    video = models.FileField(upload_to='videos/lessons', null=True, blank=True)
    image_video = models.ImageField(upload_to='images/for_videos', null=True, blank=True)
    description = RichTextField(blank=True, null=True, \
        help_text='you should use from this section for explaining the lesson')
    
    fn_l_users = models.ManyToManyField(User, verbose_name='students who are Finished the lesson', blank=True)
    
    def __str__(self):
        return self.name
    
    def next_lesson(self):
        """ this function created for getting next lesson """
        lessons = LessonModel.objects.filter(section_id=self.section_id)
        next_lesson = None
        object_is_found = False
        for lesson in lessons:
            if object_is_found == True:
                next_lesson = lesson
                break
            if lesson.id == self.id:
                object_is_found = True

        return next_lesson
        