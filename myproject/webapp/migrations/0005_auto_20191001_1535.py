# Generated by Django 2.2.5 on 2019-10-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191001_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
