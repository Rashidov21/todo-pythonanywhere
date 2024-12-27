# Generated by Django 4.2.2 on 2024-12-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550, verbose_name='Todo title')),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]