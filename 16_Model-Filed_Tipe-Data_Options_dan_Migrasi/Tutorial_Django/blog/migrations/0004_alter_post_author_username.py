# Generated by Django 3.2.15 on 2022-12-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20221218_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_username',
            field=models.CharField(default='anonym', max_length=20),
        ),
    ]
