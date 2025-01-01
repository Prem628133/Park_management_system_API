from django.urls import path
from visitors.views import visitor_list_create, visitor_detail, check_prices, check_visitors

urlpatterns = [
    path('visitors/', visitor_list_create, name='visitor-list-create'),
    path('visitors/<int:pk>/', visitor_detail, name='visitor-detail'),
    path('prices/', check_prices, name='check-prices'),
    path('visitors-stats/', check_visitors, name='check-visitors'),
]
