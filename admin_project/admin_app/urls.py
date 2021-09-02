from . import views
from django.urls import path

urlpatterns = [
    path('',views.DashBoardView),
    path('admin-login',views.LoginView.as_view()),
    path('create-user',views.CreateUser.as_view()),
    path('logout',views.logoutView)
]
