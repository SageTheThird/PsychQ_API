# Generated by Django 2.2.5 on 2019-09-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_post_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='universal_count',
            field=models.IntegerField(),
        ),
    ]
