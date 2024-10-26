from django.contrib import admin
from .models import AuctionListing, Bid, Watchlist,Comment

admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)
# Register your models here.
