# Generated by Django 3.0.6 on 2021-01-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_testimoninials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, max_length=50)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('testimony', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Testimoninials',
        ),
    ]
