# Generated by Django 5.0.2 on 2024-03-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0011_sitevisitphoto_tag_delete_phototags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitevisitphoto',
            name='tag',
        ),
    ]
