# Generated by Django 4.1.7 on 2023-04-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('Desc', models.TextField()),
            ],
        ),
    ]