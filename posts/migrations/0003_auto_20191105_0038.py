# Generated by Django 2.2.6 on 2019-11-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_custom_ordering'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='storage_link',
            new_name='full_res_image',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(help_text='Thumbnail Slug of the image', max_length=1000, null=True),
        ),
    ]
