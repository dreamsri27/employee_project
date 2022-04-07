from django.urls import path,include
from . import views

urlpatterns = [
    path('form', views.employee_form,name='employee_form'),
    path('',views.employee_list,name='employee_list'),
    path('deleteemp/<str:id>',views.deleteemp,name='deleteemp'),
    path('editemp',views.editemp,name="editemp"),
    path('partiform/<str:id>',views.partiform,name='partiform')
    
]
