from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)