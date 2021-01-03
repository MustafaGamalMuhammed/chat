from django.shortcuts import render
from django.db.models import F
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat.models import Profile


@api_view(['GET'])
def search(request, q):
    profiles = Profile.objects.filter(user__username__icontains=q)
    profiles = profiles.exclude(user__username=request.user.username)
    profiles = profiles.annotate(username=F("user__username"))

    return Response(data=profiles.values())


@login_required
def index(request):
    return render(request, "chat/index.html")
