
from app.views import home_view, about_view,save_data_view,delete_view
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),
    path('ds324adwewrrwerr3342', about_view, name='about'),
    path('ds324adwe576ft67jk42', save_data_view, name='save_data'),
    path('rtemdj673992ft67jk42/<int:id>', delete_view, name='delete_data'),
]

