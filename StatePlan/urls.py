"""StatePlan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from StatePlan import views
#from .views import RecordListView

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^TMACSP/', views.TMACSP, name='TMACSP'),
    url(r'^$', views.index, name='index'),
    url(r'^record/(?P<id>\d+)/',views.record_detail,name='record_detail'),
    url(r'^TMACSP_record/(?P<id>\d+)/',views.TMACSP_record_detail, name='TMACSP_record_detail'),



   
   
]   
