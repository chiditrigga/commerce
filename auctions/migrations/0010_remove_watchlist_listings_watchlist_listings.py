# Generated by Django 5.1.1 on 2024-10-06 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='listings',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='auctions.auctionlisting'),
        ),
    ]