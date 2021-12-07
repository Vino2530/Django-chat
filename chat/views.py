from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import User,Message
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
import json
from django.db.models import Q
# Create your views here.
@login_required
def chatroom(request,pk:int):
    other_user = get_object_or_404(User,pk=pk)
    messages= Message.objects.filter(
        Q(receiver=other_user,sender=request.user)|Q(receiver=request.user,sender = other_user)
    )
    messages.update(seen=True)
    context = {
        'other_user': other_user,'messages':messages
    }
    return render(request,'chatroom.html',context)