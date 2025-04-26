from django.urls import path
from . import views

app_name = 'tweet' 

urlpatterns = [
    path('', views.all_tweet, name='all_tweet' ),
    path('tweet/create/', views.tweet_create, name='tweet_create' ),
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit' ),
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete' ),
    path('register/', views.register, name='register' ),
    

] 