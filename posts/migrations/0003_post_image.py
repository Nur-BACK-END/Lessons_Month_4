# Generated by Django 5.1.4 on 2025-01-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_rate_alter_post_content_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
