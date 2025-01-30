"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app1 import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.welcome),
    path('movies/', views.get_data),
    path('projection/', views.get_projection, name='projection'),
    path('card/<int:user_id>', views.get_card, name='card'),
    path('buy/<int:user_id>/<int:projection_id>', views.buy_card, name='buy'),
    path('login/', LoginView.as_view(template_name='login.html'),  name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('sold_projection/', views.get_sold_projections, name="sold_projection"),
    path('user_by_card/<int:movie_id>', views.get_user_by_card, name="user_card"),
    path('update_projection/<int:projection_id>', views.update_projection, name='update_projection'),
    path('delete_projection/<int:projection_id>', views.delete_projection, name='delete_projection'),
    path('delete_confirmation/<int:projection_id>', views.delete_confirmation, name='confirm_delete'),
    path('add_projection/', views.add_projection),
]

