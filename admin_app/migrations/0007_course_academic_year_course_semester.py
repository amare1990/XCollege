# Generated by Django 4.2.5 on 2023-11-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_course_program_course_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='academic_year',
            field=models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('3rd', 'Third'), ('4th', 'Fourth'), ('5th', 'Fifth')], default='first', max_length=20),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('summer', 'Summer')], default='first', max_length=20),
        ),
    ]
