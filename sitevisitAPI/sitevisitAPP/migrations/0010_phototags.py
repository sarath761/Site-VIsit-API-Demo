# Generated by Django 5.0.2 on 2024-03-07 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitevisitAPP', '0009_alter_sitevisit_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.TextField(blank=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tags', to='sitevisitAPP.sitevisitphoto')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tagvisit', to='sitevisitAPP.sitevisit')),
            ],
        ),
    ]
