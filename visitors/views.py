from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from visitors.models import visitors_details
from visitors.serializers import visitorSerializer


#To list and create visitors

@api_view(['GET', 'POST'])
def visitor_list_create(request):
    if request.method == 'GET':
        visitors = visitors_details.objects.all()
        serializer = visitorSerializer(visitors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = visitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# To retrieve, update and delete
@api_view(['GET', 'PUT', 'DELETE'])
def visitor_detail(request, pk):
    try:
        visitor = visitors_details.objects.get(pk=pk)
    except visitor.DoesNotExist:
        return Response({"error": "Visitor not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = visitorSerializer(visitor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = visitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        visitor.delete()
        return Response({"message": "Visitor deleted"}, status=status.HTTP_204_NO_CONTENT)   
    




# For ticket prices
@api_view(['GET'])
def check_prices(request):
    prices = {
        "Children (under 18)": "10% discount, Ticket Price = 45 Rs",
        "Senior Citizens (above 60)": "5% discount, Ticket Price = 47 Rs",
        "Regular": "Ticket Price = 50 Rs"
    }
    return Response(prices)    




#For visitor statistics
@api_view(['GET'])
def check_visitors(request):
    total_visitors = visitors_details.objects.count()
    total_revenue = sum(visitor.ticket_price for visitor in visitors_details.objects.all())
    return Response({
        "Total Visitors": total_visitors,
        "Total Revenue": f"{total_revenue} Rs"
    })

