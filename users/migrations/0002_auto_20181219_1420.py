# Generated by Django 2.1.4 on 2018-12-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adress',
            field=models.CharField(blank=True, default='null', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('-', 'empty'), ('M', 'Male'), ('F', 'Female')], default='-', max_length=1, null=True),
        ),
    ]