# Generated by Django 5.0.2 on 2024-03-18 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0025_checklistitem_created_by_sitevisitphoto_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitevisit',
            old_name='title',
            new_name='visit',
        ),
    ]