from django.urls import path
from .views import StatusViewer

urlpatterns = [
    path('all/', StatusViewer.as_view(), name='status_view' )
]
