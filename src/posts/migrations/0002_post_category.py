# Generated by Django 2.1 on 2018-09-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='BOBASY', max_length=100),
            preserve_default=False,
        ),
    ]
