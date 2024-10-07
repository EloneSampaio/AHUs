import requests
from django.http import JsonResponse
from django.core.cache import cache
from django.shortcuts import render


MICROSERVICE1_URL = 'http://localhost:5001/dados_ahu301'
MICROSERVICE2_URL = 'http://localhost:5002/dados_ahur01'

# View para consumir dados do microservice1
def microservice1_view(request):
    data = cache.get('microservice1_data')
    if not data:
        try:
            response = requests.get(MICROSERVICE1_URL)
            data = response.json()
            cache.set('microservice1_data', data, timeout=60*0.05)  # Cache por 5 minutos
        except requests.ConnectionError:
            data = {"error": "Microservice 1 is down"}
    
    return render(request, 'dashboard/microservice1.html', {'data': data})

# View para consumir dados do microservice2
def microservice2_view(request):
    data = cache.get('microservice1_data')
    if not data:
        try:
            response = requests.get(MICROSERVICE2_URL)
            data = response.json()
            cache.set('microservice1_data', data, timeout=60*0.05)  # Cache por 5 minutos
        except requests.ConnectionError:
            data = {"error": "Microservice 2 is down"}
    
    return render(request, 'dashboard/microservice2.html', {'data': data})