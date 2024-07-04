
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("todoapp.urls"))
]

<<<<<<< HEAD
# if settings.DEBUG:
#     urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
=======
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
]
# 以下を追加する
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> bcb8e254b220e7b90773ea989cb37587fee694c7
