# Generated by Django 4.2.7 on 2023-12-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_courseinfo_image_alter_courseinfo_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='url_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
