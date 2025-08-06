from django.db import models

# Create your models here.
class Oders(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_length=10, decimal_places=2)
    order_status = models.CharField(max_length= 20, choices= STATUS_CHOICES, default = 'pending')

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"