from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ItemList, ItemDetail

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/items/', ItemList.as_view(), name='item-list'),
    path('api/items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]