# Generated by Django 5.0.1 on 2024-01-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kitob nomi')),
                ('books_author', models.CharField(max_length=50, verbose_name='Muallifi')),
                ('price', models.IntegerField(verbose_name='Narxi')),
            ],
            options={
                'verbose_name': 'Kitob ',
                'verbose_name_plural': 'Kitoblar ',
            },
        ),
    ]