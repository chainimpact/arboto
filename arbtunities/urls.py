from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('monitor/', views.monitor, name='monitor'),
    path('monitor/rois', views.rois, name='rois'),
    path('api/', views.monitor_data, name='monitor_data'),
    path('api/rois', views.get_hi_bids_and_lo_asks, name='get_hi_bids_and_lo_asks'), 
]