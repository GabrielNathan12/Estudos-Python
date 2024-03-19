# Generated by Django 5.0.3 on 2024-03-17 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_sitesetup'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.sitesetup'),
        ),
    ]
