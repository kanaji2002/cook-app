
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("todoapp.urls"))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
