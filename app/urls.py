from django.urls import path
from . views import *

urlpatterns = [
    path('', employee_list, name='employee-list'),
    path('employee/', employee, name='employee'),
    path('employee/<pk>/', employee_update, name='employee-update'),
    path('search/', search_employee, name='employee-search'),
    path('delete/<pk>/', delele_employee, name='employee-delete'),
    
]
