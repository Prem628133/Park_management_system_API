from rest_framework import serializers
from visitors.models import VisitorsDetails

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorsDetails # Specify the model associated with this serializer
        fields = ['id', 'name', 'age', 'gender', 'ticket_price']  # Specify the fields to include

