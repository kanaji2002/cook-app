from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path,include
from.import views
from .views import TaskCreate, TaskDelete,TaskList,TaskDetail,RegisterTodoApp,TaskListLoginView,TaskUpdate
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path("", TaskList.as_view(),name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
    path("login/", TaskListLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterTodoApp.as_view(), name="register"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)