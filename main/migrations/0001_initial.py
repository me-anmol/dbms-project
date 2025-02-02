# Generated by Django 3.1 on 2020-12-13 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='pics')),
                ('per_day_cost', models.FloatField()),
                ('no_of_visits', models.IntegerField()),
                ('type', models.CharField(choices=[('Beach', 'Beach'), ('HillStation', 'HillStation'), ('safari', 'safari'), ('city', 'city'), ('International', 'International')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('per_day_cost', models.FloatField()),
                ('max_res', models.IntegerField()),
                ('no_res', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='registerations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.destination')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rtc', models.FloatField()),
                ('loc', models.CharField(max_length=20)),
                ('max_res', models.IntegerField()),
                ('no_res', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=20)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.registerations')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='registerations',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.travel'),
        ),
        migrations.AddField(
            model_name='registerations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
