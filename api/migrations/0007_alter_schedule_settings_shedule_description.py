# Generated by Django 3.2.13 on 2022-07-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220723_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_settings',
            name='shedule_description',
            field=models.CharField(blank=True, default='Weekely  data sync', max_length=255, null=True),
        ),
    ]
