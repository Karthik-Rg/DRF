# Generated by Django 3.0.8 on 2020-07-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200714_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
