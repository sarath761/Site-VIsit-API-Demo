# Generated by Django 5.0.2 on 2024-03-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0013_imagetag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='tag',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
