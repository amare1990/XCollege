# Generated by Django 4.2.7 on 2024-01-18 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_name', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(choices=[('PhD', 'PhD'), ('MSc.', 'MSc.'), ('BSc.', 'BSc.')], max_length=50)),
                ('program_type', models.CharField(choices=[('summer', 'Summer'), ('Extension', 'Extension'), ('Regular', 'Regular')], max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='Enter your bio briefly')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('teacher', 'Teacher'), ('staff', 'Staff'), ('student', 'Student')], default='student', max_length=20)),
                ('academic_year', models.CharField(blank=True, choices=[('1st', 'First'), ('2nd', 'Second'), ('3rd', 'Third'), ('4th', 'Fourth'), ('5th', 'Fifth')], max_length=20, null=True)),
                ('semester', models.CharField(blank=True, choices=[('1st', 'First'), ('2nd', 'Second'), ('summer', 'Summer')], max_length=20, null=True)),
                ('title', models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], max_length=20, null=True)),
                ('position', models.CharField(blank=True, choices=[('head', 'Head'), ('school dean', 'School Dean'), ('chair', 'Chair'), ('program coordinator', 'Program Coordinator'), ('college dean', 'College Dean')], max_length=50, null=True)),
                ('profile_picture', models.ImageField(default='profile_pictures/default_profile.jpg', upload_to='profile_pictures/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.department')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.program')),
                ('stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.stream')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stream',
            name='chair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stream_chair', to='admin_app.userprofile'),
        ),
        migrations.AddField(
            model_name='stream',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.department'),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school_dean', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_dean', to='admin_app.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_coordinator', to='admin_app.userprofile'),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('leave_request_comments', models.TextField(blank=True)),
                ('notification_viewed', models.BooleanField(default=False)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests_requested_by', to='admin_app.userprofile')),
                ('requested_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests_requested_to', to='admin_app.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_head', to='admin_app.userprofile'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('academic_year', models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('3rd', 'Third'), ('4th', 'Fourth'), ('5th', 'Fifth')], max_length=20)),
                ('semester', models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('summer', 'Summer')], max_length=20)),
                ('is_offered', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.department')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.program')),
                ('stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.stream')),
                ('students', models.ManyToManyField(blank=True, related_name='courses_registered', to='admin_app.userprofile')),
                ('teachers', models.ManyToManyField(blank=True, related_name='courses_taught', to='admin_app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('time', models.TimeField()),
                ('class_name', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.room')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='course',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='admin_app.course'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='teacher',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='admin_app.userprofile'),
        ),
    ]
