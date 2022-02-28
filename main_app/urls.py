import requests
from django.urls import path
from . import views

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token 9cc1c059bee7ea41a3ce614958f8c9a9ed9a8133'
        }
requestResponse = requests.get("https://api.tiingo.com/api/test?token=9cc1c059bee7ea41a3ce614958f8c9a9ed9a8133",
                                    headers=headers)
print(requestResponse.json())

urlpatterns = [
    path('', views.home, name= 'home'),
    # path('stocks/', views.StockCreate, name='stockcreate')
]
