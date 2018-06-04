# Generated by Django 2.0.6 on 2018-06-04 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='2018', max_length=40)),
                ('number_of_students', models.IntegerField(default='48')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, default='', max_length=30)),
                ('affiliated_institute', models.CharField(default='PUL', max_length=10)),
                ('started_teaching', models.CharField(blank=True, default='2018', max_length=4)),
                ('upper_degree', models.CharField(
                    choices=[('MSc', 'MSc'), ('Diploma', 'Diploma'), ('PhD', 'PhD'), ('Bachelors', 'Bachelors')],
                    default='MSc', max_length=30)),
                ('aff_type', models.CharField(
                    choices=[('Visiting', 'Visiting'), ('Permanent', 'Permanent'), ('Contract', 'Contract')],
                    default='Permanent', max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('program_code', models.CharField(blank=True, default=' ', max_length=40)),
                ('subject_teacher_teaching_experience_years', models.CharField(blank=True, max_length=4)),
                ('int_marks', models.IntegerField(default='40')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college.Programme')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, default='', max_length=30)),
                ('affiliated_institute', models.CharField(default='PUL', max_length=10)),
                ('started_teaching', models.CharField(blank=True, default='2018', max_length=4)),
                ('upper_degree', models.CharField(
                    choices=[('MSc', 'MSc'), ('Diploma', 'Diploma'), ('PhD', 'PhD'), ('Bachelors', 'Bachelors')],
                    default='MSc', max_length=30)),
                ('aff_type', models.CharField(
                    choices=[('Visiting', 'Visiting'), ('Permanent', 'Permanent'), ('Contract', 'Contract')],
                    default='Permanent', max_length=30)),
                ('teacher_id', models.CharField(blank=True, default=' ', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Teacher'),
        ),
        migrations.AddField(
            model_name='expert',
            name='topic',
            field=models.ManyToManyField(to='college.Topic'),
        ),
        migrations.AddField(
            model_name='batch',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.Programme'),
        ),
    ]
