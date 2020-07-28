# Generated by Django 3.0.8 on 2020-07-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artText', models.TextField()),
                ('artDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
