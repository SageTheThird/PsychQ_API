# Generated by Django 2.2.6 on 2019-12-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnsplashCategory',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(help_text='Name of the category', max_length=120, unique=True)),
                ('description', models.CharField(blank=True, help_text='Brief description of category', max_length=1300, null=True)),
                ('pic_top', models.CharField(max_length=300)),
                ('pic_left', models.CharField(max_length=300)),
                ('pic_right', models.CharField(max_length=300)),
                ('related_tags', models.CharField(help_text='Related searches that appear after search', max_length=500)),
                ('total_posts_count', models.IntegerField()),
            ],
        ),
    ]
