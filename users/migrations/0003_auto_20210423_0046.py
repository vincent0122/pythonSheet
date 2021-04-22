# Generated by Django 3.1.7 on 2021-04-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210418_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='access_token',
        ),
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]
