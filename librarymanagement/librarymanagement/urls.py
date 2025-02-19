"""
URL configuration for librarymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view,name="home"),
    path('book',views.book_view),
    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view,name='viewbook'),
    path('update_books/<int:pk>/', views.update_book_view, name='update_book'),
    path('delete_books/<int:pk>/', views.delete_book_view, name='delete_book'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('afterlogin', views.afterlogin_view),
    path('accounts/profile/', views.afterlogin_view),
    path('news', views.news_view, name='news'),
   
    path('addnews', views.add_news, name='add_news'),
    path('viewnews', views.view_news, name='view_news'),
    path('update_news/<int:pk>/', views.update_news, name='update_news'),
    path('delete_news/<int:pk>/', views.delete_news, name='delete_news'),
    path('library_details',views.library_details,name='library_details'),
    path('add_library_details/', views.add_library_details, name='add_library_details'),
    path('view_library_details/', views.view_library_details, name='view_library_details'),

    path('user/',views.user_view,name="user"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userdashboard/',views.userdashboard,name="userdashboard"),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('viewblog', views.viewblog_view,name='viewblog'),
 


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)