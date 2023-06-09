from django.urls import path
from std import views

urlpatterns = [

    path('',views.home),
    path('home', views.home),
    path('add', views.add),
    path('delete<int:roll>',views.delete),
    path('update<int:roll>', views.update),
    path('doupdate<int:roll>', views.doupdate)

]
