# Generated by Django 3.2.4 on 2021-06-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comments_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default='2000-01-01'),
            preserve_default=False,
        ),
    ]
