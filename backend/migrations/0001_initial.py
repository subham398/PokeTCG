# Generated by Django 3.1.2 on 2020-10-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('identity', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=100)),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]