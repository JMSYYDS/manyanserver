# Generated by Django 4.0.2 on 2023-03-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_allessay_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essayId', models.IntegerField()),
                ('supportAuthor', models.CharField(max_length=200)),
                ('isSupport', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'support',
            },
        ),
    ]