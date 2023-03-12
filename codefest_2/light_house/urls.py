from django.urls import path

from . import views

app_name = "light_house"
urlpatterns = [
    path('', views.index, name='index'),
    path('language', views.language, name='language'),
    path('options',views.options,name='options'),
    # path('endpoint',views.endpoint,name='endpoint'),
    path('final',views.final,name='final'),

    path('welcome',views.index),
    path('now',views.now),
    path('documentation',views.documentation),
    path('settling',views.settling),

    path('food',views.food),
    path('shelter',views.shelter),
    path('id',views.id),
    path('ssn',views.ssn),
    path('jobs',views.jobs),
    path('school',views.school),
    path('community',views.community)
]
