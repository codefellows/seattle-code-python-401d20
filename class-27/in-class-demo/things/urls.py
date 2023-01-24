from django.urls import path

from .views import HomePageView, ThingDetailView, ThingListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('thing/', ThingListView.as_view(), name='thing_list'),
    path('thing/<int:pk>/', ThingDetailView.as_view(), name='thing_detail'),
]
