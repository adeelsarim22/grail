from django.urls import path
from .views import (
    ParticipantsListCreate,
    ParticipantRUD
)


urlpatterns = [
    path('participants/', ParticipantsListCreate.as_view(),
         name="participants_list_create"),
    path('participant/<str:pk>/', ParticipantRUD.as_view(),
         name="participants_retrive_update_delete"),

]
