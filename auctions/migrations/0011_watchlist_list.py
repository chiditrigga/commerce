# Generated by Django 5.1.1 on 2024-10-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_watchlist_listings_watchlist_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='list',
            field=models.Field(null=True),
        ),
    ]
