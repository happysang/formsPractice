from django.contrib import admin
from django.urls import path, include
from formscrud.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('formscrud/', include('formscrud.urls')),
]
