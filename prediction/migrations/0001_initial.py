# Generated by Django 4.2 on 2023-05-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=10)),
                ('test', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
