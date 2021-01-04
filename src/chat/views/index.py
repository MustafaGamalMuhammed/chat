from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat.models import FriendshipRequest, Profile


@api_view(['GET'])
def search(request, q):
    profiles = Profile.objects.filter(user__username__icontains=q)
    profiles = profiles.exclude(user__username=request.user.username)
    profiles = profiles.annotate(username=F("user__username"))

    return Response(data=profiles.values())


@api_view(['POST'])
def create_friendship_request(request):
    profile = get_object_or_404(Profile, id=request.data.get('id'))
    friendship_request = FriendshipRequest(
            sender=request.user.profile, 
            receiver=profile)
    friendship_request.save()

    return Response(data=friendship_request.__dict__)


@api_view(['POST'])
def accept_friendship_request(request):
    friendship_request = get_object_or_404(
            FriendshipRequest, 
            id=request.data.get('id'))
    friendship_request.accepted = True
    friendship_request.save()
   
    return Response(data=friendship_request.__dict__)


@login_required
def index(request):
    return render(request, "chat/index.html")
