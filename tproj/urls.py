from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('passenger/new/', views.passenger_new, name='passenger_new'),
    path('trip/<int:pk>/', views.trip_new, name='trip_new'),
    path('ticket/<int:pk>/', views.ticket_new, name='ticket_new'),
]
#path('tickets/<int:ticket_id>/',views.tickets_page, name='tickets'),
#path('trips/<int:trip_id>/',views.trips_page, name='trips'),
#re_path(r'^from/(?P<start_station>[0-9]{1,50})/$', views.details_page, name='details_page'),
#path('', views.details_page, name='booking'),
