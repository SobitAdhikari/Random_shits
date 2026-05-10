from django.urls import path
from .views.auth_views import RegisterationViews,LoginView

urlpatterns = [
    path('register/', RegisterationViews.as_view(), name='register'),
    path('login/',LoginView.as_view(),name="login")

]
