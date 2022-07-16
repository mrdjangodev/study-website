# Generated by Django 3.2.9 on 2022-06-04 05:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20220601_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='finished_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Course finished users'),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='fn_cs_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Course section finished users'),
        ),
        migrations.AlterField(
            model_name='lessonmodel',
            name='fn_l_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='students who are Finished the lesson'),
        ),
    ]