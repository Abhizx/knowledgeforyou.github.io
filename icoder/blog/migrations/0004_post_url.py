# Generated by Django 3.1.5 on 2021-01-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210130_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
