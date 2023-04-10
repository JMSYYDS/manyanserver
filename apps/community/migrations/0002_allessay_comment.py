# Generated by Django 4.0.2 on 2023-03-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllEssay',
            fields=[
                ('essayId', models.AutoField(primary_key=True, serialize=False)),
                ('essayAuthor', models.CharField(max_length=200)),
                ('essayTitle', models.CharField(max_length=200)),
                ('essayContent', models.TextField()),
                ('essayTime', models.CharField(max_length=100)),
                ('essaySupport', models.IntegerField(default=0)),
                ('essayClicks', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'allessay',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('essayId', models.IntegerField()),
                ('commentContent', models.TextField()),
                ('commentTime', models.CharField(max_length=100)),
                ('commentAuthor', models.CharField(max_length=200)),
                ('commentClicks', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]