# Generated by Django 2.2.3 on 2019-07-17 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appetizer', '0002_auto_20190718_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make_reservation',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
