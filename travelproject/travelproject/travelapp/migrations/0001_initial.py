# Generated by Django 3.2.13 on 2022-06-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('img', models.ImageField(upload_to='photos')),
                ('dist', models.TextField()),
            ],
        ),
    ]
