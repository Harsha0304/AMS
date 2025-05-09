# Generated by Django 5.2 on 2025-04-14 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_asset_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='contact',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='assigned_to',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='inventory.employee'),
            preserve_default=False,
        ),
    ]
