# Generated by Django 3.1.3 on 2020-11-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=50)),
                ('toppings', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
    ]
