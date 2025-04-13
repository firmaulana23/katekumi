from rest_framework import viewsets
from .models import Item, Purchase, Sell
from .serializers import ItemSerializer, PurchaseSerializer, SellSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from datetime import datetime

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(is_deleted=False)
    serializer_class = ItemSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class StockReportView(APIView):
    def get(self, request, item_code):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use yyyy-mm-dd."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch item
        item = Item.objects.filter(code=item_code).first()
        if not item:
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

        # Fetch purchases and sells within the date range
        purchases = Purchase.objects.filter(date__range=[start_date, end_date])
        sells = Sell.objects.filter(date__range=[start_date, end_date])

        # Prepare report data
        report_data = {
            "item_code": item.code,
            "name": item.name,
            "unit": item.unit,
            "stock_changes": []
        }

        # Add purchase details
        for purchase in purchases:
            report_data["stock_changes"].append({
                "date": purchase.date,
                "description": purchase.description,
                "in": purchase.details.aggregate(Sum('quantity'))['quantity__sum'] or 0,
                "out": 0
            })

        # Add sell details
        for sell in sells:
            report_data["stock_changes"].append({
                "date": sell.date,
                "description": sell.description,
                "in": 0,
                "out": sell.details.aggregate(Sum('quantity'))['quantity__sum'] or 0
            })

        return Response(report_data, status=status.HTTP_200_OK)