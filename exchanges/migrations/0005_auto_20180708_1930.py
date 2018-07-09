# Generated by Django 2.0.7 on 2018-07-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0004_auto_20180708_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='pair',
            field=models.CharField(choices=[('ETHEUR', 'ETHER-EURO'), ('ETHBTC', 'ETHER-BITCOIN'), ('ETHCLP', 'ETHER-PESOS'), ('BTCCLP', 'BITCOIN-PESOS'), ('LTCBTC', 'LITECOIN-BITCOIN'), ('BCHBTC', 'BITCOINCASH-BITCOIN')], default='ETHEUR', max_length=6),
        ),
        migrations.AddField(
            model_name='ask',
            name='volume',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='pair',
            field=models.CharField(choices=[('ETHEUR', 'ETHER-EURO'), ('ETHBTC', 'ETHER-BITCOIN'), ('ETHCLP', 'ETHER-PESOS'), ('BTCCLP', 'BITCOIN-PESOS'), ('LTCBTC', 'LITECOIN-BITCOIN'), ('BCHBTC', 'BITCOINCASH-BITCOIN')], default='ETHEUR', max_length=6),
        ),
        migrations.AddField(
            model_name='bid',
            name='volume',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12),
            preserve_default=False,
        ),
    ]