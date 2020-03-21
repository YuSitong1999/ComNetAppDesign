# Generated by Django 3.0.4 on 2020-03-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_id', models.IntegerField()),
                ('number', models.IntegerField(default=1)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('register_date', models.DateField()),
            ],
        ),
    ]