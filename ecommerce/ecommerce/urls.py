"""ecommerce URL Configuration

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
import django.contrib.auth
from django.contrib import admin
from django.urls import path
from django.urls import include
from item.views import signup_view
from django.conf import settings
from django.conf.urls.static import static
from pages.views import contact_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item.urls')),
    path('', include('cart.urls')),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup_view),
    path('contact/', contact_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
