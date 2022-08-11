from django.shortcuts import render
from django.views import generic
from .models import Chat, Profile
from django.urls import reverse_lazy

#API imports
from rest_framework import generics
from .serializers import ChatSerializer


class RoomListView(generic.ListView):
    model = Chat
    template_name = 'index.html'

# def index(request):
#     return render(request, 'index.html')

class RoomDetailView(generic.DetailView):
    model = Chat
    template_name = 'room.html'

    slug_url_kwarg = 'room_name'
    slug_field = 'room_name'


class RoomUpdateView(generic.UpdateView):
    model = Chat
    template_name = 'update.html'
    fields = ['room_name', 'users']

    slug_url_kwarg = 'room_name'
    slug_field = 'room_name'

class RoomDeleteView(generic.DeleteView):
    model = Chat
    template_name = 'delete.html'
    success_url = reverse_lazy('chat:index')

    slug_url_kwarg = 'room_name'
    slug_field = 'room_name'

# def room(request, room_name):
#     return render(request, 'room.html', {'room_name': room_name})

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'profile.html'

class PrivateRoomDetailView(generic.DetailView):
    model = Profile
    template_name = 'private_room.html'

    slug_url_kwarg = 'name'
    slug_field = 'name'

class ProfileUpdateView(generic.UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['name', 'image']

# API VIEWS

class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer



