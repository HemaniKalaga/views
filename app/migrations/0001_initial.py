# Generated by Django 4.2.7 on 2024-02-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100)),
                ('bauthor', models.CharField(max_length=100)),
            ],
        ),
    ]