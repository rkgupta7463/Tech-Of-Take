# Generated by Django 4.0.6 on 2022-10-27 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogshort_web_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog_Dis',
        ),
        migrations.DeleteModel(
            name='BlogShort',
        ),
    ]
