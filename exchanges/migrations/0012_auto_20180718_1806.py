# Generated by Django 2.0.7 on 2018-07-18 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0011_auto_20180709_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ask',
            options={'ordering': ('timestamp',)},
        ),
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ('timestamp',)},
        ),
    ]
