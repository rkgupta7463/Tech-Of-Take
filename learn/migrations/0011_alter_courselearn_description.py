# Generated by Django 4.0.6 on 2022-12-24 13:45

from django.db import migrations,models

class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_alter_trendingmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselearn',
            name='description',
            field=models.TextField(),
        ),
    ]
