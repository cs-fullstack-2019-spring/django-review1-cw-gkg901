# Generated by Django 2.0.6 on 2019-02-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('alcoholPercentage', models.IntegerField(default=0, max_length=20)),
                ('servingGlass', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
