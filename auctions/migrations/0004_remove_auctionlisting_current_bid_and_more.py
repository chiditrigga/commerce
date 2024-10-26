# Generated by Django 5.1.1 on 2024-10-04 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionlisting_bid_comment_watchlist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='current_bid',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='listings',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]