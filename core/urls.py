from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('services/', ServiceView.as_view(), name='services'),
    path('services/<int:pk>', ServiceDetail.as_view(), name='servicedetail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>',ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>',ProfileUpdate.as_view(), name='profile_edit'),

    path('order/create/<int:user_pk>/<int:service_pk>',CreateOrder.as_view(), name='createOrder'),
    path('order/users/', ListUserOrder.as_view(), name='listuserorder')

]