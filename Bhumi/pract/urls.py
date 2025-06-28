from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('toggle-permission/<int:id>/', views.toggle_permission, name='toggle_permission'),
    path('signin/', views.signin_view, name='signin'),  # if not already added
]
