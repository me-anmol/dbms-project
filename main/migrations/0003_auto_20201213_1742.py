# Generated by Django 3.1 on 2020-12-13 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201213_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.registerations'),
        ),
    ]
