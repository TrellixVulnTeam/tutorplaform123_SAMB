# Generated by Django 3.2.3 on 2021-12-22 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_lessonrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LessonRequest',
        ),
    ]