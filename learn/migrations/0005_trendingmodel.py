# Generated by Django 4.0.6 on 2022-12-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_delete_coursedata_alter_courselearn_scription_learn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/trending/')),
            ],
        ),
    ]