# Generated by Django 3.2.9 on 2022-06-07 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_alter_lessonmodel_image_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('max_grade', models.PositiveBigIntegerField(null=True)),
                ('begin_time', models.DateTimeField(blank=True, help_text="you should select test's start time here", null=True)),
                ('finish_time', models.DateTimeField(blank=True, help_text="you should select test's finish time here", null=True)),
                ('duration', models.TimeField(blank=True, help_text='how much time you give for working this test?', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(help_text='choose one of the courses', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.coursemodel')),
                ('section_id', models.ForeignKey(help_text='choose one of the courses section', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.coursesection')),
            ],
            options={
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.coursemodel')),
                ('section_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.coursesection')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('test_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.test')),
            ],
            options={
                'verbose_name': "Student's Result",
                'verbose_name_plural': "Students's Results",
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('answer1', models.CharField(max_length=120, null=True)),
                ('answer2', models.CharField(max_length=120, null=True)),
                ('answer3', models.CharField(max_length=120, null=True)),
                ('answer4', models.CharField(max_length=120, null=True)),
                ('correct_answer', models.CharField(choices=[('ANSWER1', 'answer1'), ('ANSWER2', 'answer2'), ('ANSWER3', 'answer3'), ('ANSWER4', 'answer4')], max_length=8, null=True)),
                ('test_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Test', to='exams.test')),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
