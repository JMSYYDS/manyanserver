# Generated by Django 4.0.2 on 2022-07-31 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='head_img',
            field=models.TextField(null=True),
        ),
    ]