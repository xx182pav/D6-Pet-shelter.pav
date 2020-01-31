from django.urls import path

from .views import (IndexPageView, PetListView, ContactsView, PetView)

urlpatterns = [
    path('', IndexPageView.as_view()),
    path('cats/', PetListView.as_view()),
    path('cats/<str:pk>/', PetView.as_view()),
    path('contacts/', ContactsView.as_view()),
]