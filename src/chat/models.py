from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("Profile")
    image = models.ImageField(upload_to="profile_pics", default="default.jpg")

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        im = Image.open(self.image)
        width, height = im.size

        if width > 200 or height > 200:
            im.thumbnail((300, 300), Image.ANTIALIAS)
            im.save(self.image.path)


class Room(models.Model):
    name = models.CharField(max_length=150, unique=True)
    admins = models.ManyToManyField(Profile, related_name="admin_rooms")
    users = models.ManyToManyField(Profile, related_name="rooms")

    def __str__(self):
        return self.name

    @classmethod
    def create_from_friendrequest(cls, friendrequest):
        sender, receiver = friendrequest.sender, friendrequest.receiver

        if sender.id < receiver.id:
            name = f"{sender.id}-{receiver.id}"
        else:
            name = f"{receiver.id}-{sender.id}"

        room = Room.objects.create(name=name)
        room.admins.add(sender, receiver)
        room.users.add(sender, receiver)


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="messages")
    content = models.CharField(max_length=400)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.user.username}: {self.content[:50]}..."


class FriendshipRequest(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="requests")
    sent_at = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.user.username} to " + \
            f"{self.receiver.user.username}"

    def save(self, *args, **kwargs):
        super(FriendshipRequest, self).save(*args, **kwargs)

        if self.accepted:
            self.sender.friends.add(self.receiver)
            self.receiver.friends.add(self.sender)
            Room.create_from_friendrequest(self)
