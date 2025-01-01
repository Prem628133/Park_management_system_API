from rest_framework import serializers
from visitors.models import visitors_details

class visitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = visitors_details # Specify the model associated with this serializer
        fields = ['id', 'name', 'age', 'gender', 'ticket_price']  # Specify the fields to include

