# Generated by Django 3.2.9 on 2022-05-31 15:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_studentsmodels_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
