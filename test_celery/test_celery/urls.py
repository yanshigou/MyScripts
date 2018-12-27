"""test_celery URL Configuration

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
from paopao.views import UploadView, Results, Download, LoginView, GetView, Index, Uploaded

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view()),
    url(r'^results/$', Results.as_view()),
    url(r'^pao/$', UploadView.as_view(), name='upload'),
    url(r'^results/(?P<file_name>.*)/$', Download.as_view(), name='results'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^get/$', GetView.as_view()),
    url(r'^uploaded/$', Uploaded.as_view()),
]
