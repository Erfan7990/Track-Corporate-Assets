# Generated by Django 4.1.7 on 2023-03-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_device_feedback_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='PaymentID',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
