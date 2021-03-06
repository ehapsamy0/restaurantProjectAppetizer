# Generated by Django 2.2.3 on 2019-07-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Happy_Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='cust_img')),
                ('bio', models.TextField()),
                ('cust_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Make_Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('how_meny_person', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider_title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slider_img', models.ImageField(upload_to='slider_img')),
            ],
        ),
    ]
