# Generated by Django 3.2.6 on 2023-09-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0013_remove_result_date_attempted'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date_attempted',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]