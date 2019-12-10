# Generated by Django 2.2.6 on 2019-12-10 15:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('product_id', models.CharField(help_text='Product id on which review is made', max_length=60)),
                ('user_id', models.CharField(help_text='id of the user who made the review', max_length=50)),
                ('title', models.CharField(help_text='Title of the review', max_length=100)),
                ('description', models.CharField(help_text='Body of the review', max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
