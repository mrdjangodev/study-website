# Generated by Django 3.2.9 on 2022-06-25 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20220607_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='test',
            name='number_of_active_questions',
            field=models.PositiveBigIntegerField(help_text='here you should enter         How many questions are should be active?...', null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='score_to_pass',
            field=models.FloatField(help_text='enter required score to pass by percents', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='test_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.test'),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(None, 'none'), (10, '10 minutes'), (15, '15 minutes'), (20, '20 minutes'), (30, '30 minutes'), (40, '40 minutes'), (1, '1 hour'), (2, '2 hours')], default=None, null=True),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.question')),
            ],
            options={
                'verbose_name_plural': 'answers',
            },
        ),
    ]
