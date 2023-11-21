from app1.views import *
from django.urls import path

app_name='firstapp'

urlpatterns=[
    path('application1/',application1,name='application1'),
]