from django.urls import path

from . import views

app_name = "light_house"
urlpatterns = [
    path('', views.index, name='index'),
    path('options',views.options,name='options'),
    path('endpoint',views.endpoint,name='endpoint')
    # path('<int:id>/',views.detail, name="detail")
]

