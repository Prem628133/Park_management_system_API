from rest_framework import serializers
from visitors.models import VisitorsDetails

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorsDetails
        fields = ['id', 'name', 'age', 'gender', 'ticket_price']  

