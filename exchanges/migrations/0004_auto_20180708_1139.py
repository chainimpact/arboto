# Generated by Django 2.0.7 on 2018-07-08 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0003_auto_20180708_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='api_request',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='exchanges.ApiRequest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='api_request',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='exchanges.ApiRequest'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='price_type',
            field=models.CharField(choices=[('a', 'ask'), ('b', 'bid')], default='b', max_length=1),
        ),
    ]
