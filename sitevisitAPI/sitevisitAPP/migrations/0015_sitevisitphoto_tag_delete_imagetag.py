# Generated by Django 5.0.2 on 2024-03-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0014_alter_imagetag_id_alter_imagetag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitevisitphoto',
            name='tag',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ImageTag',
        ),
    ]
