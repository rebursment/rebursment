from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_identity, name='add_identity'),
    path('card', views.add_card, name='add_card'),
    path('succeded', views.success, name='success'),
]
