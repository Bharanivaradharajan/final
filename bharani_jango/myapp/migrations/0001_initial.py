# Generated by Django 4.2.2 on 2023-06-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.IntegerField(default='')),
                ('Address', models.CharField(default='', max_length=20)),
                ('Contact', models.IntegerField(default='')),
                ('Mail', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
