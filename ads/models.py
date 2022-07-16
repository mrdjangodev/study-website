from secrets import choice
from django.db import models
from account.models import User
# Create your models here.

class Ads(models.Model):
    class Meta:
        verbose_name_plural = 'Ads'
    auther = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    text = models.TextField()
    RECIEVER_CHOICES = (
        ("everyone", "everyone"),
        ("Student", "student"),
        ("Teacher", "teacher"),
        )
    speacial_for = models.CharField(max_length=9, choices=RECIEVER_CHOICES)
    ad_seen_by_users = models.ManyToManyField(User, related_name='seen_users', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.speacial_for}"
    
    
    
        
    