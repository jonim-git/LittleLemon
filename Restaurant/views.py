from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer  # Use the BookingSerializer you defined in Step 2
