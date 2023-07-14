from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.firstpage,name='first'),
    path('stream/',views.streampage,name='stream'),
    path('start/',views.start,name='start'),
    path('stop/',views.stop,name='stop'),  
    path('video_feed/',views.video_feed,name='video_feed'),    
]