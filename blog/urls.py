from django.urls import path

from . import views
urlpatterns = [
    path("register",views.register_user,name="register-user"),
    path('home',views.home,name="home"),
    path("create-post",views.create_post,name="create-post"),
    path("delete-post/<int:pk>",views.delete_post,name="delete-post"),
    path("logout",views.logout_view,name="logout"),
    path("login",views.login_view,name="login"),
    path("viewPost/<int:pk>",views.view_post,name="view-post")
]