# Generated by Django 2.2.5 on 2019-10-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_question_creater_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.AutoField(default='default value', primary_key=True, serialize=False),
        ),
    ]
