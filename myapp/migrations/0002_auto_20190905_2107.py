# Generated by Django 2.2.5 on 2019-09-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=255),
        ),
    ]
