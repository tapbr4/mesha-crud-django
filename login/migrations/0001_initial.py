# Generated by Django 4.0.4 on 2022-05-15 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('admin', models.BooleanField()),
            ],
        ),
    ]
