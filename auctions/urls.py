from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("login", views.login_view, name="login"),
#     path("logout", views.logout_view, name="logout"),
#     path("register", views.register, name="register"),
#     # path('comment/<int:user_id>/', views.comment, name='comment'),
#     # path('listings', views.active_listings, name='listings'),
#     path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
#     path('create/', views.create_listing, name='create_listing'),
#     # path('listing/<int:listing_id>/watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
# ]
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("closed", views.closed, name="closed"),
    path("active/<int:listing_id>", views.active, name="active"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:listing_id>", views.categories_listing, name="categories_listing"),
    path("register", views.register, name="register"),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('create/', views.create_listing, name='create_listing'),
    path('listing/<int:listing_id>/watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
]

