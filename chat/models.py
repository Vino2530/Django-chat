from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# Create your models here.
User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User,related_name='sent_messages',on_delete=CASCADE)
    receiver = models.ForeignKey(User,related_name='receive_messages',on_delete=CASCADE)
    message= models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)