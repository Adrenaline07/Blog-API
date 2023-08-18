# Generated by Django 4.2.4 on 2023-08-18 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('firstname', models.CharField(max_length=25, null=True)),
                ('lastname', models.CharField(max_length=25, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posttitle', models.CharField(max_length=50)),
                ('postcontent', models.CharField(max_length=1500)),
                ('postdate', models.DateField(max_length=50)),
                ('postOwner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppBlog.user')),
            ],
        ),
    ]
