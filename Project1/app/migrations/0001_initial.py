# Generated by Django 3.1.7 on 2021-02-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.IntegerField(max_length=5)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]
