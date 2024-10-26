from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    CATEGORIES = [
        ('Fashion', 'Fashion'),
        ('Toys', 'Toys'),
        ('Electronics', 'Electronics'),
        ('Home', 'Home'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=64, choices=CATEGORIES, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)



    
    current_bid = models.ForeignKey('Bid', on_delete=models.SET_NULL, blank=True, null=True, related_name="current_bid")
    
    def __str__(self):
        return f"Title: {self.title} description: {self.description}" 

# Bid Model
class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids")
   

    def __str__(self):
        return f"Bid of {self.amount} by {self.bidder.username}"

# Comment Model
class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True,)  # Automatically set when the comment is created

    def __str__(self):
        return f"Comment by {self.author} on {self.auction}"

   


# Watchlist Model
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(AuctionListing, related_name="watchlist")

    def __str__(self):
        return f"Watchlist of {self.user.username}"