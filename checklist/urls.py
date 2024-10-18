from django.urls import path
from . import views

urlpatterns = [
    path('', views.checklist, name='checklist'),
    path('create_checklist/', views.create_checklist, name='create_checklist'),
    path('checklist_service/', views.checklist_service, name='checklist_service'),
    path('checklist_mall/', views.checklist_mall, name='checklist_mall'),
    path('checklist_plazma/', views.checklist_plazma, name='checklist_plazma'),
    path('checklist_nagornoe/', views.checklist_nagornoe, name='checklist_nagornoe'),
]
