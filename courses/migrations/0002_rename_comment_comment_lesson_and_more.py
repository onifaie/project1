# Generated by Django 4.1 on 2022-08-13 06:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comment',
            new_name='comment_lesson',
        ),
        migrations.AlterField(
            model_name='gatogery_course',
            name='add_date',
            field=models.DateField(auto_created=True),
        ),
    ]
