
from app.views import home_view, about_view
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about')
]

