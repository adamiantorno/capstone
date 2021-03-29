from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import User, FriendRequest, Vehicle, Footprint, Race, Profile
from .calculate import kmToCarbon
from .forms import VehicleForm, TravelForm


# Create your views here.
@login_required
def input(request):    
    if request.method == 'POST':
        form1 = VehicleForm(request.POST)
        form2 = TravelForm(current_user=request.user, data=request.POST)
        if all(form1.is_valid(), form2.is_valid()): #server side validation
            v = form1.save()
            profile = Profile.objects.get_or_create(user=request.user)
            profile.vehicle.add(v)

            if (form2.cleaned_data['vehicle'] == 'Add New Vehicle'):
                kmToCarbon(form2.cleaned_data['distance'], v.style, request.user)
            else:
                kmToCarbon(form2.cleaned_data['distance'], form2.cleaned_data['vehicle'].style, request.user)

            return HttpResponseRedirect(f'/profile/{request.user.username}')
    else:
        form1 = VehicleForm()
        form2 = TravelForm(current_user=request.user)
        
    return render(request, 'greenfoot/input.html', {
        'vehicleForm': form1,
        'travelForm': form2
    })


def footprint(request):    
    # query for footprint
    try: 
        footprint = Footprint.objects.get(user=request.user)
    except Footprint.DoesNotExist:
        return JsonResponse({'error': 'Footprint not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse(footprint.serialize())
    # Footprint must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)


@login_required
def profile(request, username):
    # get profile objects and info
    profile_user = User.objects.get(username=username)
    profile = Profile.objects.get_or_create(user=profile_user)[0]

    if profile_user != request.user:
        friend_request = FriendRequest.objects.filter(
            to_user=profile_user, from_user=request.user).exists()

        return render(request, "greenfoot/profile.html", {
            'user': profile_user,
            'profile': profile,
            'requested': friend_request
        })
    
    return render(request, "greenfoot/profile.html", {
        'user': profile_user,
        'profile': profile,
        'requested': False
    })


def racelist(request):
    return render(request, 'greenfoot/racelist.html')


def race(request, pk):
    return render(request, 'greenfoot/race.html')

@login_required
def friends(request):
    allusers = User.objects.all()
    all_friend_requests = FriendRequest.objects.filter(to_user=request.user)
    return render(request, 'greenfoot/users.html', {
        'allusers': allusers,
        'all_friend_requests': all_friend_requests
    })


@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user
    )
    if created:
        return HttpResponse(status=204)
    else:
        return HttpResponse('friend request was already sent')


@login_required
def accept_friend_request(request, requestID):
    friend_request = FriendRequest.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('friend request not accepted')


@login_required
def decline_friend_request(request, requestID):
    pass


@login_required
def remove_friend(request, userID):
    friend = User.objects.get(id=userID)
    request.user.friends.remove(friend)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password mathes
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'greenfoot/login.html', {
                'r-message': 'Passwords must match!'
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, 'greenfoot/login.html', {
                'r_message': 'Email address is already taken'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('friends'))
    else:
        return render(request, 'greenfoot/login.html')



def login_view(request):
    if request.method == 'POST':
        
        # Attempt to sign in User
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('friends'))
        else:
            return render(request, 'greenfoot/login.html', {
                'l_message': 'Invalid username and/or password'
            })
    else:
        return render(request, 'greenfoot/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))