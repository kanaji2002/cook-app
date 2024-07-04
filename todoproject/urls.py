
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("todoapp.urls"))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
]
# 以下を追加する
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)