# Generated by Django 5.0.2 on 2024-03-07 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0006_alter_sitevisitphoto_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitevisitphoto',
            name='tags',
        ),
        migrations.AlterField(
            model_name='sitevisitphoto',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='site_visit_photos/'),
        ),
        migrations.AlterField(
            model_name='sitevisitphoto',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sitevisitAPP.sitevisit'),
        ),
    ]
