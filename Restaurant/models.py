from django.db import models

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)  
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField()  
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name  

class MenuItem(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField()  

    def __str__(self):
       return f'{self.Title} : {str(self.Price)}'
