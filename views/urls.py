"""
URL configuration for views project.

    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('only_template/',TemplateView.as_view(template_name='only_template.html'),name='only_template'),
    path('Templateview/',Templateview.as_view(),name='Templateview'),
    path('Insert_data_by_tv/',Insert_data_by_tv.as_view(),name='Insert_data_by_tv'),
    path('Insert_data_by_fv/',Insert_data_by_fv.as_view(),name='Insert_data_by_fv'),
]
