# Generated by Django 2.0.7 on 2018-07-09 08:15

from django.db import migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0008_auto_20180708_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apirequest',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AlterModelOptions(
            name='exchange',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AddField(
            model_name='apirequest',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apirequest',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='ask',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ask',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='bid',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exchange',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterUniqueTogether(
            name='ask',
            unique_together={('timestamp', 'exchange', 'pair', 'value', 'volume')},
        ),
        migrations.AlterUniqueTogether(
            name='bid',
            unique_together={('timestamp', 'exchange', 'pair', 'value', 'volume')},
        ),
    ]
