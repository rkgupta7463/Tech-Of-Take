# Generated by Django 4.0.6 on 2022-10-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Dis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='blog_overview/')),
                ('title', models.CharField(max_length=250)),
                ('discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='blog_overview/')),
                ('title', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('web_link', models.TextField()),
            ],
        ),
    ]
