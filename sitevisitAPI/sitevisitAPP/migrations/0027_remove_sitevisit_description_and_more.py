# Generated by Django 5.0.2 on 2024-03-25 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0026_rename_title_sitevisit_visit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitevisit',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sitevisit',
            name='plan_file',
        ),
        migrations.RemoveField(
            model_name='sitevisit',
            name='status',
        ),
    ]