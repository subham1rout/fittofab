from django.urls import path,include
from . import views
from heartrates.views import HearttestView


urlpatterns=[
    path('',views.index,name='index'),
    path('hearttest/',HearttestView.as_view(),name='user-hearttest'),
    path('lessons/',views.lessons,name='user-lessons'),
    path('show_heartrate',views.index,name='show_heartrate'),
    # path('hearttest/heartrate_measure',views.hearttest,name='heartrate_measure')
]