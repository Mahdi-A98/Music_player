from django.urls import path, include
from music import views


app_name = 'music'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('account/', include('account.url')),    
]
