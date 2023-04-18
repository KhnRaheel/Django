from django.urls import path
from .import views



urlpatterns = [
    
    path("",views.StartPageView.as_view(),name= "start-page"),
    path("posts",views.AllPostView.as_view(),name="posts"),
    path("posts/<slug:slug>",views.PostDetail.as_view(),name="posts-detail"),
    path("read-later", views.ReadLaterView.as_view(),name="read-later")
] 

