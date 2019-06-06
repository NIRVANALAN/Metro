# Generated by Django 2.2.1 on 2019-05-29 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('operation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=50)),
                ('app_name', models.CharField(default='', max_length=20)),
                ('view_name', models.CharField(default='', max_length=20)),
                ('role_belong_to', models.IntegerField(default=4)),
                ('parent_operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operation.Operation')),
            ],
        ),
    ]
