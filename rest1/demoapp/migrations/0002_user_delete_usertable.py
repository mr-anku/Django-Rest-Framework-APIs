# Generated by Django 4.0.3 on 2022-03-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='UserTable',
        ),
    ]
