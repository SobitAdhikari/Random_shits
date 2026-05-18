from django.urls import path
from .views import home
urlpatterns = [
    path('app/',view=home,name='home')
]
