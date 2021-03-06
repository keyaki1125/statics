from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('list/', views.List.as_view(), name='list'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),

]