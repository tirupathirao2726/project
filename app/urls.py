from django.urls import path
#from .views import home
from app import views
urlpatterns = [
path('',views.home,name="home"),
 
]