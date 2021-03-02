from django.urls import path

from .views import index

app_name = 'user'

urlpatterns = [
    path('', index, name="user_dashboard")
]