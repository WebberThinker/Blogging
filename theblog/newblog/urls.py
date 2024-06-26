from django.urls import path
from .views import HomeView, DetailPageView, BlogView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail_page/<int:pk>', DetailPageView.as_view(), name='detail_page'),
    path('myblogs', BlogView.as_view() , name='all_blogs'),
]
