# Generated by Django 4.1.7 on 2023-03-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_remove_employee_device_employee_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='device_return',
            name='payment_method',
            field=models.CharField(choices=[('SSLcommerz', 'SSLcommerz')], default=('SSLcommerz', 'SSLcommerz'), max_length=30),
        ),
    ]
