# Generated by Django 3.1.2 on 2022-02-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BR_Parents_Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id_number', models.CharField(max_length=13)),
                ('student_id_number', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('topic', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('creator_id', models.CharField(max_length=13)),
                ('res_id', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('surname', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('id_number', models.CharField(max_length=13, unique=True)),
                ('image', models.ImageField(null=True, upload_to='parent')),
            ],
        ),
        migrations.CreateModel(
            name='Validate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=225)),
                ('parent_id', models.CharField(max_length=13)),
                ('student_id', models.CharField(max_length=13)),
            ],
        ),
    ]
