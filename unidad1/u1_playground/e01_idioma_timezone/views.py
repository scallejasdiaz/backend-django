from django.http import HttpResponse
from django.utils import timezone

def ahora(request):
    ahora_local = timezone.now().strftime("%Y-%m-%d %H:%M:%S %Z")
    return HttpResponse(f"Fecha/Hora local: {ahora_local}")