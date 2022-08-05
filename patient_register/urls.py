from django.urls import path,include
from . import views
urlpatterns = [
    path('insert/', views.patient_form, name='patient_insert'), 
    path('insert/<int:id>/', views.patient_form, name='patient_update'),
    path('prescription/', views.patient_prescription, name='patient_prescription'),
    path('delete/<int:id>/', views.patient_delete, name='patient_delete'), 
    path('list/', views.patient_list, name='patient_list'),
    path('', views.patient_home, name='patient_home')
]