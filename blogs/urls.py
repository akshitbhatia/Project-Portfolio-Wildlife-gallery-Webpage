from django.urls import path
from . import views

urlpatterns = [
    path('',views.allblogs, name='blogs'),
    path('<int:blog_id>/',views.detail_blog, name='detail')
]
