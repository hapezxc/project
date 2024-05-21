




# models.py
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    method = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_type = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    room_quantity = models.IntegerField()
    placed_on = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room_type}"


# myapp/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
