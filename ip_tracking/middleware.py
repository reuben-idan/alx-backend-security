from .models import RequestLog
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now

class IPTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR', '')
        path = request.path
        RequestLog.objects.create(ip_address=ip, timestamp=now(), path=path) 