# Generated by Django 3.2.9 on 2022-06-26 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_studentresult_is_passed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresult',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='section_id',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='test_id',
            new_name='test',
        ),
    ]
