# Generated by Django 4.2.2 on 2023-07-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_course_requirements_course_what_you_learn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]