# Generated by Django 4.2.7 on 2024-04-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_blog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]