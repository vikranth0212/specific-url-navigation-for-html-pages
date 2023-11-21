from app2.views import *
from django.urls import path

app_name='secondapp'

urlpatterns=[
    path('application2/',application2,name='application2'),
]