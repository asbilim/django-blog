from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('listings.urls')),
    path('__reload__',include('django_browser_reload.urls')),
    path('auth/',include('authentication.urls')),
    path('auth/',include('django.contrib.auth.urls'))

]
