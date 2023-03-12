from django.urls import path
from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView

urlpatterns = [
    path('', ItemListCreateView.as_view(), name='item-list-create'),
    path('<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-retrieve-update-destroy'),
]