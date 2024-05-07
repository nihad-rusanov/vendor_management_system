from django.db import models
from django.db.models import F ,Avg
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def update_on_time_delivery_rate(self):
        completed_purchases = self.purchaseorder_set.filter(status='completed')
        total_completed = completed_purchases.count()
        if total_completed > 0:
            on_time_delivered = completed_purchases.filter(delivery_date__lte=F('acknowledgment_date')).count()
            self.on_time_delivery_rate = (on_time_delivered / total_completed) * 100
        else:
            self.on_time_delivery_rate = 0
        self.save()

    def update_quality_rating_avg(self):
        completed_purchases = self.purchaseorder_set.filter(status='completed').exclude(quality_rating__isnull=True)
        total_completed = completed_purchases.count()
        if total_completed > 0:
            self.quality_rating_avg = completed_purchases.aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        else:
            self.quality_rating_avg = 0
        self.save()

    def update_average_response_time(self):
        acknowledged_purchases = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        total_acknowledged = acknowledged_purchases.count()
        if total_acknowledged > 0:
            avg_response_time = acknowledged_purchases.aggregate(avg_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_time']
            self.average_response_time = avg_response_time.total_seconds() / 3600  # Convert to hours
        else:
            self.average_response_time = 0
        self.save()

    def update_fulfillment_rate(self):
        total_orders = self.purchaseorder_set.count()
        if total_orders > 0:
            fulfilled_orders = self.purchaseorder_set.filter(status='completed').count()
            self.fulfillment_rate = (fulfilled_orders / total_orders) * 100
        else:
            self.fulfillment_rate = 0
        self.save()

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
