# Generated by Django 3.2.4 on 2021-07-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_number_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='number',
            field=models.IntegerField(),
        ),
    ]
