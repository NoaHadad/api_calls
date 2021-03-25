# Generated by Django 3.1.7 on 2021-03-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_quotelog_suit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotelog',
            name='suit',
        ),
        migrations.AddField(
            model_name='quotelog',
            name='operation',
            field=models.IntegerField(choices=[(1, 'Create'), (2, 'Update'), (3, 'Delete')], default=1),
        ),
    ]
