# Generated by Django 3.2.3 on 2021-12-22 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stutor', '0004_alter_lessonrequest_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonrequest',
            name='education_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stutor.education_level'),
            preserve_default=False,
        ),
    ]