# Generated by Django 5.0.2 on 2024-03-16 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0016_rename_image_sitevisitphoto_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitevisitphoto',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitevisitAPP.sitevisit'),
        ),
    ]
