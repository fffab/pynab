# Generated by Django 2.2.6 on 2019-12-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nabairqualityd', '0003_auto_20191211_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='latitude',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='config',
            name='longitude',
            field=models.TextField(null=True),
        ),
    ]
