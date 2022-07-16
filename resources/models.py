from django.db import models
from account.models import User


from courses.models import CourseModel
from .validators import valid_file_size_for_documents, valid_file_type_for_documents
# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=35, null=True)
    auther =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="from")
    RECIEVERS_CHOICES = (
        ('everyone', 'everyone'),
        ('my_students', 'my students'),
    )
    recievers = models.CharField(max_length=11, choices=RECIEVERS_CHOICES, default='everyone')
    TYPE_CHOICES = (
        ('books', 'books'),
        ('articles', 'articles'),
        ('scientific_article', 'scientific article'),
        ('usefull', 'usefull'),
    )
    document_type = models.CharField(max_length=19, choices=TYPE_CHOICES, default='books')
    file = models.FileField(upload_to='resources', \
        validators=[valid_file_type_for_documents, valid_file_size_for_documents])
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.recievers} {self.auther}'
    
    def get_size(self):
        # 1 mb = 1048576
        size = round(self.file.size/1048576, 2)
        return size