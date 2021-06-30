from django.contrib import admin
from django.urls import include
from django.urls import path
from . import  views
app_name='predict'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('predict/',views.predict_chances,name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('classifIntern/', views.classifIntern, name='classifIntern'),
    path('predict_excel/', views.predict_excel, name='predict_xl'),
    path('chatroom/', views.index, name='chatroom'),
    path('External/', views.External, name='External'),
    
    
]
