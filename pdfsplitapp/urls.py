from django.urls import path
from pdfsplitapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('split/', views.split_pdf, name='split_pdf'),
]
