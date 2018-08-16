from django.urls import path ,include
from basic_app import views

app_name='basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login')
    #path('base/',views.base,name='base'),
    #path('login/',views.loggin,name='login')

]