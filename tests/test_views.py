from django.test import TestCase
from restaurant.models import MenuItem
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(Title="Item 1", Price=10, Inventory=100)
        self.menu_item2 = MenuItem.objects.create(Title="Item 2", Price=20, Inventory=50)

    def test_getall(self):
        
        response = self.client.get('/restaurant/menu/') 

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        
        self.assertEqual(response.data, serializer.data)
