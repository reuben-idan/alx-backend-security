from django.db import models

# Create your models here.

class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.ip_address} at {self.timestamp} on {self.path}"
