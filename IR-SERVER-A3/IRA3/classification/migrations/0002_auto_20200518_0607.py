# Generated by Django 3.0.6 on 2020-05-18 01:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knnclasification',
            options={'get_latest_by': ['time_created']},
        ),
        migrations.AddField(
            model_name='knnclasification',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='knnclasification',
            name='id',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
