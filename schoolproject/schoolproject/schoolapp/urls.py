from django.urls import path
from.import views
urlpatterns = [
    path('',views.demo,name="demo"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('new/',views.new,name="new"),
    path('new_page/',views.new_page,name='new_page'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),


]