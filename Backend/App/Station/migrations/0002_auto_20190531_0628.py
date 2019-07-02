# Generated by Django 2.2.1 on 2019-05-31 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Station', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='station_name',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_x_cor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_y_cor',
            field=models.IntegerField(default=0),
        ),
    ]
