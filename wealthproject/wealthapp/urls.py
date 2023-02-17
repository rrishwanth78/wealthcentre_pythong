from django.urls import path
from wealthapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('alerts/', views.alerts, name = 'alerts'),

    path('forms-elements/', views.forms_elements, name = 'forms-elements'),
    path('forms-layouts/', views.forms_layouts, name = 'forms-layouts'),
    path('forms-validation/', views.forms_validation, name = 'forms-validation'),
]
