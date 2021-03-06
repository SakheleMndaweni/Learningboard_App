# Generated by Django 3.1.2 on 2022-02-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.IntegerField()),
                ('Second', models.IntegerField()),
                ('third', models.IntegerField()),
                ('fourth', models.IntegerField()),
                ('totalmarks', models.IntegerField()),
                ('id_number', models.CharField(max_length=13)),
                ('subject_code', models.CharField(default='not set', max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('assessment_code', models.CharField(max_length=225)),
                ('comment', models.CharField(max_length=225)),
                ('marks', models.IntegerField()),
                ('assessment_answer', models.FileField(null=True, upload_to='AssessmentsSub')),
            ],
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.AddField(
            model_name='assessments',
            name='assessment_code',
            field=models.CharField(default='not set', max_length=225),
        ),
        migrations.AddField(
            model_name='assessments',
            name='subject_code',
            field=models.CharField(default='not set', max_length=13),
        ),
        migrations.AddField(
            model_name='attendance_code',
            name='status',
            field=models.CharField(default='not set', max_length=225),
        ),
        migrations.AddField(
            model_name='attendance_code',
            name='subject_code',
            field=models.CharField(default='not set', max_length=13),
        ),
        migrations.AlterField(
            model_name='assessments',
            name='sub_assessment',
            field=models.CharField(default='not set', max_length=13),
        ),
    ]
