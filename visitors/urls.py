from django.urls import path
from visitors.views import VisitorsList,VisitorsDetail,CheckPrice,VisitorsStats

urlpatterns = [
    path('visitors/', VisitorsList.as_view(), name='VisitorsListCreate'),
    path('visitors/<int:pk>/', VisitorsDetail.as_view(), name='visitorDetails'),
    path('prices/', CheckPrice.as_view(), name='CheckPrice'),
    path('visitor-stats/', VisitorsStats.as_view(), name='check-visitors'),
]
