# Generated by Django 3.2.9 on 2022-06-27 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20220627_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_result', to='exams.test'),
        ),
    ]