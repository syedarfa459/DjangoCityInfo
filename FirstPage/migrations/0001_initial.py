# Generated by Django 3.0.5 on 2020-04-28 10:31

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
                ('UserName', models.CharField(max_length=50)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('City', models.CharField(max_length=20)),
                ('Useradvice', models.CharField(max_length=300)),
            ],
        ),
    ]
