from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.RoomListView.as_view(), name='index'),
    path('<slug:room_name>/', views.RoomDetailView.as_view(), name='room'),
    path('<slug:room_name>/update/', views.RoomUpdateView.as_view(), name='room_update'),
    path('<slug:room_name>/delete/', views.RoomDeleteView.as_view(), name='room_delete'),
    path('<int:pk>/profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('<slug:name>/private/', views.PrivateRoomDetailView.as_view(), name='private_room'),

    # API
    path('api/v1/<int:pk>/', views.ChatDetail.as_view(), name='api_detail'),
    path('api/v1/', views.ChatList.as_view(), name='api_list'),
]