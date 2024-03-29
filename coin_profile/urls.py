from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
     path('signup/', views.SignUp.as_view(), name='signup'),
    # path('login/', views.login, name='login')
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]