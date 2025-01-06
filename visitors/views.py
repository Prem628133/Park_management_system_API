from visitors.models import VisitorsDetails
from visitors.serializers import VisitorSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

#To list and create visitors

class VisitorsList(generics.ListCreateAPIView):
    queryset = VisitorsDetails.objects.all()
    serializer_class = VisitorSerializer


# To retrieve, update and delete
class VisitorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisitorsDetails.objects.all()
    serializer_class = VisitorSerializer



class CheckPrice(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        age = request.query_params.get('age', None)

        # Base ticket price
        base_price = 50

        if age is None:
            return Response({
                "error": "Age is required. Provide it as a query parameter, e.g., ?age=25."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            age = int(age)
        except ValueError:
            return Response({"error": "Invalid age format."}, status=status.HTTP_400_BAD_REQUEST)

        # Discount based on age
        if age < 18:
            discount = 0.10  # 10% discount for children
            message = "Children (under 18): 10% discount applied."
        elif age > 60:
            discount = 0.05  # 5% discount for senior citizens
            message = "Senior Citizens (above 60): 5% discount applied."
        else:
            discount = 0.0  
            message = "Regular: No discount applied."

        # Calculate the final ticket price after applying the discount
        final_price = base_price - (base_price * discount)

        return Response({
            "message": message,
            "Base Price": f"{base_price} Rs",
            "Discount": f"{int(discount * 100)}%",
            "Final Price": f"{final_price:.2f} Rs"
        })


class VisitorsStats(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        total_visitors = VisitorsDetails.objects.count()
        total_revenue = sum(
            VisitorsDetails.objects.values_list("ticket_price", flat=True)
        )

        return Response({
            "Total Visitors": total_visitors,
            "Total Revenue": f"{total_revenue} Rs"
        })