# Generated by Django 3.1.7 on 2021-03-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210304_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='children',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='license',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, choices=[('사장', '사장'), ('상무', '상무'), ('부장', '부장'), ('차장', '차장'), ('과장', '과장'), ('대리', '대리'), ('주임', '주임'), ('사원', '사원')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='working_place',
            field=models.CharField(blank=True, choices=[('안양', '안양'), ('천안', '천안')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]