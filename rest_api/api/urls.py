from django.urls import path
from status.views import (StatusViewer,  StatusCreateView, StatusDetailView,
                          StatusListView, StatusUpdateView, StatusDeleteView)

urlpatterns = [
    path('status/<int:id>/', StatusViewer.as_view(), name='status_view'),
    path('statuses/', StatusListView.as_view(), name='status_view'),
    path("status/create/", StatusCreateView.as_view()),
    path("status/<pk>/", StatusDetailView.as_view()),
    path("status/update/<pk>/", StatusUpdateView.as_view()),
    path("status/delete/<pk>/", StatusDeleteView.as_view()),
]
