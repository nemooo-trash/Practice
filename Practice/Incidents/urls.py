from django.urls import path

from .views import *

urlpatterns = [
    # ------Incidents------
    path('', IncidentsView.as_view(), name='incidents-list'),
    path('<int:pk>/', IncidentDatail.as_view(), name='incident-detail'),  # http://127.0.0.1:8000/Incidents/id/
    path('add/', IncidentsAdd.as_view(), name='Incidents_add'),
    path('<int:pk>/delete/', IncidentsDelete.as_view(), name='Incidents_delete'),
    path('<int:pk>/update/', IncidentsUpdate.as_view(), name='Incidents_update'),
]
