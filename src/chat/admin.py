from django.contrib import admin
from chat.models import *


admin.site.register([Profile, Message, Room, FriendshipRequest])
