
from django.contrib import admin
from django.urls import include, path
from project_main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include("user.urls")),
    path('api/app/',include("app.urls")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

