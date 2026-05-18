from django.urls import path
from .views.auth_views import RegisterationViews,LoginView,NotificationView

urlpatterns = [
    path('register/', RegisterationViews.as_view(), name='register'),
    path('login/',LoginView.as_view(),name="login"),
    path('notification/',NotificationView.as_view(),name="notification"),
]
