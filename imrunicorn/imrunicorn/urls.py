"""imrunicorn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
# from . import forms, views
from . import forms, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_home, name='home'),

    path('days_since', views.page_days_since, name='days_since'),
    path('batf/', views.fetch_estimated_batf_days, name='fetch_estimated_batf_days'),

    path('blog/', views.page_blog_read, name='blog_read'),
    path('blog/add/', views.page_blog_add, name='blog_add'),

    path('loaddata/', include('loaddata.urls')),
    path('farminvite/', include('farminvite.urls')),
    path('news/', include('announcements.urls')),

    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/',
         LoginView.as_view
             (
             template_name='imrunicorn/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
]

# # https://docs.djangoproject.com/en/2.0/topics/http/views/#customizing-error-views
# handler404 = 'YOUR_APP_NAME.views.handler404'

handler404 = 'imrunicorn.views.handler404'
handler500 = 'imrunicorn.views.handler500'