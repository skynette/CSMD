# Generated by Django 3.0.6 on 2021-01-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimoninials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, max_length=50)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('testimony', models.TextField(blank=True, max_length=100)),
            ],
        ),
    ]