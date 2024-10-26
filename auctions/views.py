from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import AuctionListing,Comment, Watchlist
from .forms import AuctionListingForm, BidForm,CommentForm
from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import User


def index(request):
    listings = AuctionListing.objects.filter(is_active=True)
  
    return render(request, "auctions/index.html", {
        "listings": listings,
        
    })

def closed(request):
    listings = AuctionListing.objects.filter(is_active=False)
    
  
    return render(request, "auctions/closed.html", {
        "listings": listings,
        
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")




@login_required(login_url=reverse_lazy('login'))
def create_listing(request):
    if request.method == 'POST':
        form = AuctionListingForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.created_by = request.user
            auction.save()
            return redirect('index')
    else:
        form = AuctionListingForm()
    return render(request, 'auctions/create_listing.html', {'form': form})






#listing details

def listing_detail(request, listing_id):
    auction = AuctionListing.objects.get(pk=listing_id)
    detail = AuctionListing.objects.get(pk=listing_id)
    listing = get_object_or_404(AuctionListing, id=listing_id)
    if request.user.is_authenticated:
     watchlist, created = Watchlist.objects.get_or_create(user=request.user)
     mode = False
     if listing in watchlist.listings.all():
        mode = True
     else:
        mode = False
    else:
        mode = False
        pass
 
    # Get all comments related to this auction
    comments = auction.comments.all()

    if 'content' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a comment instance but don't save it to the database yet
            comment = form.save(commit=False)
            # Set the author and auction before saving
            comment.author = request.user
            comment.auction = auction
            comment.save()

            return redirect('listing_detail', listing_id=listing_id)
        
    elif 'amount' in request.POST:
        
            
                 bid_form = BidForm(request.POST)
                 if bid_form.is_valid():
                      bid = bid_form.save(commit=False)
                      bid.bidder = request.user
                      bid.auction = listing
                      if bid.amount >= listing.starting_bid and (listing.current_bid is None or bid.amount > listing.current_bid.amount):
                         bid.save()
                         listing.current_bid = bid
                         listing.save()
                         return redirect('listing_detail', listing_id=listing_id)
                      else:
                            error = "Bid must be higher than the current highest bid or starting bid."
                            return render(request, 'auctions/listing_detail.html', 
                                        {
                                            "form": AuctionListingForm(),
                                            "details": detail,
                                            "comments": comments,
                                            "bid_form":BidForm() ,
                                            'error': error,
                                         })

    else:
      return render(request, 'auctions/listing_detail.html', {
         "form": CommentForm(),
         "details": detail,
        "comments": comments,
         "bid_form":BidForm(),
         "mode":mode
         
            })



# Add or remove from watchlist


@login_required(login_url=reverse_lazy('login'))
def toggle_watchlist(request, listing_id):
    # Get the auction listing
    detail = get_object_or_404(AuctionListing, pk=listing_id)
    
    # Get or create the user's watchlist
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
 
    if detail in watchlist.listings.all():
  
        watchlist.listings.remove(detail)
    else:

        watchlist.listings.add(detail)
    
  
    watchlist.save()

    return redirect('watchlist')








@login_required(login_url=reverse_lazy('login'))
def watchlist(request):
    # Get or create a watchlist for the current user
    user_watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    
    # Get the listings in the watchlist
    listings = user_watchlist.listings.all()  

    return render(request, 'auctions/watchlist.html', {
        "watch": listings,
        "watch_count": listings.count()  
    })


#categories 


def categories(request):
    # Get distinct categories and count the number of items in each category
    categories = AuctionListing.objects.values('category').annotate(count=Count('category')).distinct()

    return render(request, 'auctions/categories.html', {
        "categories": categories
    })



def categories_listing(request,listing_id):
    listings = AuctionListing.objects.filter(category = listing_id)
    return render(request, 'auctions/categories_details.html', {
        "listings":listings
    })


def active(request, listing_id):
    # Get the AuctionListing object by its id
    listing = get_object_or_404(AuctionListing, id=listing_id)
    
    # Update is_active to False
    listing.is_active = False
    listing.save()

    # Redirect to the same page or another page
    # return HttpResponseRedirect(request.path_info)    
    return redirect('listing_detail', listing_id=listing_id)


   
    



