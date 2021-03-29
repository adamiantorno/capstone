from django.urls import path

from . import views

urlpatterns = [
    path('input', views.input, name='input'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('races', views.racelist, name='racelist'),
    path('race/<int:pk>', views.race, name='race'),
    path('', views.friends, name='friends'),

    # friend request urls
    path('send_friend_request/<int:userID>', views.send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:requestID>', views.accept_friend_request, name='accept friend request'),
    path('decline_friend/<int:requestID>', views.decline_friend_request, name='decline friend request'),
    path('remove_friend/<int:userID>', views.remove_friend, name='remove friend'),
    

    # Login, Logout, Register
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    # API Routes
    path('footprint', views.footprint, name='footprint')
]