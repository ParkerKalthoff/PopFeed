"""PopFeedBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from popfeed import views
from popfeed.views import *

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    # User login paths
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    path('following', following),
# 

    # API paths

        # Pops and Timelines
    path('pops/<int:pop_id>/', Pop),
    path('pops/timeline/anon/<int:page>/', anom_timeline),
    path('pops/timeline/user/<int:page>/', user_timelime),
    path('pops/timeline/user_with_repop/<int:page>/', user_timelime_with_repops),
        # User Interactions
    path('pops/interaction/like/<int:pop_id>/', like),
    path('pops/interaction/repop/<int:pop_id>/', repop),
    

]
