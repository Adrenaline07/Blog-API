# Generated by Django 4.2.4 on 2023-08-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_remove_post_postownersusername_post_post_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_owner',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
