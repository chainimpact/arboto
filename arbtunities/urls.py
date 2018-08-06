from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('monitor/', views.monitor, name='monitor'),
    path('monitor/rois', views.rois, name='rois'),
    path('monitor2/', views.monitor2, name='monitor2'),
    path('api/', views.monitor_data, name='monitor_data'),
    path('api/rois', views.rois_data, name='rois_data'),
    path('api/monitor2', views.monitor2_data, name='monitor2_data'),
]