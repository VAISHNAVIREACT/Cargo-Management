# Generated by Django 5.0.4 on 2024-04-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('shipping_date', models.DateField()),
            ],
        ),
    ]