# Generated by Django 5.0.2 on 2024-03-18 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0021_remove_checklistitem_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitevisitphoto',
            name='created_by',
        ),
    ]