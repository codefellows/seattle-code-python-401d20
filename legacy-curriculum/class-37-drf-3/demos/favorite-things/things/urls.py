from django.urls import path
from . import views

urlpatterns = [
    path('things/', views.ThingList.as_view()),
    path('things/<int:pk>/', views.ThingDetail.as_view()),
]